---
title: "Building Zlib from Source on Ubuntu"
date: 2018-07-26 10:09:01 +0000
layout: post
canonical: https://www.systutorials.com/how-to-install-the-zlib-library-in-ubuntu/
---

Zlib is a foundational open-source compression library implementing the DEFLATE algorithm. It powers gzip, PNG, HTTP compression, and countless applications. While Ubuntu’s package repositories provide pre-built binaries, compiling from source lets you use the latest version, customize the installation path, enable specific compile-time features, and maintain multiple versions simultaneously. This guide covers building zlib on Ubuntu 24.04 LTS and other recent releases.

## Prerequisites

Install the C compiler and build toolchain:

``` bash
sudo apt update
sudo apt install build-essential wget
```

`build-essential` includes gcc, make, and related utilities; `wget` fetches the source archive.

## Download and verify the source

Fetch the latest stable release:

``` bash
wget https://zlib.net/zlib-1.3.2.tar.gz
```

Alternatively, use the rolling-release permalink to always get the latest version:

``` bash
wget https://zlib.net/current/zlib.tar.gz
```

Verify the SHA-256 hash against the value published on <a href="https://zlib.net" rel="nofollow noopener" target="_blank">zlib.net</a>:

``` bash
sha256sum zlib-1.3.2.tar.gz
```

Cross-check the output with the official hash listed on their website before proceeding.

## Extract and configure

``` bash
tar -xf zlib-1.3.2.tar.gz
cd zlib-1.3.2
```

Run the configure script. By default, it uses `/usr/local` as the installation prefix:

``` bash
./configure
```

For a custom installation location, specify `--prefix`. This is essential when you need multiple zlib versions, lack root access, or want to isolate the installation:

``` bash
./configure --prefix=$HOME/.local
```

Or to a system-wide custom path:

``` bash
./configure --prefix=/opt/zlib
```

View all available options:

``` bash
./configure --help
```

Key configuration flags include:

- `--static` — build only static libraries (`libz.a`)
- `--shared` — build only shared libraries (`libz.so`; default behavior)
- `--64` — optimize for 64-bit systems (usually auto-detected)
- `--disable-shared` — disable shared library compilation if you only need static linking

## Build and install

``` bash
make
sudo make install
```

If you configured with a user-owned prefix (such as `$HOME/.local`), omit `sudo`:

``` bash
make
make install
```

By default, `make install` places files at:

- **Libraries**: `/usr/local/lib/` — contains `libz.a` (static) and `libz.so` (shared)
- **Headers**: `/usr/local/include/` — contains `zlib.h` and `zconf.h`
- **pkg-config**: `/usr/local/lib/pkgconfig/zlib.pc`

## Update the dynamic linker cache

After installing to a system directory, refresh the linker cache:

``` bash
sudo ldconfig
```

For custom system-wide prefixes, add the library directory to the linker search path:

``` bash
echo "/opt/zlib/lib" | sudo tee /etc/ld.so.conf.d/zlib.conf
sudo ldconfig
```

For user-local prefixes like `$HOME/.local`, ldconfig isn’t typically needed. Instead, set `LD_LIBRARY_PATH` at runtime or permanently in your shell profile:

``` bash
export LD_LIBRARY_PATH=$HOME/.local/lib:$LD_LIBRARY_PATH
```

Add this to your `~/.bashrc` or `~/.zshrc` for persistence.

## Verify the installation

Check the installed library version:

``` bash
ldconfig -v 2>/dev/null | grep libz
```

Expected output:

    libz.so.1 -> libz.so.1.3.2

Inspect the header file:

``` bash
grep ZLIB_VERSION /usr/local/include/zlib.h
```

Expected output:

    #define ZLIB_VERSION "1.3.2"

If available, check the zlib-config tool:

``` bash
which zlib-config && zlib-config --version
```

## Using zlib in C programs

To compile against zlib, add the `-lz` flag to your gcc or clang command.

### Basic in-memory compression

Here’s a minimal example that compresses a string:

