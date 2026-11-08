---
title: "Export PowerPoint Slides at Higher DPI for Better Print Quality"
date: 2015-11-03 14:31:48 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-change-dpi-exported-images-slides-powerpoint/
---

PowerPoint exports slides at 96 DPI by default, which is too low for professional printing. Print shops typically require 150 DPI for acceptable quality or 300 DPI for high-quality output. The UI export options in PowerPoint don’t reliably control the actual output DPI—you need to change a registry setting on Windows or use alternative methods on macOS.

## Windows: Registry-Based DPI Control

The export resolution is controlled by the `ExportBitmapResolution` registry key. PowerPoint reads this value on export and maxes out at 307 DPI.

### Locate Your Office Version

Open PowerPoint and go to **File → Account** (or **Help** on older versions) to find your version number:

- Office 2013: 15.0
- Office 2016: 16.0
- Office 2019: 16.0
- Microsoft 365: 16.0

The registry path is: `HKEY_CURRENT_USER\Software\Microsoft\Office\VERSION\PowerPoint\Options`

Replace VERSION with your number (e.g., `16.0` for Office 2019/365).

### DPI to Hexadecimal Conversion

The `ExportBitmapResolution` value uses hexadecimal format:

| DPI           | Hex Value |
|---------------|-----------|
| 96 (default)  | 0x60      |
| 150           | 0x96      |
| 200           | 0xC8      |
| 300           | 0x12C     |
| 307 (maximum) | 0x133     |

### Method 1: Registry File (.reg)

Create a file named `powerpoint-dpi-300.reg` and add this content for Office 365/2019/2016:

    Windows Registry Editor Version 5.00

    [HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\PowerPoint\Options]
    "ExportBitmapResolution"=dword:0000012c

Then:

1.  Close PowerPoint completely
2.  Right-click the .reg file and select **Merge**
3.  Confirm the Windows User Account Control prompt
4.  Restart PowerPoint

For multiple Office versions, add separate registry sections:

    Windows Registry Editor Version 5.00

    [HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\PowerPoint\Options]
    "ExportBitmapResolution"=dword:0000012c

    [HKEY_CURRENT_USER\Software\Microsoft\Office\15.0\PowerPoint\Options]
    "ExportBitmapResolution"=dword:0000012c

### Method 2: Manual Registry Editor Access

1.  Press **Win+R**, type `regedit`, and press Enter
2.  Navigate to `HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\PowerPoint\Options` (adjust version as needed)
3.  Right-click the empty space on the right and select **New → DWORD (32-bit) Value**
4.  Name it `ExportBitmapResolution`
5.  Double-click it and enter `300` (in decimal, not hex—the editor converts automatically)
6.  Click OK and close the registry editor
7.  Restart PowerPoint

## macOS: Alternative Approach

macOS doesn’t expose this registry setting. Instead, export at standard resolution and use command-line tools to adjust metadata, or export directly to PDF and convert:

``` bash
# Using sips (built-in on macOS) to set DPI metadata
sips -s dpiWidth 300 -s dpiHeight 300 input.png -o output.png
```

Note: This adjusts metadata only and doesn’t improve actual pixel quality.

## Exporting at the New DPI

After applying the registry change:

1.  Open your presentation in PowerPoint
2.  Go to **File → Export As** (or **Save As**)
3.  Choose your format: PNG, JPEG, TIFF, or PDF
4.  Click **Export** and configure settings if prompted
5.  Save the file

## Verify the DPI

Check the exported image’s DPI using ImageMagick’s `identify` command:

``` bash
identify -verbose exported-slide.png | grep Resolution
```

Or on Windows with ImageMagick installed:

``` powershell
identify -verbose exported-slide.png | findstr Resolution
```

You should see output like:

    Resolution: 300x300 PixelsPerInch

## Post-Processing with ImageMagick

If you can’t or don’t want to change the registry, export at default resolution and re-sample afterward:

``` bash
convert slide-96dpi.png -density 300 -units PixelsPerInch slide-300dpi.png
```

Be aware this only changes the DPI metadata—it doesn’t improve actual image quality. The pixel count stays the same. For genuine quality improvement, export at higher DPI directly from PowerPoint.

## Revert to Default

To restore 96 DPI, either:

1.  Set `ExportBitmapResolution` to `0x60` in the registry
2.  Delete the `ExportBitmapResolution` key entirely (PowerPoint will use the default)

If you’re bulk-exporting slides, consider exporting to PDF first at high quality, then converting the PDF to images using `ghostscript` or `pdfimages` for better control.
