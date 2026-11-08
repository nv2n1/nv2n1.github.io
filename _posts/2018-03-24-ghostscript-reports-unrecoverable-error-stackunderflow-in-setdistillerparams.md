---
title: "Fix Ghostscript stackunderflow Error in PDF Conversion"
date: 2018-03-24 08:21:12 +0000
author: "Eric Ma"
layout: post
categories: [algorithms-data-structures]
canonical: /ghostscript-reports-unrecoverable-error-stackunderflow-in-setdistillerparams/
---

When converting PostScript to PDF using ps2pdf with certain PDFSETTINGS options, you may hit this error:

    GPL Ghostscript 9.10: Set UseCIEColor for UseDeviceIndependentColor to work properly.
    Unrecoverable error: stackunderflow in .setdistillerparams

This occurs when Ghostscript’s internal stack runs out of expected values during PDF distiller parameter processing. The root cause is usually conflicting color space settings or incompatible parameter combinations that don’t work together.

## Quick fix: Disable color conversion

The most reliable solution is to prevent Ghostscript from attempting color space conversions:

``` bash
ps2pdf -dColorConversionStrategy=/LeaveColorUnchanged \
  -dPDFSETTINGS=/printer input.ps output.pdf
```

This preserves your PostScript file’s original color spaces without triggering the distiller stack issue. Use this as your default approach for print workflows.

## Alternative: Use prepress settings

If you need PDFSETTINGS, switch from `/printer` to `/prepress`:

``` bash
ps2pdf -dPDFSETTINGS=/prepress input.ps output.pdf
```

The prepress profile uses more conservative parameter combinations and typically avoids conflicting settings.

## Direct Ghostscript approach for print output

For better control over print-destined PDFs, bypass ps2pdf and call Ghostscript directly:

``` bash
gs -q -dNOPAUSE -dBATCH -dSAFER \
  -dMediaClass=Letter \
  -dDEVICEWIDTHPOINTS=612 \
  -dDEVICEHEIGHTPOINTS=792 \
  -dFitPage \
  -sDEVICE=pdfwrite \
  -sOutputFile=output.pdf \
  input.ps
```

This approach gives you explicit control over output dimensions and color handling without relying on preset PDFSETTINGS combinations that might conflict.

## Explicit color handling parameters

If you need fine-grained control, specify color settings directly:

``` bash
ps2pdf -dEmbedAllFonts=true \
  -dSubsetFonts=true \
  -dColorConversionStrategy=/RGB \
  -dProcessColorModel=/DeviceRGB \
  input.ps output.pdf
```

Avoid mixing `-dColorConversionStrategy` with `-dPDFSETTINGS` in the same command, as this commonly triggers the stack underflow.

## Why the error happens

The stackunderflow in `.setdistillerparams` indicates internal parameter stack exhaustion. Common culprits:

- CIE color space requirements conflicting with device color models
- Multiple contradictory color conversion flags set simultaneously
- PostScript color space definitions clashing with PDFSETTINGS expectations
- Mixing high-level PDFSETTINGS with low-level device parameters

## Version considerations

If you’re running Ghostscript 9.10 or older (check with `gs --version`), update to a current version:

``` bash
sudo apt install ghostscript  # Debian/Ubuntu
sudo dnf install ghostscript  # Fedora/RHEL
```

Modern versions handle color space management and parameter stacking much more robustly. Most issues disappear after updating.

## Debugging tips

To see what Ghostscript is processing, add verbose output:

``` bash
ps2pdf -dDEBUG -dNOPAUSE -dColorConversionStrategy=/LeaveColorUnchanged \
  -dPDFSETTINGS=/printer input.ps output.pdf 2>&1 | head -50
```

If you still hit errors with the LeaveColorUnchanged approach, your PostScript file itself may have structural issues. Test with a simple PostScript file first to isolate whether the problem is file-specific or configuration-wide.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
