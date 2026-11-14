---
title: "cdk_misc(3)"
name: "cdk_misc"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_misc/"
description: "cdk_misc – Curses Development Kit Miscellaneous Routines"
---

<h2>NAME</h2>
<p> cdk_misc &#8211; <code>Curses Development Kit</code> Miscellaneous Routines </p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>

void Beep(void);
unsigned CDKallocStrings(
    char ***list /,
    char *item /,
    unsigned length /,
    unsigned used /);
unsigned CDKcountStrings(
    CDK_CONST char **list);
void CDKfreeChtypes(
    chtype **list);
void CDKfreeStrings(
    char **list);
char **CDKsplitString(
    const char *string,
    int splitChar);
char *baseName(
    char *string);
int ceilCDK(
    doublevalue);
int chlen(
    const chtype *string);
void chstrncpy(
    char *dest,
    const chtype *src,
    int maxcount);
char *chtype2Char(
    const chtype *string);
void cleanChar(
    char *string,
    int length,
    char character);
void cleanChtype(
    chtype *string,
    int length,
    chtype character);
int cmpStrChstr(
    const char *str,
    const chtype *chstr);
char *copyChar(
    const char *string);
char **copyCharList(
    const char **list);
chtype *copyChtype(
    const chtype *string);
chtype **copyChtypeList(
    const chtype **list);
char *dirName(
    char *filename);
int floorCDK(
    double value);
void freeChar(
    char *string);
void freeCharList(
    char **list,
    unsigned size);
void freeChtype(
    chtype *string);
void freeChtypeList(
    chtype **list,
    unsigned size);
int intlen(
    int value);
int lenCharList(
    const char **list);
int lenChtypeList(
    const chtype **list);
int mode2Char(
    char *string,
    mode_t fileMode);
int searchList(
    CDK_CONST char *CDK_CONST *list,
    int listSize,
    const char *pattern);
void sortList(
    CDK_CONST char **list,
    int length);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> These are miscellaneous functions which may be useful with the Cdk widget set.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>Beep</code></p>
<dd> makes an audible beep. The standard curses beep() does not flush the stream, so it will only beep until a force is made. This forces a flush after issuing the beep command.</p>
<dt><code>CDKallocStrings</code></p>
<dd> Add a new string <i>item</i> to a <i>list</i>. Keep a null pointer on the end so one may use <code>CDKfreeStrings()</code> to deallocate the whole list. The caller is responsible for updating the <i>length</i> of the list. The return value is the updated number of chars <i>used</i>.</p>
<dt><code>CDKcountStrings</code></p>
<dd> Count the number of items in a null-terminated <i>list</i> of character strings. Return the count.</p>
<dt><code>CDKfreeChtypes</code></p>
<dd> Free a <i>list</i> of chtype-strings which is terminated by a null pointer.</p>
<dt><code>CDKfreeStrings</code></p>
<dd> Free a <i>list</i> of character strings which is terminated by a null pointer. Also free <i>list</i> itself.</p>
<dt><code>CDKsplitString</code></p>
<dd> split the <i>string</i> at each occurrence of <i>separator</i>, returning a pointer to a dynamically allocated array of the pieces. The original <i>string</i> is unmodified. The caller is responsible for freeing the result.</p>
<dt><code>baseName</code></p>
<dd> returns a pointer to the first character of the filename in the given pathname. The result should be freed by the caller.</p>
<dt><code>ceilCDK</code></p>
<dd> Return an integer like the math library <code>ceil()</code>, which returns a double.</p>
<dt><code>chlen</code></p>
<dd> returns the length of the (null-terminated) <i>string</i> of chtype&#8217;s.</p>
<dt><code>chstrncpy</code></p>
<dd> Extract the characters from a null-terminated array of chtype&#8217;s <i>src</i>. The size of the destination <i>dest</i> is given in <i>maxcount</i>.</p>
<dt><code>chtype2Char</code></p>
<dd> Extract the characters from a null-terminated array of chtype&#8217;s <i>string</i>. A dynamically allocated string is returned. The caller is responsible for freeing the result.</p>
<dt><code>cleanChar</code></p>
<dd> is analogous to <i>memset</i>. Set the characters in <i>string</i> to the given <i>character</i>. The length of <i>string</i> is given by <i>length</i>. character which will be written.</p>
<dt><code>cleanChtype</code></p>
<dd> is analogous to <i>memset</i>. Set the chtype&#8217;s in <i>string</i> to the given <i>character</i>. The length of <i>string</i> is given by <i>length</i>.</p>
<dt><code>cmpStrChstr</code></p>
<dd> Compare a char string <i>str</i> to a chtype string <i>chstr</i>. Return -1, 0 or 1 according to whether <i>str</i> is less than, equal to to greater than <i>chstr</i>.</p>
<dt><code>copyChar</code></p>
<dd> copies the string passed in. Unlike <i>strdup</i> this checks to see if the string is NULL before copying.</p>
<dt><code>copyCharList</code></p>
<dd> copies the given list.</p>
<dt><code>copyChtype</code></p>
<dd> function copies the string passed in, analogous to <code>copyChar</code>, but for chtype strings.</p>
<dt><code>copyChtypeList</code></p>
<dd> copies the given list.</p>
<dt><code>dirName</code></p>
<dd> Returns the directory for the given <i>filename</i>, i.e., the part before the * last slash. The return value should be freed by the caller.</p>
<dt><code>floorCDK</code></p>
<dd> Return an integer like the math function floor(), which returns a double.</p>
<dt><code>freeChar</code></p>
<dd> is a wrapper for <i>free</i>. It checks to see if the string is NULL before trying to free the string.</p>
<dt><code>freeCharList</code></p>
<dd> Free the memory used by the given <i>list</i> of strings. The number of strings to free is given by <i>size</i>.</p>
<dt><code>freeChtype</code></p>
<dd> is a wrapper for <i>free</i>, like <i>freeChar</i>.</p>
<dt><code>freeChtypeList</code></p>
<dd> Free the memory used by the given <i>list</i> of chtype strings. The number of strings to free is given by <i>size</i>.</p>
<dt><code>intlen</code></p>
<dd> returns the length of an integer, i.e., the number of characters needed to represent it.</p>
<dt><code>lenCharList</code></p>
<dd> returns the length of the given list.</p>
<dt><code>lenChtypeList</code></p>
<dd> returns the length of the given list.</p>
<dt><code>mode2Char</code></p>
<dd> Given a file protection mode <i>fileMode</i>, store a printable version of the permissions in <i>string</i>, formatted as if by &quot;ls -l&quot;). Return the corresponding permissions data, i.e., ignoring the file-type bits.</p>
<dt><code>searchList</code></p>
<dd> Search the given <i>list</i> of <i>listSize</i> strings for a subset of a word <i>pattern</i> in the given list. Return the index in the list if it is found, or -1 if not found.</p>
<dt><code>sortList</code></p>
<dd> performs a quick sort of the given list. This is a wrapper for qsort, used to sort the <i>list</i> of strings. The number of strings in <i>list</i> is given by <i>length</i>. The list is sorted alphabetically in increasing order.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_util/">cdk_util</a></code>(3) </p>
<h2>Index</h2>
