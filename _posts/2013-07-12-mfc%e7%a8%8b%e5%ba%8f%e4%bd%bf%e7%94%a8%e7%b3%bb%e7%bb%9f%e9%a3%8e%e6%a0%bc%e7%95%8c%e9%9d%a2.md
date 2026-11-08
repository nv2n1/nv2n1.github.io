---
title: "Enabling Modern Visual Styles in MFC Applications"
date: 2013-07-12 16:47:41 +0000
layout: post
permalink: /mfc%e7%a8%8b%e5%ba%8f%e4%bd%bf%e7%94%a8%e7%b3%bb%e7%bb%9f%e9%a3%8e%e6%a0%bc%e7%95%8c%e9%9d%a2/
canonical: https://www.systutorials.com/mfc%e7%a8%8b%e5%ba%8f%e4%bd%bf%e7%94%a8%e7%b3%bb%e7%bb%9f%e9%a3%8e%e6%a0%bc%e7%95%8c%e9%9d%a2/
---

MFC applications built with older Visual C++ versions often render with the classic Windows 95 appearance, ignoring modern system visual styles. This happens because the application isn’t explicitly linked to Common Controls v6.0, which provides visual styles support. On modern Windows systems (Windows Vista and later), this looks particularly jarring compared to contemporary applications.

The solution involves embedding a manifest file that declares the application’s dependency on Common Controls v6.0. The approach varies depending on your Visual C++ version and project configuration.

## Visual C++ 6.0 and Older Versions

### Creating the Manifest File

In your `res/` directory, create a file named `{ProgramName}.exe.manifest`. For example, if your executable is `myapp.exe`, name it `myapp.exe.manifest`.

Save the following as UTF-8 without BOM:

``` xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <assemblyIdentity
    version="1.0.0.0"
    processorArchitecture="*"
    name="MyApplication"
    type="win32"
  />
  <description>My Application</description>
  <dependency>
    <dependentAssembly>
      <assemblyIdentity
        type="win32"
        name="Microsoft.Windows.Common-Controls"
        version="6.0.0.0"
        processorArchitecture="*"
        publicKeyToken="6595b64144ccf1df"
        language="*"
      />
    </dependentAssembly>
  </dependency>
</assembly>
```

### Embedding the Manifest as a Resource

Open your `.rc` or `.rc2` file and add this line:

    1 24 MOVEABLE PURE "res/myapp.exe.manifest"

Adjust the path to match your manifest filename. The `24` is the resource type identifier for manifests. Perform a clean rebuild—the manifest will be embedded as a resource in the final executable.

### Font Optimization

Set dialog and window fonts to TrueType fonts like Tahoma or Segoe UI to ensure proper font rendering on modern Windows versions. In the resource editor, select each dialog and set the font property accordingly.

## Visual C++ 2008 and Later

Modern versions of Visual C++ include automatic manifest support through linker pragmas, which is simpler than manual embedding.

### Unicode Projects

If your project uses Unicode character encoding, visual styles are typically enabled automatically in the generated manifest. No additional configuration is needed.

### ANSI/Multibyte Projects

Open `stdafx.h` and locate the manifest pragma comments near the end of the file. They’re typically wrapped in `#ifdef _UNICODE`. Remove the preprocessor guards so the pragmas run unconditionally:

``` cpp
#if defined _M_IX86
#pragma comment(linker,"/manifestdependency:\"type='win32' name='Microsoft.Windows.Common-Controls' version='6.0.0.0' processorArchitecture='x86' publicKeyToken='6595b64144ccf1df' language='*'\"")
#elif defined _M_IA64
#pragma comment(linker,"/manifestdependency:\"type='win32' name='Microsoft.Windows.Common-Controls' version='6.0.0.0' processorArchitecture='ia64' publicKeyToken='6595b64144ccf1df' language='*'\"")
#elif defined _M_X64
#pragma comment(linker,"/manifestdependency:\"type='win32' name='Microsoft.Windows.Common-Controls' version='6.0.0.0' processorArchitecture='amd64' publicKeyToken='6595b64144ccf1df' language='*'\"")
#else
#pragma comment(linker,"/manifestdependency:\"type='win32' name='Microsoft.Windows.Common-Controls' version='6.0.0.0' processorArchitecture='*' publicKeyToken='6595b64144ccf1df' language='*'\"")
#endif
```

This pragma is injected at link time, embedding the manifest dependency into the executable. Rebuild and the application will respect system visual styles.

## Verification and Troubleshooting

After enabling visual styles, perform a clean rebuild and test on Windows Vista or later. Buttons, checkboxes, scrollbars, list controls, and other standard controls should render with the active system theme.

If controls still appear flat and classic, check the following:

- **Manifest XML syntax**: Validate the XML is well-formed with no byte-order mark (BOM) on UTF-8 files. Use an XML validator if unsure.
- **Resource path**: Verify the `.rc` entry points to the correct manifest file path relative to the `.rc` file location.
- **Clean rebuild**: Do a full rebuild, not an incremental compile. Delete the `Debug/` and `Release/` folders to ensure old binaries aren’t cached.
- **System theme**: Confirm the system has an active visual style theme (not disabled in accessibility settings).
- **Linker output**: In Visual Studio, examine the linker output during build to confirm manifest dependencies are being embedded. Search for the string “manifestdependency” in the build log.
- **Bitness mismatch**: Ensure you’re rebuilding for the correct platform (x86, x64, or ARM64). The manifest architecture declaration must match the compiled executable.

### External Manifest as Fallback

For VC6 projects that won’t link the manifest as a resource, place an external manifest file alongside the executable with the same filename plus `.manifest` extension (e.g., `myapp.exe.manifest` in the same directory as `myapp.exe`). Windows will load it automatically, though embedding is more reliable and portable.

## Modern Alternatives

If maintaining legacy MFC projects becomes unwieldy, consider modernizing to Windows Presentation Foundation (WPF) or WinUI for new applications. For gradual migration, WinUI 3 can be embedded in MFC applications via interop, allowing you to leverage modern visual styles in new features while keeping existing MFC code intact.