``` c
#include <stdio.h>
#include <string.h>
#include <zlib.h>

int main() {
    const char *input = "Hello, zlib compression!";
    uLong src_len = strlen(input) + 1;
    uLong dest_len = compressBound(src_len);
    Bytef dest[dest_len];

    if (compress(dest, &dest_len, (const Bytef *)input, src_len) == Z_OK) {
        printf("Compressed %lu bytes to %lu bytes\n", src_len, dest_len);
    } else {
        fprintf(stderr, "Compression failed\n");
        return 1;
    }
    return 0;
}
```

Compile and run:

``` bash
gcc -o compress_test compress_test.c -lz
./compress_test
```

For custom prefixes, pass include and library paths explicitly:

``` bash
gcc -o compress_test compress_test.c -I/opt/zlib/include -L/opt/zlib/lib -lz
```

The cleaner approach uses pkg-config to avoid hardcoding paths:

``` bash
gcc -o compress_test compress_test.c $(pkg-config --cflags --libs zlib)
```

If zlib was installed to a custom prefix, ensure pkg-config can locate it:

``` bash
export PKG_CONFIG_PATH=/opt/zlib/lib/pkgconfig:$PKG_CONFIG_PATH
pkg-config --cflags --libs zlib
```

### Streaming compression

For processing large files or network data, zlib supports streaming compression in chunks:

``` c
#include <stdio.h>
#include <zlib.h>
#include <string.h>

int main() {
    z_stream stream = {0};
    unsigned char input[256] = "Some data to compress...";
    unsigned char output[256];

    deflateInit(&stream, Z_DEFAULT_COMPRESSION);

    stream.avail_in = strlen((const char *)input);
    stream.next_in = input;
    stream.avail_out = sizeof(output);
    stream.next_out = output;

    deflate(&stream, Z_FINISH);
    deflateEnd(&stream);

    printf("Compressed %u bytes to %u bytes\n",
           (unsigned int)strlen((const char *)input),
           (unsigned int)(sizeof(output) - stream.avail_out));

    return 0;
}
```

Compile the same way:

``` bash
gcc -o stream_test stream_test.c -lz
```

### Streaming decompression

For decompression, use the inflate API:

``` c
#include <stdio.h>
#include <zlib.h>

int main() {
    z_stream stream = {0};
    unsigned char compressed[256];
    unsigned char output[512];

    // Assume compressed data is populated
    inflateInit(&stream);

    stream.avail_in = 10;  // actual compressed size
    stream.next_in = compressed;
    stream.avail_out = sizeof(output);
    stream.next_out = output;

    int result = inflate(&stream, Z_FINISH);
    if (result != Z_STREAM_END) {
        fprintf(stderr, "Decompression failed with code %d\n", result);
        inflateEnd(&stream);
        return 1;
    }

    printf("Decompressed to %lu bytes\n", 
           (unsigned long)(sizeof(output) - stream.avail_out));

    inflateEnd(&stream);
    return 0;
}
```

## Troubleshooting

### error: zlib.h: No such file or directory

The compiler cannot find the header. Verify the installation:

``` bash
ls /usr/local/include/zlib.h
```

If the file is missing, the build failed. Re-run `make install` with `sudo`. If the header exists in a custom prefix, pass `-I`:

``` bash
gcc -I/opt/zlib/include -o program program.c -L/opt/zlib/lib -lz
```

### cannot find -lz

The linker cannot locate the library. Verify it exists:

``` bash
ls /usr/local/lib/libz.so
```

Run `sudo ldconfig` to update the linker cache. If using a custom prefix, either pass `-L` explicitly or use pkg-config:

``` bash
gcc -o program program.c $(pkg-config --cflags --libs zlib)
```

### Permission denied during make install

You’re attempting to install to a system directory without root privileges. Either use `sudo`, or reconfigure with a user-owned prefix:

``` bash
./configure --prefix=$HOME/.local
make
make install
```

### Conflicts with system zlib

If both system zlib and a custom build are installed, they typically coexist without issues — the dynamic linker prioritizes `/usr/local/lib` over `/usr/lib` by default. To verify which library your program uses:

``` bash
ldd ./program | grep libz
```

For detailed linker diagnostics:

``` bash
LD_DEBUG=libs ./program 2>&1 | grep libz
```

If you need strict version control, use separate prefixes and manage `LD_LIBRARY_PATH` or `PKG_CONFIG_PATH` carefully per project.
