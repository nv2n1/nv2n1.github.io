---
title: "pcre16_pattern_to_host_byte_order(3)"
name: "pcre16_pattern_to_host_byte_order"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre16_pattern_to_host_byte_order/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre.h&gt;
int pcre_pattern_to_host_byte_order(pcre *code,
                                    pcre_extra *extra, const unsigned char *tables);

int pcre16_pattern_to_host_byte_order(pcre16 *code,
                                      pcre16_extra *extra, const unsigned char *tables);

int pcre32_pattern_to_host_byte_order(pcre32 *code,
                                      pcre32_extra *extra, const unsigned char *tables);</code></pre>
<h2>Description</h2>
<p>This function ensures that the bytes in 2-byte and 4-byte values in a compiled pattern are in the correct order for the current host. It is useful when a pattern that has been compiled on one host is transferred to another that might have different endianness. The arguments are:<br />
&nbsp;<wbr>&nbsp;<i>code</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;A compiled regular expression<br />
&nbsp;<wbr>&nbsp;<i>extra</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Points to an associated&nbsp;<code>pcre[16|32]_extra</code>&nbsp;structure,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;or is NULL<br />
&nbsp;<wbr>&nbsp;<i>tables</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pointer to character tables, or NULL to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;set the built-in default The result is 0 for success, a negative PCRE_ERROR_xxx value otherwise. There is a complete description of the PCRE native API in the <code>pcreapi</code> page and a description of the POSIX API in the <code>pcreposix</code> page. </p>
