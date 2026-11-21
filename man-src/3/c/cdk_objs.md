---

title: "cdk_objs(3)"
name: "cdk_objs"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_objs/"
description: "cdk_objs – Cdk object-support functions"
---

<h2>NAME</h2>
<p> cdk_objs &#8211; Cdk object-support functions</p>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<pre><code>
void cleanCdkTitle(
    CDKOBJS *obj);
void drawCdkTitle(
    WINDOW *window,
    CDKOBJS *object);
void positionCDKObject(
    CDKOBJS *object,
    WINDOW *win);
void setCDKObjectBackgroundColor(
    CDKOBJS *object,
    const 3char * color);
void setCDKObjectPostProcess(
    CDKOBJS *object,
    PROCESSFN func,
    void *data);
void setCDKObjectPreProcess(
    CDKOBJS *object,
    PROCESSFN func,
    void *data);
void setCdkExitType(
    CDKOBJS *obj,
    EExitType *type,
    chtyp ch);
int setCdkTitle(
    CDKOBJS *obj,
    const char *title,
    int boxWidth);
bool validCDKObject(
    CDKOBJS *obj);
</code></pre>
</dl>
<p> Cdk is written in ANSI C, which has &quot;no&quot; object support. Most of the object support in Cdk is done using macros and a small number of types which hold object information:</p>
<dl>
<dl>
<dt>CDKFUNCS</dt>
<dd> contains the function pointers for common methods of the widgets. It is separate from CDKOBJS because it is compiled into each widget&#8217;s C code (see the DeclareCDKObjects() and DeclareSetXXchar() macros. The widget instances point to a single copy of CDKFUNCS for each widget.</dd>
<dt>CDKOBJS</dt>
<dd> Holds data common to all objects (widget instances). It appears first in each widget&#8217;s struct to allow Cdk to use generic functions in binding.c, cdkscreen.c, position.c, etc.</dd></dl>
</dl>
<h2>AVAILABLE FUNCTIONS</h2>
<p> The functions declared in &lt;cdk/cdk_objs.h&gt; are used in situations where the expressions are too complex for a macro.</p>
<dl>
<dt><code>cleanCdkTitle</code></dt>
<dd> Remove storage for the widget&#8217;s title.</dd>
<dt><code>drawCdkTitle,</code></dt>
<dd> Draw the widget&#8217;s title.</dd>
<dt><code>positionCDKObject</code></dt>
<dd> This allows the user to use the cursor keys to adjust the position of the widget.</dd>
<dt><code>setCDKObjectBackgroundColor</code></dt>
<dd> Set the background color of the widget.</dd>
<dt><code>setCDKObjectPostProcess</code></dt>
<dd> Set data for postprocessing.</dd>
<dt><code>setCDKObjectPreProcess</code></dt>
<dd> Set data for preprocessing.</dd>
<dt><code>setCdkExitType</code></dt>
<dd> Set the object&#8217;s exit-type based on the input. The <code>.exitType</code> field should have been part of the CDKOBJS struct, but it is used too pervasively in Cdk4 applications to move.</dd>
<dt><code>setCdkTitle</code></dt>
<dd> Set the widget&#8217;s title.</dd>
<dt><code>validCDKObject </code></dt>
<dd> Returns true if a &quot;new&quot; was done on the object but no &quot;destroy&quot;.</dd></dl>
<h2>SEE ALSO</h2>
<p> cdk_binding (3) cdk_process (3) </p>
