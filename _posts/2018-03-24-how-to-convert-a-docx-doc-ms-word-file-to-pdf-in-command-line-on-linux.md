---
title: "Converting Word Documents to PDF on Linux"
date: 2018-03-24 08:19:58 +0000
layout: post
canonical: https://www.systutorials.com/how-to-convert-a-docx-doc-ms-word-file-to-pdf-in-command-line-on-linux/
---

Several tools can convert `.doc` and `.docx` files to PDF from the command line. Here’s what works in practice.

### LibreOffice (most common approach)

The standard command is:

``` bash
libreoffice --headless --convert-to pdf --outdir /path/to/output/ /path/to/file.docx
```

This works well on systems with X11 available. However, on truly headless servers, `--headless` doesn’t fully suppress X11 requirements—LibreOffice will still fail without a display server, even though it won’t render anything visually.

For headless environments, use `xvfb-run` to provide a virtual X server:

``` bash
xvfb-run -a libreoffice --headless --convert-to pdf --outdir /path/to/output/ /path/to/file.docx
```

The `-a` flag tells xvfb-run to auto-select a display number. This works reliably in cron jobs and background processes.

**Batch conversion example:**

``` bash
for file in *.docx; do
  xvfb-run -a libreoffice --headless --convert-to pdf --outdir ./pdfs/ "$file"
done
```

LibreOffice handles most `.doc` and `.docx` files reasonably well, though complex formatting may not translate perfectly.

### Pandoc (lightweight alternative)

For simpler documents, Pandoc offers a lighter-weight option:

``` bash
pandoc input.docx -o output.pdf
```

Pandoc requires a LaTeX installation for PDF output (`texlive-latex-base` on Debian/Ubuntu). It’s faster than LibreOffice for basic conversions but may drop some formatting.

``` bash
apt-get install pandoc texlive-latex-base texlive-latex-extra
```

### Unoconv (LibreOffice wrapper)

Unoconv wraps LibreOffice with a simpler interface and can run a persistent server:

``` bash
unoconv -f pdf input.docx
```

For batch jobs, start the listener once:

``` bash
soffice --headless --accept="socket,host=127.0.0.1,port=2002;urp;" &
unoconv -s localhost:2002 -f pdf input.docx
```

This avoids launching LibreOffice repeatedly.

### Libreoffice with timeout (production consideration)

LibreOffice processes sometimes hang. Wrap conversions with a timeout:

``` bash
timeout 30 xvfb-run -a libreoffice --headless --convert-to pdf \
  --outdir /path/to/output/ /path/to/file.docx
```

### Python automation

For application integration, use `python-pptx` or `python-docx` libraries combined with conversion:

``` bash
pip install python-docx
```

Then script the conversion:

``` python
import subprocess
import sys

def convert_docx_to_pdf(docx_path, output_dir):
    cmd = [
        'xvfb-run', '-a',
        'libreoffice', '--headless', '--convert-to', 'pdf',
        '--outdir', output_dir,
        docx_path
    ]
    result = subprocess.run(cmd, capture_output=True, timeout=60)
    return result.returncode == 0

if __name__ == '__main__':
    convert_docx_to_pdf(sys.argv[1], sys.argv[2])
```

### Comparison summary

| Tool        | Speed  | Quality | Dependencies | Headless          |
|-------------|--------|---------|--------------|-------------------|
| LibreOffice | Slow   | Good    | Heavy        | Needs xvfb        |
| Pandoc      | Fast   | Basic   | Medium       | Yes               |
| Unoconv     | Medium | Good    | Heavy        | Yes (with server) |

For most Linux servers, LibreOffice + xvfb-run is the standard choice despite overhead. Pandoc works well for text-heavy documents. Always test with your specific document types before deploying to production.

## Troubleshooting Common Issues

When encountering problems on Linux systems, follow a systematic approach. Check system logs first using journalctl for systemd-based distributions. Verify service status with systemctl before attempting restarts. For network issues, use ip addr and ss -tulpn to diagnose connectivity problems.

Package management issues often stem from stale caches. Run dnf clean all on Fedora or apt clean on Ubuntu before retrying failed installations. If a package has unmet dependencies, try resolving them with dnf autoremove or apt autoremove.

## Related System Commands

These commands are frequently used alongside the tools discussed in this article:

- systemctl status service-name – Check if a service is running
- journalctl -u service-name -f – Follow service logs in real time
- rpm -qi package-name – Query installed package information
- dnf history – View package transaction history
- top or htop – Monitor system resource usage

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
