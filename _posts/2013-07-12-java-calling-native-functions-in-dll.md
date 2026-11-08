---
title: "Calling C/C++ DLLs from Java with JNI on Windows"
date: 2013-07-12 16:47:40 +0000
modified: 2026-04-11 17:51:49 +0000
author: "Eric Ma"
layout: post
categories: [development-best-practices]
canonical: /java-calling-native-functions-in-dll/
---

JNI lets you call native C/C++ functions from Java on Windows. This guide covers the complete workflow with modern tooling.

## Prerequisites

- JDK 17 or later (JDK 21 LTS recommended)
- Microsoft Visual Studio 2022 or Visual Studio Build Tools
- MSVC C/C++ compiler
- `javac` for compilation and header generation

## Step 1: Write the Java Code

Create your Java class with native method declarations:

``` java
public class JNITest {
    public static void main(String[] args) {
        if (args.length > 0) {
            try {
                int x = Integer.parseInt(args[0]);
                int result = new MyNative().cubecal(x);
                System.out.println(result);
            } catch (NumberFormatException e) {
                System.err.println("Invalid input: " + e.getMessage());
            }
        } else {
            System.out.println("Usage: java JNITest <integer>");
        }
    }
}

class MyNative {
    public native int cubecal(int x);

    static {
        System.loadLibrary("mynative");
    }
}
```

The static initializer loads the native library when the class is first accessed. This is cleaner than calling `System.loadLibrary()` in `main()` since it guarantees the library loads before any native method is invoked.

## Step 2: Generate the JNI Header File

Compile the Java source and generate the native header in one step:

``` bash
javac -h . JNITest.java
```

This generates `MyNative.h` with the required JNI function signatures. The `-h` flag (available since JDK 10) replaces the deprecated `javah` tool entirely.

View the generated header to understand the expected function signature:

``` bash
type MyNative.h
```

The header file contains the exact C function signature you need to implement.

## Step 3: Write the Native Code

Create `MyNative.c` with the implementation:

``` c
#include "jni.h"
#include "MyNative.h"
#include <stdio.h>

int cube(int x) {
    return (x * x * x);
}

JNIEXPORT jint JNICALL Java_MyNative_cubecal
(JNIEnv *env, jobject obj, jint x) {
    return cube(x);
}
```

The function name must follow the JNI naming convention: `Java_<ClassName>_<MethodName>`. The generated header file provides the exact signature to match.

**Key points:**

- `JNIEXPORT` and `JNICALL` are JNI macros that ensure correct calling conventions on Windows
- `JNIEnv *env` provides access to JNI functions like throwing exceptions or calling back into Java
- `jobject obj` is a reference to the Java object (`this`) — use `NULL` if it’s a static native method
- Return type `jint` maps to Java `int`; JNI provides similar type mappings for all Java primitives and objects

## Step 4: Configure Visual Studio Project

Create a new C++ DLL project in Visual Studio 2022.

### Add JNI Headers

In Project Properties → VC++ Directories, add these paths to **Include Directories**:

    %JAVA_HOME%\include
    %JAVA_HOME%\include\win32

Or edit the `.vcxproj` file directly:

``` xml
<PropertyGroup>
  <OutDir>$(SolutionDir)bin\</OutDir>
  <TargetName>mynative</TargetName>
</PropertyGroup>
<ItemDefinitionGroup>
  <ClCompile>
    <AdditionalIncludeDirectories>$(JAVA_HOME)\include;$(JAVA_HOME)\include\win32;%(AdditionalIncludeDirectories)</AdditionalIncludeDirectories>
    <WarningLevel>Level4</WarningLevel>
    <PreprocessorDefinitions>WIN32;_WINDOWS;%(PreprocessorDefinitions)</PreprocessorDefinitions>
  </ClCompile>
</ItemDefinitionGroup>
```

### Set the DLL Name

Ensure the output DLL name matches the library name in `System.loadLibrary()`. In this example, set **Target Name** to `mynative` (which creates `mynative.dll`).

### Verify JAVA_HOME

Confirm the `JAVA_HOME` environment variable points to a valid JDK:

``` cmd
echo %JAVA_HOME%
dir %JAVA_HOME%\include
dir %JAVA_HOME%\include\win32
```

If unset, add it to your system environment variables or set it in your build configuration.

## Step 5: Build the DLL

In Visual Studio, select **Release** configuration (not Debug for production) and the correct platform:

- **x64** for 64-bit Java (standard on modern systems)
- **Win32** for 32-bit Java (rare; avoid unless explicitly required)

Build the solution and verify the DLL was created:

``` cmd
dir bin\mynative.dll
```

