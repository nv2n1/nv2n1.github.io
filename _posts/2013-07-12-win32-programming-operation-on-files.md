---
title: "C++ std::filesystem Reference for Windows File Operations"
date: 2013-07-12 16:47:44 +0000
author: "Eric Ma"
layout: post
categories: [languages-frameworks]
canonical: /win32-programming-operation-on-files/
---

Use `std::filesystem` for all new code. It’s exception-safe, cross-platform, and requires no external dependencies.

``` cpp
#include <filesystem>
#include <iostream>

void ListAllFiles(const char *folderPath)
{
    for (const auto& entry : std::filesystem::recursive_directory_iterator(folderPath)) {
        std::cout << entry.path() << std::endl;
    }
}
```

To filter by file type, check the entry status:

``` cpp
void ListRegularFiles(const char *folderPath)
{
    for (const auto& entry : std::filesystem::recursive_directory_iterator(folderPath)) {
        if (entry.is_regular_file()) {
            std::cout << entry.path() << std::endl;
        }
    }
}
```

You can also filter by extension:

``` cpp
void ListFilesByExtension(const char *folderPath, const std::string& ext)
{
    for (const auto& entry : std::filesystem::recursive_directory_iterator(folderPath)) {
        if (entry.is_regular_file() && entry.path().extension() == ext) {
            std::cout << entry.path() << std::endl;
        }
    }
}
```

Legacy code using `CFileFind` or other MFC approaches lacks exception handling and cross-platform support. Don’t use these for new projects.

## Recursively Copy a Folder

For simple recursive copies, use `std::filesystem::copy`:

``` cpp
#include <filesystem>
#include <iostream>

bool CopyFolder(const char *srcPath, const char *dstPath)
{
    try {
        std::filesystem::copy(
            srcPath,
            dstPath,
            std::filesystem::copy_options::recursive | 
            std::filesystem::copy_options::overwrite_existing
        );
        return true;
    }
    catch (const std::filesystem::filesystem_error& e) {
        std::cerr << "Copy failed: " << e.what() << std::endl;
        return false;
    }
}
```

By default, `recursive` preserves file permissions and timestamps—important for backups. To skip existing files instead of overwriting:

``` cpp
std::filesystem::copy(
    srcPath,
    dstPath,
    std::filesystem::copy_options::recursive | 
    std::filesystem::copy_options::skip_existing
);
```

For large directory trees where you need progress reporting or cancellation, iterate manually:

``` cpp
bool CopyFolderWithProgress(const char *src, const char *dst)
{
    try {
        std::filesystem::create_directories(dst);

        for (const auto& entry : std::filesystem::recursive_directory_iterator(src)) {
            auto rel_path = std::filesystem::relative(entry.path(), src);
            auto target = std::filesystem::path(dst) / rel_path;

            if (entry.is_directory()) {
                std::filesystem::create_directories(target);
            }
            else {
                std::filesystem::copy_file(
                    entry.path(), 
                    target, 
                    std::filesystem::copy_options::overwrite_existing
                );
                // Report progress or check cancellation flag here
            }
        }
        return true;
    }
    catch (const std::filesystem::filesystem_error& e) {
        std::cerr << "Copy failed: " << e.what() << std::endl;
        return false;
    }
}
```

## Recursively Delete a Folder

Use `std::filesystem::remove_all` for recursive deletion:

``` cpp
#include <filesystem>

bool DeleteFolder(const char *folderPath)
{
    try {
        std::size_t removed = std::filesystem::remove_all(folderPath);
        std::cout << "Removed " << removed << " files/directories" << std::endl;
        return true;
    }
    catch (const std::filesystem::filesystem_error& e) {
        std::cerr << "Delete failed: " << e.what() << std::endl;
        return false;
    }
}
```

`remove_all` returns the count of removed items, useful for verification. This operation is thorough and recursive—use carefully.

To delete selectively (preserving certain files):

``` cpp
bool DeleteFolderSelective(const char *folderPath, const std::string& keepExtension)
{
    try {
        for (const auto& entry : std::filesystem::recursive_directory_iterator(folderPath)) {
            if (entry.is_regular_file() && entry.path().extension() != keepExtension) {
                std::filesystem::remove(entry.path());
            }
        }
        // Clean up empty directories
        std::filesystem::remove_all(folderPath);
        return true;
    }
    catch (const std::filesystem::filesystem_error& e) {
        std::cerr << "Delete failed: " << e.what() << std::endl;
        return false;
    }
}
```

