---
title: "papersize(5)"
name: "papersize"
section: "5"
letter: "p"
url: "/docs/linux/man/5-papersize/"
description: "papersize – specify preferred paper size"
---

<p><code>papersize</code> &#8211; specify preferred paper size</p>
<h2>Synopsys</h2>
<p><code>/etc/papersize</code></p>
<h2>Description</h2>
<p>The <code>papersize</code> file is used to specify the preferred paper size to use by available commands and programs generating documents. </p>
<p> The format of this file is extremely simple: whitespace and anything starting with `#&#8217; is ignored, and the name of the paper is the first string found; the case in the name of the paper does not import (see <code>CAVEATS</code> section however).</p>
<h2>Paper Names</h2>
<p>The following names are commonly understood by programs: <code>a3</code>,<code> a4</code>,<code> a5</code>, <code>b5</code>,<code> letter</code>,<code> legal</code>,<code> executive</code>,<code> note</code> and <code>11&#215;17</code>. </p>
<p> Additional paper names that one may encounter are: <code>a0</code>,<code> a1</code>,<code> a2</code>,<code> a6</code>,<code> a7</code>,<code> a8</code>,<code> a9</code>,<code> a10</code>, <code>b0</code>,<code> b1</code>,<code> b2</code>,<code> b3</code>,<code> b4</code>,<code> tabloid</code>, <code>statement</code>,<code> note</code>, <code>halfletter</code>,<code> halfexecutive</code>,<code> folio</code>,<code> quarto</code>,<code> ledger</code>, <code>archA</code>,<code> archB</code>,<code> archC</code>,<code> archD</code>,<code> archE</code>,<code> flsa</code>, <code>flse</code>,<code> csheet</code>,<code> dsheet</code>,<code> esheet</code> and <code>10&#215;14</code>. </p>
<p> The value of the <code>papersize</code> file can be overrideen by looking in order at the <code>PAPERSIZE</code> environment variable, then at the contents of the file specified by the <code>PAPERCONF</code> environment variable. If the <code>papersize</code> file does not exist, programs using the paper library default to using <code>letter</code> as a fall-back value</p>
<h2>Caveats</h2>
<p>This manual page documents the format of the <code>papersize</code> file that is read by the <code>libpaper</code> library. Some programs that read this file do not yet use the library and may have trouble ignoring whitespace and comments in the file; they may also require that the paper names use a specific capitalization.</p>
<h2>Documentation</h2>
<p>Yves Arrouye &lt;arrouye [at] debian.org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-paperconf/">paperconf</a></code>(1)<br />
 <code><a href="/docs/linux/man/8-paperconfig/">paperconfig</a></code>(8) </p>
