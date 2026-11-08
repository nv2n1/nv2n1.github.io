---
title: "Recursively List All Files and Directories in C++"
date: 2018-03-24 11:54:56 +0000
layout: post
canonical: https://www.systutorials.com/how-to-iterate-all-dirs-and-files-in-a-dir-in-c/
---

For iterating through directories and files in C++, you have several options depending on your needs and C++ standard version.

### Using `<filesystem>` (C++17 and Later — Recommended)

The modern approach uses `std::filesystem`, which is cleaner, safer, and handles cross-platform differences for you:

``` cpp
#include <filesystem>
#include <iostream>
#include <string>

namespace fs = std::filesystem;

int ListDir(const std::string& path) {
  try {
    for (const auto& entry : fs::directory_iterator(path)) {
      std::cout << entry.path().filename().string() << std::endl;
    }
  } catch (const fs::filesystem_error& e) {
    std::cerr << "Error: " << e.what() << std::endl;
    return -1;
  }
  return 0;
}

int main(int argc, char* argv[]) {
  if (argc < 2) {
    std::cerr << "Usage: " << argv[0] << " path\n";
    return 1;
  }
  return ListDir(argv[1]);
}
```

To distinguish between files and directories:

``` cpp
for (const auto& entry : fs::directory_iterator(path)) {
  if (entry.is_directory()) {
    std::cout << "[DIR]  " << entry.path().filename().string() << std::endl;
  } else if (entry.is_regular_file()) {
    std::cout << "[FILE] " << entry.path().filename().string() << std::endl;
  }
}
```

For recursive traversal, use `std::filesystem::recursive_directory_iterator`:

``` cpp
for (const auto& entry : fs::recursive_directory_iterator(path)) {
  std::cout << entry.path().string() << std::endl;
}
```

### Using POSIX `opendir()` and `readdir()`

If you’re stuck with older C++ standards or legacy systems, the POSIX approach still works:

``` cpp
#include <cstdio>
#include <dirent.h>
#include <iostream>
#include <string>
#include <sys/stat.h>

int ListDir(const std::string& path) {
  DIR* dp = opendir(path.c_str());
  if (!dp) {
    perror("opendir");
    return -1;
  }

  struct dirent* entry;
  while ((entry = readdir(dp))) {
    std::string fullpath = path + "/" + entry->d_name;
    struct stat st;

    if (stat(fullpath.c_str(), &st) == 0) {
      if (S_ISDIR(st.st_mode)) {
        std::cout << "[DIR]  " << entry->d_name << std::endl;
      } else if (S_ISREG(st.st_mode)) {
        std::cout << "[FILE] " << entry->d_name << std::endl;
      }
    }
  }

  closedir(dp);
  return 0;
}

int main(int argc, char* argv[]) {
  if (argc < 2) {
    std::cerr << "Usage: " << argv[0] << " path\n";
    return 1;
  }
  return ListDir(argv[1]);
}
```

Note: The POSIX approach requires `stat()` to distinguish files from directories, since `d_type` is not guaranteed to be set on all systems.

### Recursive Directory Traversal

With `<filesystem>`, recursion is handled automatically:

``` cpp
void ListDirRecursive(const std::string& path, int depth = 0) {
  try {
    for (const auto& entry : fs::recursive_directory_iterator(path)) {
      std::string indent(entry.depth() * 2, ' ');
      std::cout << indent << entry.path().filename().string();
      if (entry.is_directory()) {
        std::cout << "/";
      }
      std::cout << std::endl;
    }
  } catch (const fs::filesystem_error& e) {
    std::cerr << "Error: " << e.what() << std::endl;
  }
}
```

With the POSIX approach, you need to implement recursion manually:

``` cpp
void ListDirRecursive(const std::string& path) {
  DIR* dp = opendir(path.c_str());
  if (!dp) return;

  struct dirent* entry;
  while ((entry = readdir(dp))) {
    if (entry->d_name[0] == '.') continue; // Skip . and ..

    std::string fullpath = path + "/" + entry->d_name;
    struct stat st;

    if (stat(fullpath.c_str(), &st) == 0 && S_ISDIR(st.st_mode)) {
      std::cout << fullpath << std::endl;
      ListDirRecursive(fullpath);
    } else {
      std::cout << fullpath << std::endl;
    }
  }
  closedir(dp);
}
```

### Compilation

For `<filesystem>` on older GCC versions, link with `-lstdc++fs`:

``` bash
g++ -std=c++17 -o listdir main.cpp -lstdc++fs
```

Modern GCC and Clang don’t require this flag.

Use `<filesystem>` for new projects—it’s safer, more readable, and handles edge cases properly. Reserve POSIX APIs for legacy codebases or embedded systems with limited C++ standard library support.
