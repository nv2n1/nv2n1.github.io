---
title: "star(5)"
name: "star"
section: "5"
letter: "s"
url: "/docs/linux/man/5-star/"
description: "star – tape archive file format"
---

<p>star &#8211; tape archive file format</p>
<h2>Description</h2>
<p><code>Tar</code> Archives are layered archives. The basic structure is defined by the POSIX.1-1988 archive format and documented in the <code>BASIC TAR HEADER DESCRIPTION</code> section below. The higher level structure is defined by the POSIX.1-2001 extended headers and documented in the <code>EXTENDED TAR (PAX) HEADER STRUCTURE</code> section below. POSIX.1-2001 extended headers are pseudo files that contain an unlimited number of extended header keywords and associated values. The header keywords are documented in the <code>EXTENDED TAR (PAX) HEADER KEYWORDS</code> section below.</p>
<h2>Basic Tar Header Description</h2>
<p>Physically, a POSIX.1-1988 <code>tar</code> archive consists of a series of fixed sized blocks of TBLOCK (512) characters. It contains a series of file entries terminated by a logical end-of-archive marker, which consists of two blocks of 512 bytes of binary zeroes. Each file entry is represented by a header block that describes the file followed by one or more blocks with the content of the file. The length of each file is rounded up to a multiple of 512 bytes. </p>
<p> A number of TBLOCK sizes blocks are grouped together to a tape record for physical I/O operations. Each record of <i>n</i> blocks is written with a single <code><a href="/docs/linux/man/2-write/">write</a></code>(2) operation. On magnetic tapes, this results in a single tape record in case the tape drive is in <code>variable length record mode</code>. </p>
<p> The header block is defined in star.h as follows: </p>
<pre>/*
 * POSIX.1-1988 field size values and magic.
 */
#define TBLOCK 512
#define NAMSIZ 100
#define PFXSIZ 155
#define TMODLEN 8
#define TUIDLEN 8
#define TGIDLEN 8
#define TSIZLEN 12
#define TMTMLEN 12
#define TCKSLEN 8
#define TMAGIC &quot;ustar&quot; /* ustar magic 6 chars + '