The output should show `mynative.dll` with a size greater than 0.

## Step 6: Run the Program

Place `mynative.dll` in the current working directory and run:

``` bash
java -Djava.library.path=. JNITest 9
```

Output:

    729

The result is correct: 9³ = 729.

### Alternative DLL Placement

Instead of using `-Djava.library.path`, you can:

- Place the DLL in the same directory as your compiled `.class` files
- Add the DLL directory to Windows `PATH`
- Use an absolute path with `System.load()` instead of `System.loadLibrary()`

``` java
System.load("C:\\path\\to\\mynative.dll");
```

## Architecture Matching

Modern systems run 64-bit Java by default. The DLL architecture must match the JVM architecture or you’ll get `UnsatisfiedLinkError`.

Check your Java bitness:

``` bash
java -version
```

Look for “64-Bit Server VM” (standard) or “32-Bit Client VM” (rare). Compile your DLL accordingly:

| Java Version | DLL Platform |
|--------------|--------------|
| 64-bit       | x64          |
| 32-bit       | Win32        |

If you need to support both, build two separate DLLs and load them conditionally:

``` java
String osArch = System.getProperty("os.arch");
if ("amd64".equals(osArch) || "x86_64".equals(osArch)) {
    System.loadLibrary("mynative_x64");
} else if ("x86".equals(osArch)) {
    System.loadLibrary("mynative_x86");
}
```

## Troubleshooting

### UnsatisfiedLinkError: cannot open shared object file

**Verify the DLL exists in the library path:**

``` bash
java -Djava.library.path=. -cp . JNITest 9
```

**Check that JVM and DLL bitness match:**

``` bash
java -version
# Look for "64-Bit" or "32-Bit"
```

**Verify the DLL filename matches the library name in `System.loadLibrary()`:**

Windows is case-insensitive for filenames, but the actual `.dll` file must exist. Ensure `System.loadLibrary("mynative")` corresponds to `mynative.dll` in the library path.

### Compilation errors in Visual Studio

**Verify JAVA_HOME is set:**

``` cmd
echo %JAVA_HOME%
dir %JAVA_HOME%\include
dir %JAVA_HOME%\include\win32
```

Both directories must exist. If `%JAVA_HOME%` is empty or points to a JRE instead of a JDK, compilation will fail.

**Ensure you’re compiling C/C++, not C#:**

The project type must be “Visual C++” or “Windows Desktop C++”, not “C#”. If using a C# project, you’ll get errors about `jni.h` not being found.

### Symbol not found or method signature mismatch

**Regenerate the header file and rebuild:**

``` bash
javac -h . JNITest.java
```

Then verify the C function name matches the generated header exactly. Copy the entire function signature from the header file into your `.c` file.

**Clean and rebuild the entire Visual Studio project:**

``` cmd
# In Visual Studio: Build → Clean Solution
# Then: Build → Build Solution
```

A stale `.obj` file can cause linker errors if the function signature changed.

### DLL fails to load at runtime

**Check Windows Event Viewer for dependency issues:**

Open Event Viewer (eventvwr.msc) and look under Windows Logs → System for errors related to your DLL. Common issues include missing Visual C++ Runtime libraries.

**List all DLL dependencies:**

``` cmd
dumpbin /imports bin\mynative.dll
```

This shows all DLLs that `mynative.dll` depends on. Ensure they’re available on the target system.

**Install the Visual C++ Runtime:**

If the DLL depends on VCRUNTIME140.dll or similar, install the corresponding Visual C++ Redistributable from Microsoft on the target machine. For development, this is usually already installed with Visual Studio.

## Performance Considerations

- Use **Release** configuration for production; Debug adds significant overhead
- JNI has overhead (~100-200 nanoseconds per call). Keep frequently-called native methods lightweight and batch operations where possible
- Move computationally intensive work to C/C++, but keep Java logic in Java — don’t push everything to native code
- For large projects, consider CMake or Meson instead of the Visual Studio GUI to manage build complexity

## Example: Passing Strings and Arrays

JNI can handle more than primitives. Here’s an example with strings:

``` c
JNIEXPORT jstring JNICALL Java_MyNative_processString
(JNIEnv *env, jobject obj, jstring input) {
    const char *str = (*env)->GetStringUTFChars(env, input, NULL);
    // Process str...
    char result[256];
    sprintf_s(result, sizeof(result), "Processed: %s", str);
    (*env)->ReleaseStringUTFChars(env, input, str);
    return (*env)->NewStringUTF(env, result);
}
```

And the Java counterpart:

``` java
public native String processString(String input);
```

Always release acquired JNI references with `Release*` functions to avoid memory leaks.
