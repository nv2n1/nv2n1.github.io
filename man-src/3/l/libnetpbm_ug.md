---
title: "libnetpbm_ug(3)"
name: "libnetpbm_ug"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libnetpbm_ug/"
description: "libnetpbm_ug – netpbm sample code"
---

<h2 class="name">NAME</h2>
<p> libnetpbm_ug &#8211; netpbm sample code</p>
<h2>DESCRIPTION</h2>
<p> The Libnetpbm programming library is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<h2>Example</h2>
<p> Here is an example of a C program that uses <code>libnetpbm</code> to read a Netpbm image input and produce a Netpbm image output. </p>
<pre><code>
/* Example program fragment to read a PAM or PNM image
   from stdin, add up the values of every sample in it
   (I don't know why), and write the image unchanged to
   stdout. */
#include &lt;netpbm/pam.h&gt;
struct pam inpam, outpam;
tuple *tuplerow;
unsigned int row;
pm_init(argv[0], 0);
pnm_readpaminit(stdin, &amp;inpam, PAM_STRUCT_SIZE(tuple_type));
outpam = inpam;
outpam.file = stdout;
pnm_writepaminit(&amp;outpam);
tuplerow = pnm_allocpamrow(&amp;inpam);
for (row = 0; row &lt; inpam.height; row++) {
    unsigned int column;
    pnm_readpamrow(&amp;inpam, tuplerow);
    for (column = 0; column &lt; inpam.width; ++column) {
        unsigned int plane;
        for (plane = 0; plane &lt; inpam.depth; ++plane) {
            grand_total += tuplerow[column][plane];
        }
    }
    pnm_writepamrow(&amp;outpam, tuplerow);
}
pnm_freepamrow(tuplerow);
</code></pre>
<h2>Guide To Using Libnetpbm</h2>
<h3><code>libnetpbm classes</code></h3>
<p> In this section, Guide To Using Libnetpbm, we cover only the PAM functions in <code>libnetpbm</code>. As described in <code>the</code> introduction to <code>libnetpbm</code> (1) , there are four other classes of image processing functions (PBM, PGM, PPM, PNM). They are less important, since you can do everything more easily with the PAM functions, but if you&#8217;re working on old programs or need the extra efficiency those older functions can sometimes provide, you can find them documented as here: <code>PBM</code>Function<code><a href="/docs/linux/man/1-manual/">Manual</a></code>(1) , <code>PGM</code>Function<code><a href="/docs/linux/man/1-manual/">Manual</a></code>(1) , <code>PPM</code>Function<code><a href="/docs/linux/man/1-manual/">Manual</a></code>(1) , and <code>PNM</code>Function<code><a href="/docs/linux/man/1-manual/">Manual</a></code>(1) </p>
<p> In case you&#8217;re wondering, what makes the PAM functions easier to use is: </p>
<dl>
<dt>&bull;</p>
<dd> Each function handles all the formats. It does so without converting to a common format, so your program can treat the different formats differently if it wants. However, the interface makes it easy for your program to ignore the differences between the formats if that&#8217;s what you want. </p>
<dt>&bull;</p>
<dd> The PAM function parameter lists convey most information about the image with which you&#8217;re working with a single <code>pam</code> structure, which you can build once and use over and over, whereas the older functions require you to pass up to 5 pieces of image information (height, width, etc.) as separate arguments to every function. </p>
</dl>
<h3>Library Initialization</h3>
<p> Every program that uses the library must initialize the library, i.e. set up the process to use the library, as described in Initialization . That is the purpose of the call to <code>pm_init()</code> in the example above. </p>
<h3>THE pam STRUCTURE</h3>
<p> The PAM functions take most of their arguments in the form of a single <code>pam</code> structure. This is not an opaque object, but just a convenient way to organize the information upon which most the functions depend. So you are free to access or set the elements of the structure however you want. But you will find in most cases it is most convenient to call <code>pnm_readpaminit()</code> or <code>pnm_writepaminit()</code> to set the fields in the <code>pam</code> structure before calling any other pam functions, and then just to pass the structure unchanged in all future calls to pam functions. </p>
<p> The fields are: </p>
<dl>
<dt><code>size</code></p>
<dd> The storage size in bytes of this entire structure. </p>
<dt><code>len</code></p>
<dd> The length, in bytes, of the information in this structure. The information starts in the first byte and is contiguous. This cannot be greater than <code>size</code>. <code>size</code> and <code>len</code> can be used to make programs compatible with newer and older versions of the Netpbm libraries. </p>
<dt><code>file</code></p>
<dd> The file. </p>
<dt><code>format</code></p>
<dd> The format code of the image. This is <code>PAM_FORMAT</code> unless the PAM image is really a view of a PBM, PGM, or PPM image. Then it&#8217;s <code>PBM_FORMAT</code>, <code>RPBM_FORMAT</code>, etc. </p>
<p> There is an important quirk in the meaning of this member when you use the pam structure to write an image: Only the type portion of it is meaningful. A Netpbm format code conveys two pieces of information: The format type (PBM, PGM, PPM, or PAM) and the plainness (plain PBM vs raw PBM, etc.). But when writing, <code>libnetpbm</code> ignores the plainness part and instead takes the plainness from the <code>plainformat</code> member. So <code>PBM_FORMAT</code> and <code>RPBM_FORMAT</code> are identical when writing. </p>
<p> This quirk exists for historical purposes; it&#8217;s necessary for consistency with the older functions such as <code>pnm_writepnmrow()</code> whose <i>format</i> and <i>forceplain</i> arguments are analogous. </p>
<p> Before Netpbm 10.32 (February 2006), <code>libnetpbm</code> did not ignore the plainness. This caused many programs to behave poorly, producing plain format output when they should, for backward compatibility at the very least, produce raw format output. </p>
<p> A common way to use this member is to copy it and the <code>plainformat</code> member from a pam for an input image to a pam for an output image. When you do that, your output image will be raw format regardless of whether your input image was plain or raw, and this is the conventional behavior of Netpbm programs. </p>
<dt><code>plainformat</code></p>
<dd> This is a boolean value (0 = false, 1 = true), meaningful only when writing an image file. It means to write in the plain (text) version of the format indicated by <code>format</code> as opposed to the raw (binary) version. Note that the format code in <code>format</code> would appear to completely specify the format, making <code>plainformat</code> redundant. But see the description of <code>format</code> for why that isn&#8217;t true. </p>
<p> Until Netpbm 10.32 (February 2006), this was defined a little differently. The <code>format</code> member did in fact completely identify the format and <code>plainformat</code> was redundant and existed as a separate member only for computational speed. But this was inconsistent with the older <code>libnetpbm</code> interface (e.g. <code>pnm_writepnm()</code>, and it made it difficult to write backward compatible programs. Before Netpbm 10.32, it affected reading as well as writing. </p>
<p> <code>libnetpbm</code> image reading functions set this field to false, for your convenience in building an output image pam from an input image pam. </p>
<dt><code>height</code></p>
<dd> The height of the image in rows. </p>
<dt><code>width</code></p>
<dd> The width of the image in number of columns (tuples per row). </p>
<dt><code>depth</code></p>
<dd> The depth of the image (degree of or number of samples in each tuple). </p>
<dt><code>maxval</code></p>
<dd> The maxval of the image. See definitions in <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<dt><code>bytes_per_sample</code></p>
<dd> The number of bytes used to represent each sample in the image file. See the format definition in <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) is entirely redundant with <code>maxval</code>. It exists as a separate member for computational speed. </p>
<dt><code>tuple_type</code></p>
<dd> The tuple type of the image. See definitions in <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) except the following, which are used for a PAM image which is really a view of a PBM, PGM, or PPM image: <code>PAM_PBM_TUPLETYPE</code>, <code>PAM_PGM_TUPLETYPE</code>, <code>PAM_PPM_TUPLETYPE</code>. </p>
<dt><code>allocation_depth</code></p>
<dd> The number of samples for which memory is allocated for any tuple associated with this PAM structure. This must be at least as great as &#8216;depth&#8217;. Only the first &#8216;depth&#8217; of the samples of a tuple are meaningful. </p>
<p> The purpose of this is to make it possible for a program to change the type of a tuple to one with more or fewer planes. </p>
<p> 0 means the allocation depth is the same as the image depth. </p>
<dt><code>comment_p</code></p>
<dd> Pointer to a pointer to a NUL-terminated ASCII string of comments. When reading an image, this contains the comments from the image&#8217;s PAM header; when writing, the image gets these as comments, right after the magic number line. The individual comments are delimited by newlines and are in the same order as in the PAM header. The &#8216;#&#8217; at the beginning of a PAM header line that indicates the line is a comment is not part of the comment. </p>
<p> On output, NULL means no comments. </p>
<p> On input, libnetpbm mallocs storage for the comments and placed the pointer at *comment_p. Caller must free it. NULL means libnetpbm does not return comments and does not allocate any storage. </p>
<p> Examples: </p>
<p>const char *comments;<br />
&#8230; pam.comment_p = &amp;comments;<br />
pnm_readpaminit(fileP, &amp;pam, PAM_STRUCT_SIZE(comment_p));<br />
printf(&#8216;The comments are:
&#8217;);<br />
printf(&#8216;%s&#8217;, comments)<br />
    free(comments);</p>
<pre><code>

const char *comments;
... comments = strdup('This is a comment 1
This is comment 2
');
pam.comment_p = &amp;comments;
pnm_writepaminit(&amp;pam);
free(comments);
</code></pre>
<p> This works only for PAM images. If you read a PNM image, you always get back a null string. If you write a PNM image, you always get an image that contains no comments. </p>
<p> This member does not exist before Netpbm 10.35 (August 2006). Before that, there is no way with libnetpbm to get or set comments. The macro <code>PAM_HAVE_COMMENT_P</code> is defined in <code>pam.h</code> where the member exists. </p>
</dl>
<h3>PLAIN VERSUS RAW FORMAT</h3>
<p> The PNM formats each come in two varieties: the older plain (text) format and the newer raw (binary) format. There are different format codes for the plain and raw formats, but which of the two formats the pnm and pam functions write is independent of the format code you pass to them. </p>
<p> The pam functions always write raw formats. If you specify the format code for a plain format, a pam function assumes instead the raw version of that format. </p>
<p> The pnm functions choose between plain and raw based on the <i>forceplain</i> parameter that every write-type pnm function has. If this boolean value is true, the function writes the plain version of the format specified by the format code. If it is false, the function writes the raw version of the format specified by the format code. </p>
<p> We are trying to stamp out the older plain formats, so it would be a wise choice not to write a program that sets <i>forceplain</i> true under any circumstance. A user who needs a plain format can use the <code>pnmtoplainpnm</code> program to convert the output of your program to plain format. </p>
<h3>Reference</h3>
<p> The <code>Libnetpbm</code>Netpbm<code>Image</code> Processing Manual (1)<br />
&nbsp;<wbr>describes the the&nbsp;<wbr><code>libnetpbm</code>&nbsp;<wbr>functions for processing image data. </p>
<p> The <code>Libnetpbm</code>Utility<code><a href="/docs/linux/man/1-manual/">Manual</a></code>(1) </p>
<p> describes the functions that are not specifically related to the Netpbm image formats. </p>
<h2>Index</h2>
</dl>