## File Metadata and Permissions

Inspect file properties before performing operations:

``` cpp
#include <filesystem>
#include <chrono>
#include <iostream>

void InspectFile(const char *filePath)
{
    auto path = std::filesystem::path(filePath);

    if (!std::filesystem::exists(path)) {
        std::cerr << "Path does not exist" << std::endl;
        return;
    }

    std::cout << "Is regular file: " << path.is_regular_file() << std::endl;
    std::cout << "Is directory: " << path.is_directory() << std::endl;
    std::cout << "Is symlink: " << path.is_symlink() << std::endl;
    std::cout << "File size: " << std::filesystem::file_size(path) << " bytes" << std::endl;

    auto last_write = std::filesystem::last_write_time(path);
    auto sctp = std::chrono::time_point_cast<std::chrono::system_clock::duration>(
        last_write - std::filesystem::file_time_type::clock::now() + 
        std::chrono::system_clock::now()
    );
    auto tt = std::chrono::system_clock::to_time_t(sctp);
    std::cout << "Last modified: " << std::ctime(&tt);
}
```

## Error Handling Best Practices

Always catch `std::filesystem::filesystem_error` explicitly. Different error codes require different handling:

``` cpp
bool SafeFileCopy(const char *src, const char *dst)
{
    try {
        std::filesystem::copy_file(src, dst);
        return true;
    }
    catch (const std::filesystem::filesystem_error& e) {
        switch (e.code().value()) {
            case static_cast<int>(std::errc::permission_denied):
                std::cerr << "Permission denied: " << e.path1() << std::endl;
                break;
            case static_cast<int>(std::errc::no_such_file_or_directory):
                std::cerr << "File not found: " << e.path1() << std::endl;
                break;
            case static_cast<int>(std::errc::file_exists):
                std::cerr << "Destination exists: " << e.path2() << std::endl;
                break;
            default:
                std::cerr << "Operation failed (" << e.code() << "): " << e.what() << std::endl;
        }
        return false;
    }
}
```

Check preconditions before operations to avoid unnecessary exceptions:

``` cpp
bool SmartCopyFile(const char *src, const char *dst)
{
    try {
        if (!std::filesystem::exists(src)) {
            std::cerr << "Source does not exist" << std::endl;
            return false;
        }

        if (!std::filesystem::is_regular_file(src)) {
            std::cerr << "Source is not a regular file" << std::endl;
            return false;
        }

        std::filesystem::copy_file(
            src, 
            dst, 
            std::filesystem::copy_options::overwrite_existing
        );
        return true;
    }
    catch (const std::filesystem::filesystem_error& e) {
        std::cerr << "Copy failed: " << e.what() << std::endl;
        return false;
    }
}
```

## When to Use Win32 APIs Directly

Stick with `std::filesystem` unless you need Windows-specific functionality:

- **Alternate Data Streams (ADS)** — NTFS-specific metadata
- **Extended file attributes** — Windows property systems
- **Security descriptors** — Fine-grained ACL control
- **UNC paths with authentication** — Complex network share access
- **File change notifications** — Real-time monitoring via `ReadDirectoryChangesW`

For these cases, use Win32 functions directly (`CreateFileA`, `ReadFile`, `WriteFile`, etc.), but manage file handles explicitly with RAII wrappers to prevent leaks:

``` cpp
class FileHandle {
    HANDLE h = INVALID_HANDLE_VALUE;
public:
    FileHandle(const char *path, DWORD access) {
        h = CreateFileA(path, access, 0, nullptr, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, nullptr);
        if (h == INVALID_HANDLE_VALUE) throw std::runtime_error("CreateFile failed");
    }
    ~FileHandle() { if (h != INVALID_HANDLE_VALUE) CloseHandle(h); }
    HANDLE get() const { return h; }
};
```

## C++17 Requirement

`std::filesystem` requires C++17. For older codebases, use `Boost.Filesystem`, which provides similar semantics and better cross-platform support than legacy approaches.
