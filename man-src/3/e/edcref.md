---
title: "edcref(3)"
name: "edcref"
section: "3"
letter: "e"
url: "/docs/linux/man/3-edcref/"
description: "edcref – Edje Data Collection reference An Edje Data Collection, it’s a plain text file (normally identified with the .edc extension),consisting of instructions for the Edje Compiler."
---

<h2 class="name">NAME</h2>
<p> edcref &#8211; Edje Data Collection reference An Edje Data Collection, it&#8217;s a plain text file (normally identified with the .edc extension),consisting of instructions for the Edje Compiler. </p>
<p> The syntax for the edje data collection files follows a simple structure of &#8216;blocks { .. }&#8217; that can contain &#8216;properties: ..&#8217;, more blocks, or both. </p>
<p> <code>Author:</code></p>
<dl>
<dt>
<dd> Andres Blanc (dresb) andresblanc [at] gmail.com</dl>
<p> <code> images </code> </p>
<pre><code>
images
{
image:
    'filename1.ext' COMP;
image:
    'filename2.ext' LOSSY 99;
    ..
}
</code></pre>
<p>&nbsp;<wbr>The&nbsp;<wbr>&#8216;images&#8217;&nbsp;<wbr>block is used to list each image file that will be used in the theme along with its compression method&nbsp;<wbr>(if any). Besides the domcument&#8217;s root, additional&nbsp;<wbr>&#8216;images&#8217;&nbsp;<wbr>blocks can be included inside other blocks, normally&nbsp;<wbr>&#8216;collections&#8217;,&nbsp;<wbr>&#8216;group&#8217;&nbsp;<wbr>and&nbsp;<wbr>&#8216;part&#8217;, easing mantienance of the file list when the theme is split among multiple files.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>image&nbsp;<wbr>&nbsp;<wbr>[image file]&nbsp;<wbr>[compression method]&nbsp;<wbr>(compression level)&nbsp;<wbr>&nbsp;<wbr>Used to include each image file. The full path to the directory holding the images can be defined later with edje_cc&#8217;s&nbsp;<wbr>&#8216;-id&#8217;&nbsp;<wbr>option. Compression methods:&nbsp;<wbr> </p>
<dl>
<dt>*</p>
<dd> RAW: Uncompressed.</p>
<dt>*</p>
<dd> COMP: Lossless compression.</p>
<dt>*</p>
<dd> LOSSY [0-100]: Lossy comression with quality from 0 to 100.</dl>
<p> <code> fonts </code> </p>
<p>fonts<br />
{<br />
font:<br />
    &#8216;filename1.ext&#8217; &#8216;fontname&#8217;;<br />
font:<br />
    &#8216;filename2.ext&#8217; &#8216;otherfontname&#8217;;<br />
    ..<br />
}</p>
<p>&nbsp;<wbr>The&nbsp;<wbr>&#8216;fonts&#8217;&nbsp;<wbr>block is used to list each font file with an alias used later in the theme. As with the&nbsp;<wbr>&#8216;images&#8217;&nbsp;<wbr>block, additional&nbsp;<wbr>&#8216;fonts&#8217;&nbsp;<wbr>blocks can be included inside other blocks.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>font&nbsp;<wbr>&nbsp;<wbr>[font filename]&nbsp;<wbr>[font alias]&nbsp;<wbr>&nbsp;<wbr>Defines each font&nbsp;<wbr>&#8216;file&#8217;&nbsp;<wbr>and&nbsp;<wbr>&#8216;alias&#8217;, the full path to the directory holding the font files can be defined with edje_cc&#8217;s&nbsp;<wbr>&#8216;-fd&#8217;&nbsp;<wbr>option.&nbsp;<wbr> </p>
<p> <code> data </code> </p>
<p>data<br />
{<br />
item:<br />
    &#8216;arbitraryname&#8217; &#8216;arbitraryvalue&#8217;;<br />
item:<br />
    &#8216;othername&#8217; &#8216;othervalue&#8217;;<br />
    ..<br />
}</p>
<p>&nbsp;<wbr>The&nbsp;<wbr>&#8216;data&#8217;&nbsp;<wbr>block is used to pass arbitrary parameters from the theme to the application. Unlike the&nbsp;<wbr>&#8216;images&#8217;&nbsp;<wbr>and&nbsp;<wbr>&#8216;fonts&#8217;&nbsp;<wbr>blocks, additional&nbsp;<wbr>&#8216;data&#8217;&nbsp;<wbr>blocks can only be included inside the&nbsp;<wbr>&#8216;group&#8217;&nbsp;<wbr>block.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>item&nbsp;<wbr>&nbsp;<wbr>[parameter name]&nbsp;<wbr>[parameter value]&nbsp;<wbr>&nbsp;<wbr>Defines each additional parameter.&nbsp;<wbr> </p>
<p> <code> data </code> </p>
<p>data<br />
{<br />
file:<br />
    &#8216;arbitraryname&#8217; &#8216;filename&#8217;;<br />
file:<br />
    &#8216;othername&#8217; &#8216;otherfilename&#8217;;<br />
    ..<br />
}</p>
<p>&nbsp;<wbr>The&nbsp;<wbr>&#8216;data&#8217;&nbsp;<wbr>block is used to pass arbitrary parameters from the theme to the application. Unlike the&nbsp;<wbr>&#8216;images&#8217;&nbsp;<wbr>and&nbsp;<wbr>&#8216;fonts&#8217;&nbsp;<wbr>blocks, additional&nbsp;<wbr>&#8216;data&#8217;&nbsp;<wbr>blocks can only be included inside the&nbsp;<wbr>&#8216;group&#8217;&nbsp;<wbr>block.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>file&nbsp;<wbr>&nbsp;<wbr>[parameter name]&nbsp;<wbr>[parameter filename]&nbsp;<wbr>&nbsp;<wbr>Defines each additional parameter.&nbsp;<wbr> </p>
<p> <code> color_classes </code> </p>
<p>color_classes<br />
{<br />
    color_class<br />
    {<br />
    name:<br />
        &#8216;colorclassname&#8217;;<br />
    color:<br />
        [0 &#8211; 255][0 &#8211; 255][0 &#8211; 255][0 &#8211; 255];<br />
    color2:<br />
        [0 &#8211; 255][0 &#8211; 255][0 &#8211; 255][0 &#8211; 255];<br />
    color3:<br />
        [0 &#8211; 255][0 &#8211; 255][0 &#8211; 255][0 &#8211; 255]<br />
    }<br />
    ..<br />
}</p>
<p>&nbsp;<wbr>The&nbsp;<wbr>&#8216;color_classes&#8217;&nbsp;<wbr>block contains a list of one or more&nbsp;<wbr>&#8216;color_class&#8217;&nbsp;<wbr>blocks. Each&nbsp;<wbr>&#8216;color_class&#8217;&nbsp;<wbr>allows the designer to name an arbitrary group of colors to be used in the theme, the application can use that name to alter the color values at runtime.&nbsp;<wbr> </p>
<p>&nbsp;<wbr> </p>
<p> name [color class name] Sets the name for the color class, used as reference by both the theme and the application. </p>
<p>&nbsp;<wbr> </p>
<p> color [red] [green] [blue] [alpha] The main color. </p>
<p>&nbsp;<wbr> </p>
<p> color2 [red] [green] [blue] [alpha] Used as shadow in text and textblock parts. </p>
<p>&nbsp;<wbr> </p>
<p> color3 [red] [green] [blue] [alpha] Used as outline in text and textblock parts. </p>
<p> <code> spectra </code> </p>
<p>spectra<br />
{<br />
    spectrum<br />
    {<br />
    name:<br />
        &#8216;colorspectrumname&#8217;;<br />
    color: [0-255] [0-255] [0-255] [0-255] [0-?]<br />
                color: [0-255] [0-255] [0-255] [0-255] [0-?]<br />
                ..<br />
    }<br />
    ..<br />
}</p>
<p>&nbsp;<wbr>The&nbsp;<wbr>&#8216;spectra&#8217;&nbsp;<wbr>block contains a list of one or more&nbsp;<wbr>&#8216;spectrum&#8217;&nbsp;<wbr>blocks. Each&nbsp;<wbr>&#8216;spectrum&#8217;&nbsp;<wbr>block defines a color range used to fill GRADIENT parts. The colors are defined with the red, green, blue, alpha, delta format.&nbsp;<wbr> </p>
<p>&nbsp;<wbr> </p>
<p> name [spectrum name] The name of the spectrum used as reference later in the theme. </p>
<p>&nbsp;<wbr> </p>
<p> color [red] [green] [blue] [alpha] [delta] Each color declaration represents a stop point in the color range. The last parameter (delta) is used to set the proportion of a given stop point higher or lower in contrast with the other color&#8217;s delta value. </p>
<p> <code> styles </code> </p>
<p>styles<br />
{<br />
    style<br />
    {<br />
    name:<br />
        &#8216;stylename&#8217;;<br />
    base:<br />
        &#8216;..default style properties..&#8217;;<br />
    tag:<br />
        &#8216;tagname&#8217; &#8216;..style properties..&#8217;;<br />
        ..<br />
    }<br />
    ..<br />
}</p>
<p>&nbsp;<wbr>The&nbsp;<wbr>&#8216;styles&#8217;&nbsp;<wbr>block contains a list of one or more&nbsp;<wbr>&#8216;style&#8217;&nbsp;<wbr>blocks. A&nbsp;<wbr>&#8216;style&#8217;&nbsp;<wbr>block is used to create style&nbsp;<wbr>&lt;tags&gt;&nbsp;<wbr>for advanced TEXTBLOCK formatting.&nbsp;<wbr> </p>
<p>&nbsp;<wbr> </p>
<p> name [style name] The name of the style to be used as reference later in the theme. </p>
<p>&nbsp;<wbr> </p>
<p> base [style properties string] The default style properties that will be applied to the complete text. </p>
<p>&nbsp;<wbr> </p>
<p> tag [tag name] [style properties string] Style to be applied only to text between style &lt;tags&gt;..&lt;/tags&gt;. </p>
<p> <code> collections </code> </p>
<p>collections<br />
{<br />
    ..group<br />
    {<br />
    }<br />
    group{}<br />
        ..<br />
}</p>
<p>&nbsp;<wbr>The&nbsp;<wbr>&#8216;collections&#8217;&nbsp;<wbr>block is used to list the groups that compose the theme. Additional&nbsp;<wbr>&#8216;collections&#8217;&nbsp;<wbr>blocks do not prevent overriding group names.&nbsp;<wbr> </p>
<p> <code> group </code> </p>
<p>collections<br />
{<br />
    ..group<br />
    {<br />
    name:<br />
        &#8216;nameusedbytheapplication&#8217;;<br />
    alias:<br />
        &#8216;anothername&#8217;;<br />
    min:<br />
        width height;<br />
    max:<br />
        width height;<br />
        data<br />
        {<br />
        }<br />
        script<br />
        {<br />
        }<br />
        parts<br />
        {<br />
        }<br />
        programs<br />
        {<br />
        }<br />
    }<br />
    ..<br />
}</p>
<p>&nbsp;<wbr>A&nbsp;<wbr>&#8216;group&#8217;&nbsp;<wbr>block contains the list of parts and programs that compose a given Edje Object.&nbsp;<wbr> </p>
<p>&nbsp;<wbr> </p>
<p> name [group name] The name that will be used by the application to load the resulting Edje object, must be unique within the theme. </p>
<p>&nbsp;<wbr> </p>
<p> script_only [on/off] The flag (on/off) as to if this group is defined ONLY by script callbacks such as init(), resize() and shutdown() </p>
<p>&nbsp;<wbr> </p>
<p> alias [aditional group name] Additional name to serve as identifier. Defining multiple aliases is supported. </p>
<p>&nbsp;<wbr> </p>
<p> min [width] [height] The minimum size for the container defined by the composition of the parts. </p>
<p>&nbsp;<wbr> </p>
<p> max [width] [height] The maximum size for the container defined by the totality of the parts. </p>
<p> <code> script </code> </p>
<p>..group{<br />
    script{<br />
        // embryo script<br />
    }<br />
        ..program{<br />
            script{<br />
                // embryo script<br />
            }}<br />
        ..}<br />
    ..</p>
<p>&nbsp;<wbr>This block is used to&nbsp;<wbr>&#8216;inject&#8217;&nbsp;<wbr>embryo scripts to a given Edje theme and it functions in two modalities. When it&#8217;s included inside a&nbsp;<wbr>&#8216;program&#8217;&nbsp;<wbr>block, the script will be executed every time the program is run, on the other hand, when included directly into a&nbsp;<wbr>&#8216;group&#8217;,&nbsp;<wbr>&#8216;part&#8217;&nbsp;<wbr>or&nbsp;<wbr>&#8216;description&#8217;&nbsp;<wbr>block, it will be executed once at load time, in the load order.&nbsp;<wbr> </p>
<p> <code> part </code> </p>
<p>group<br />
{<br />
    parts<br />
    {<br />
        ..part<br />
        {<br />
        name:<br />
            &#8216;partname&#8217;;<br />
        type:<br />
            IMAGE;<br />
        mouse_events:<br />
            1;<br />
        repeat_events:<br />
            0;<br />
        ignore_flags:<br />
            NONE;<br />
        clip_to:<br />
            &#8216;anotherpart&#8217;;<br />
        source:<br />
            &#8216;groupname&#8217;;<br />
        pointer_mode:<br />
            AUTOGRAB;<br />
        use_alternate_font_metrics:<br />
            0;<br />
            description<br />
            {<br />
            }<br />
            dragable<br />
            {<br />
            }<br />
        }<br />
        ..<br />
    }<br />
}</p>
<p>&nbsp;<wbr>Parts are used to represent the most basic design elements of the theme, for example, a part can represent a line in a border or a label on a button.&nbsp;<wbr> </p>
<p>&nbsp;<wbr> </p>
<p> name [part name] The part&#8217;s name will be used as reference in the theme&#8217;s relative positioning system, by programs and in some cases by the application. It must be unique within the group. </p>
<p>&nbsp;<wbr> </p>
<p> type [TYPE] Set the type (all caps) from among the available types, it&#8217;s set to IMAGE by default. Valid types: </p>
<dl>
<dt>*</p>
<dd> RECT</p>
<dt>*</p>
<dd> TEXT</p>
<dt>*</p>
<dd> IMAGE</p>
<dt>*</p>
<dd> SWALLOW</p>
<dt>*</p>
<dd> TEXTBLOCK</p>
<dt>*</p>
<dd> GRADIENT</p>
<dt>*</p>
<dd> GROUP</dl>
<p>&nbsp;<wbr> </p>
<p> mouse_events [1 or 0] Specifies whether the part will emit signals, altought is named &#8216;mouse_events&#8217;, disabling it (0) will prevent the part from emitting any type of signal at all. Its set to 1 by default. </p>
<p>&nbsp;<wbr> </p>
<p> repeat_events [1 or 0] Specifies whether a part echoes a mouse event to other parts below the pointer (1), or not (0). Its set to 0 by default. </p>
<p>&nbsp;<wbr> </p>
<p> ignore_flags [FLAG] &#8230; Specifies whether events with the given flags should be ignored, i.e., will not have the signals emitted to the parts. Multiple flags must be separated by spaces, the effect will be ignoring all events with one of the flags specified. Possible flags: </p>
<dl>
<dt>*</p>
<dd> NONE (default value, no event will be ignored)</p>
<dt>*</p>
<dd> ON_HOLD</dl>
<p>&nbsp;<wbr> </p>
<p> scale [1 or 0] Specifies whether the part will scale its size with an edje scaling factor. By default scale is off (0) and the default scale factor is 1.0 &#8211; that means no scaling. This would be used to scale properties such as font size, min/max size of the part, and possibly can be used to scale based on DPI of the target device. The reason to be selective is that some things work well being scaled, others do not, so the designer gets to choose what works best. </p>
<p>&nbsp;<wbr> </p>
<p> pointer_mode [MODE] Sets the mouse pointer behavior for a given part. The default value is AUTOGRAB. Aviable modes: </p>
<dl>
<dt>*</p>
<dd> AUTOGRAB, when the part is clicked and the button remains pressed, the part will be the source of all future mouse signals emitted, even outside the object, until the button is released.</p>
<dt>*</p>
<dd> NOGRAB, the effect will be limited to the part&#8217;s container. container.</dl>
<p>&nbsp;<wbr> </p>
<p> precise_is_inside [1 or 0] Enables precise point collision detection for the part, which is more resource intensive. Disabled by default. </p>
<p>&nbsp;<wbr> </p>
<p> use_alternate_font_metrics [1 or 0] Only affects text and textblock parts, when enabled Edje will use different size measurement functions. Disabled by default. (note from the author: I don&#8217;t know what this is exactlu useful for?) </p>
<p>&nbsp;<wbr> </p>
<p> clip_to [another part&#8217;s name] Only renders the area of part that coincides with another part&#8217;s container. Overflowing content will not be displayed. </p>
<p>&nbsp;<wbr> </p>
<p> source [another group&#8217;s name] Only available to GROUP parts. Swallows the specified group into the part&#8217;s container. </p>
<p>&nbsp;<wbr> </p>
<p> effect [EFFECT] Causes Edje to draw the selected effect among: </p>
<dl>
<dt>*</p>
<dd> PLAIN</p>
<dt>*</p>
<dd> OUTLINE</p>
<dt>*</p>
<dd> SOFT_OUTLINE</p>
<dt>*</p>
<dd> SHADOW</p>
<dt>*</p>
<dd> SOFT_SHADOW</p>
<dt>*</p>
<dd> OUTLINE_SHADOW</p>
<dt>*</p>
<dd> OUTLINE_SOFT_SHADOW</p>
<dt>*</p>
<dd> FAR_SHADOW</p>
<dt>*</p>
<dd> FAR_SOFT_SHADOW</p>
<dt>*</p>
<dd> GLOW</dl>
<p> <code> dragable </code> </p>
<p>part<br />
{<br />
    ..dragable<br />
    {<br />
    confine:<br />
        &#8216;another part&#8217;;<br />
    events:<br />
        &#8216;another dragable part&#8217;;<br />
    x:<br />
        0 0 0;<br />
    y:<br />
        0 0 0;<br />
    }<br />
    ..<br />
}</p>
<p>&nbsp;<wbr>When this block is used the resulting part can be dragged around the interface, do not confuse with external drag&nbsp;<wbr>&amp;&nbsp;<wbr>drop. By default Edje&nbsp;<wbr>(and most applications)&nbsp;<wbr>will attempt to use the minimal size possible for a dragable part. If the min property is not set in the description the part will be&nbsp;<wbr>(most likely)&nbsp;<wbr>set to 0px width and 0px height, thus invisible.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>x&nbsp;<wbr>&nbsp;<wbr>[enable/disable]&nbsp;<wbr>[step]&nbsp;<wbr>[count]&nbsp;<wbr>&nbsp;<wbr>Used to setup dragging events for the X axis. The first parameter is used to enable&nbsp;<wbr>(1 or -1)&nbsp;<wbr>and disable&nbsp;<wbr>(0)&nbsp;<wbr>dragging along the axis. When enabled, 1 will set the starting point at 0.0 and -1 at 1.0. The second parameter takes any integer and will limit movement to values divisibles by it, causing the part to jump from position to position. The third parameter,&nbsp;<wbr>(question from the author: What is count for?).&nbsp;<wbr> </p>
<p>&nbsp;<wbr> </p>
<p> y [enable/disable] [step] [count] Used to setup dragging events for the Y axis. The first parameter is used to enable (1 or -1) and disable (0) dragging along the axis. When enabled, 1 will set the starting point at 0.0 and -1 at 1.0. The second parameter takes any integer and will limit movement to values divisibles by it, causing the part to jump from position to position. The third parameter, (question from the author: What is count for?). </p>
<p>&nbsp;<wbr> </p>
<p> confine [another part&#8217;s name] When set, limits the movement of the dragged part to another part&#8217;s container. </p>
<p>&nbsp;<wbr> </p>
<p> events [another dragable part&#8217;s name] It causes the part to forward the drag events to another part, thus ignoring them for itself. </p>
<p> <code> description </code> </p>
<p>description<br />
{<br />
inherit:<br />
    &#8216;another_description&#8217; INDEX;<br />
state:<br />
    &#8216;description_name&#8217; INDEX;<br />
visible:<br />
    1;<br />
min:<br />
    0 0;<br />
max:<br />
    -1 &#8211; 1;<br />
align:<br />
    0.5 0.5;<br />
fixed:<br />
    0 0;<br />
step:<br />
    0 0;<br />
aspect:<br />
    1 1;<br />
    rel1{<br />
        ..} rel2<br />
    {<br />
        ..<br />
    }<br />
}</p>
<p>&nbsp;<wbr>Every part can have one or more description blocks. Each description is used to define style and layout properties of a part in a given&nbsp;<wbr>&#8216;state&#8217;.&nbsp;<wbr> </p>
<p>&nbsp;<wbr> </p>
<p> inherit [another description&#8217;s name] [another description&#8217;s index] When set, the description will inherit all the properties from the named description. The properties defined in this part will override the inherited properties, reducing the amount of necessary code for simple state changes. Note: inheritance in Edje is single level only. </p>
<p>&nbsp;<wbr> </p>
<p> state [a name for the description] [an index] Sets a name used to identify a description inside a given part. Multiple descriptions are used to declare different states of the same part, like &#8216;clicked&#8217; or &#8216;invisible&#8217;. All states declarations are also coupled with an index number between 0.0 and 1.0. All parts must have at least one description named &#8216;default 0.0&#8217;. </p>
<p>&nbsp;<wbr> </p>
<p> visible [0 or 1] Takes a boolean value specifying whether part is visible (1) or not (0). Non-visible parts do not emit signals. The default value is 1. </p>
<p>&nbsp;<wbr> </p>
<p> align [X axis] [Y axis] When the displayed object&#8217;s size is smaller than its container, this property moves it relatively along both axis inside its container. The default value is &#8216;0.5 0.5&#8217;. </p>
<p>&nbsp;<wbr> </p>
<p> fixed [width, 0 or 1] [height, 0 or 1] When the &#8216;min&#8217; or &#8216;max&#8217; properties are set, fixed enables or disables resizing for each dimension. The default value is &#8216;0 0&#8217; </p>
<p>&nbsp;<wbr> </p>
<p> min [width] [height] The minimum size of the state. </p>
<p>&nbsp;<wbr> </p>
<p> max [width] [height] The maximum size of the state. </p>
<p>&nbsp;<wbr> </p>
<p> step [width] [height] Restricts resizing of each dimension to values divisibles by its value. This causes the part to jump from value to value while resizing. The default value is &#8216;0 0&#8217; disabling stepping. </p>
<p>&nbsp;<wbr> </p>
<p> aspect [min] [max] Normally width and height can be resized to any values independently. The aspect property forces the width to height ratio to be kept between the minimum and maximum set. For example, &#8216;1.0 1.0&#8217; will increase the width a pixel for every pixel added to heigh. The default value is &#8216;0.0 0.0&#8217; disabling aspect. </p>
<p>&nbsp;<wbr> </p>
<p> aspect_preference [DIMENSION] Sets the scope of the &#8216;aspect&#8217; property to a given dimension. Available options are BOTH, VERTICAL, HORIZONTAL and NONE </p>
<p>&nbsp;<wbr> </p>
<p> color_class [color class name] The part will use the color values of the named color_class, these values can be overrided by the &#8216;color&#8217;, &#8216;color2&#8217; and &#8216;color3&#8217; properties set below. </p>
<p>&nbsp;<wbr> </p>
<p> color [red] [green] [blue] [alpha] Sets the main color to the specified values (between 0 and 255). </p>
<p>&nbsp;<wbr> </p>
<p> color2 [red] [green] [blue] [alpha] Sets the text shadow color to the specified values (0 to 255). </p>
<p>&nbsp;<wbr> </p>
<p> color3 [red] [green] [blue] [alpha] Sets the text outline color to the specified values (0 to 255). </p>
<p> <code> rel1/rel2 </code> </p>
<p>description<br />
{<br />
    ..rel1<br />
    {<br />
    relative:<br />
        0.0 0.0;<br />
    offset:<br />
        0 0;<br />
    }<br />
    ..rel2<br />
    {<br />
    relative:<br />
        1.0 1.0;<br />
    offset:<br />
        -1 &#8211; 1;<br />
    }<br />
    ..<br />
}</p>
<p>&nbsp;<wbr>The rel1 and rel2 blocks are used to define the position of each corner of the part&#8217;s container. With rel1 being the left-up corner and rel2 being the right-down corner.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>relative&nbsp;<wbr>&nbsp;<wbr>[X axis]&nbsp;<wbr>[Y axis]&nbsp;<wbr>&nbsp;<wbr>Moves a corner to a relative position inside the container of the relative&nbsp;<wbr>&#8216;to&#8217;&nbsp;<wbr>part. Values from 0.0&nbsp;<wbr>(0%, begining)&nbsp;<wbr>to 1.0&nbsp;<wbr>(100%, end)&nbsp;<wbr>of each axis.&nbsp;<wbr> </p>
<p>&nbsp;<wbr> </p>
<p> offset [X axis] [Y axis] Affects the corner postion a fixed number of pixels along each axis. </p>
<p>&nbsp;<wbr> </p>
<p> to [another part&#8217;s name] Causes a corner to be positioned relatively to another part&#8217;s container. </p>
<p>&nbsp;<wbr> </p>
<p> to_x [another part&#8217;s name] Causes a corner to be positioned relatively to the X axis of another part&#8217;s container. Simply put affects the first parameter of &#8216;relative&#8217;. </p>
<p>&nbsp;<wbr> </p>
<p> to_y [another part&#8217;s name] Causes a corner to be positioned relatively to the Y axis of another part&#8217;s container. Simply put, affects the second parameter of &#8216;relative&#8217;. </p>
<p> <code> image </code> </p>
<p>description<br />
{<br />
    ..image<br />
    {<br />
    normal:<br />
        &#8216;filename.ext&#8217;;<br />
    tween:<br />
        &#8216;filename2.ext&#8217;;<br />
        ..tween : &#8216;filenameN.ext&#8217;;<br />
    border:<br />
        left right top bottom;<br />
    middle:<br />
        0 &#8211; 1;<br />
    }<br />
    ..<br />
}</p>
<p>&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>normal&nbsp;<wbr>&nbsp;<wbr>[image&#8217;s filename]&nbsp;<wbr>&nbsp;<wbr>Name of image to be used as previously declared in the images block. In an animation, this is the first and last image displayed. It&#8217;s required in any image part&nbsp;<wbr> </p>
<p>&nbsp;<wbr> </p>
<p> tween [image&#8217;s filename] Name of an image to be used in an animation loop, an image block can have none, one or multiple tween declarations. Images are displayed in the order they are listed. </p>
<p>&nbsp;<wbr> </p>
<p> border [left] [right] [top] [bottom] If set, the area (in pixels) of each side of the image will be displayed as a fixed size border, from the side -&gt; inwards, preventing the corners from being changed on a resize. </p>
<p>&nbsp;<wbr> </p>
<p> middle [0 or 1] If border is set, this boolean value tells Edje if the rest of the image (not covered by the defined border) will be displayed or not. The default value is 1. </p>
<p> <code> fill </code> </p>
<p>description<br />
{<br />
    ..fill<br />
    {<br />
    smooth:<br />
        0 &#8211; 1;<br />
        origin<br />
        {<br />
        relative:<br />
            X &#8211; axis Y &#8211; axis;<br />
        offset:<br />
            X &#8211; axis Y &#8211; axis;<br />
        }<br />
        size<br />
        {<br />
        relative:<br />
            width height;<br />
        offset:<br />
            width height;<br />
        }<br />
    }<br />
    ..<br />
}</p>
<p>&nbsp;<wbr>The fill method is an optional block that defines the way an IMAGE or GRADIENT part is going to be displayed inside its container.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>smooth&nbsp;<wbr>&nbsp;<wbr>[0 or 1]&nbsp;<wbr>&nbsp;<wbr>The smooth property takes a boolean value to decide if the image will be smoothed on scaling&nbsp;<wbr>(1)&nbsp;<wbr>or not&nbsp;<wbr>(0). The default value is 1.&nbsp;<wbr> </p>
<p>&nbsp;<wbr> </p>
<p> spread TODO TODO </p>
<p>&nbsp;<wbr> </p>
<p> angle TODO TODO </p>
<p>&nbsp;<wbr> </p>
<p> type TODO TODO </p>
<p> <code> origin </code> </p>
<p>description<br />
{<br />
    ..fill{<br />
        ..<br />
        origin{<br />
            relative : 0.0 0.0;<br />
offset:<br />
    0 0;<br />
}<br />
..<br />
}<br />
..<br />
}</p>
<p>&nbsp;<wbr>The origin block is used to place the starting point, inside the displayed element, that will be used to render the tile. By default, the origin is set at the element&#8217;s left-up corner.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>relative&nbsp;<wbr>&nbsp;<wbr>[X axis]&nbsp;<wbr>[Y axis]&nbsp;<wbr>&nbsp;<wbr>Sets the starting point relatively to displayed element&#8217;s content.&nbsp;<wbr> </p>
<p>&nbsp;<wbr> </p>
<p> offset [X axis] [Y axis] Affects the starting point a fixed number of pixels along each axis. </p>
<p> <code> size </code> </p>
<p>description<br />
{<br />
    ..fill{<br />
        ..<br />
        size{<br />
            relative : 1.0 1.0;<br />
offset:<br />
    -1 &#8211; 1;<br />
}<br />
..<br />
}<br />
..<br />
}</p>
<p>&nbsp;<wbr>The size block defines the tile size of the content that will be displayed.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>relative&nbsp;<wbr>&nbsp;<wbr>[width]&nbsp;<wbr>[height]&nbsp;<wbr>&nbsp;<wbr>Takes a pair of decimal values that represent the a percentual value of the original size of the element. For example,&nbsp;<wbr>&#8216;0.5 0.5&#8217;&nbsp;<wbr>represents half the size, while&nbsp;<wbr>&#8216;2.0 2.0&#8217;&nbsp;<wbr>represents the double. The default value is&nbsp;<wbr>&#8216;1.0 1.0&#8217;.&nbsp;<wbr> </p>
<p>&nbsp;<wbr> </p>
<p> offset [X axis] [Y axis] Affects the size of the tile a fixed number of pixels along each axis. </p>
<p> <code> text </code> </p>
<p>part<br />
{<br />
    description<br />
    {<br />
        ..text<br />
        {<br />
        text:<br />
            &#8216;some string of text to display&#8217;;<br />
        font:<br />
            &#8216;font_name&#8217;;<br />
        size:<br />
            SIZE;<br />
        text_class:<br />
            &#8216;class_name&#8217;;<br />
        fit:<br />
            horizontal vertical;<br />
        min:<br />
            horizontal vertical;<br />
        max:<br />
            horizontal vertical;<br />
        align:<br />
            X &#8211; axis Y &#8211; axis;<br />
        source:<br />
            &#8216;part_name&#8217;;<br />
        text_source:<br />
            &#8216;text_part_name&#8217;;<br />
        elipsis:<br />
            0.0 &#8211; 1.0;<br />
        style:<br />
            &#8216;stylename&#8217;;<br />
        }<br />
        ..<br />
    }<br />
}</p>
<p>&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>text&nbsp;<wbr>&nbsp;<wbr>[a string of text, or nothing]&nbsp;<wbr>&nbsp;<wbr>Sets the default content of a text part, normally the application is the one changing its value.&nbsp;<wbr> </p>
<p>&nbsp;<wbr> </p>
<p> text_class [text class name] Similar to color_class, this is the name used by the application to alter the font family and size at runtime. </p>
<p>&nbsp;<wbr> </p>
<p> font [font alias] This sets the font family to one of the aliases set up in the &#8216;fonts&#8217; block. Can be overrided by the application. </p>
<p>&nbsp;<wbr> </p>
<p> style [the style name] Causes the part to use the default style and tags defined in the &#8216;style&#8217; block with the specified name. </p>
<p>&nbsp;<wbr> </p>
<p> size [font size in points (pt)] Sets the default font size for the text part. Can be overrided by the application. </p>
<p>&nbsp;<wbr> </p>
<p> fit [horizontal] [vertical] When any of the parameters is set to 1 edje will resize the text for it to fit in it&#8217;s container. Both are disabled by default. </p>
<p>&nbsp;<wbr> </p>
<p> min [horizontal] [vertical] When any of the parameters is enabled (1) it forces the minimum size of the container to be equal to the minimum size of the text. The default value is &#8216;0 0&#8217;. </p>
<p>&nbsp;<wbr> </p>
<p> max [horizontal] [vertical] When any of the parameters is enabled (1) it forces the maximum size of the container to be equal to the maximum size of the text. The default value is &#8216;0 0&#8217;. </p>
<p>&nbsp;<wbr> </p>
<p> align [horizontal] [vertical] Change the position of the point of balance inside the container. The default value is 0.5 0.5. </p>
<p>&nbsp;<wbr> </p>
<p> source [another TEXT part&#8217;s name] Causes the part to use the text properties (like font and size) of another part and update them as they change. </p>
<p>&nbsp;<wbr> </p>
<p> text_source [another TEXT part&#8217;s name] Causes the part to display the text content of another part and update them as they change. </p>
<p>&nbsp;<wbr> </p>
<p> text_elipsis [point of balance] Used to balance the text in a relative point from 0.0 to 1.0, this point is the last section of the string to be cut out in case of a resize that is smaller than the text itself. The default value is 0.0. </p>
<p> <code> gradient </code> </p>
<p>part<br />
{<br />
    description{<br />
        ..<br />
        gradient{<br />
            type : &#8216;linear&#8217;;<br />
    spectrum &#8216;spectrumName&#8217;;<br />
    rel1<br />
    {<br />
    relative:<br />
        0.0 0.0;<br />
    offset:<br />
        0 0;<br />
    }<br />
    rel2<br />
        relative : 1.0 1.0;<br />
offset:<br />
    -1 &#8211; 1;<br />
}<br />
}<br />
..<br />
}<br />
}</p>
<p>&nbsp;<wbr>A gradient block is used to display a given&nbsp;<wbr>&#8216;spectrum&#8217;&nbsp;<wbr>inside a container. The container&#8217;s shape is a rect but this not mean the gradient is restricted to a rectangular shape. Gradients can use&nbsp;<wbr>&#8216;rel1&#8217;&nbsp;<wbr>and&nbsp;<wbr>&#8216;rel2&#8217;&nbsp;<wbr>blocks to layout the initial and final point relatively inside the container.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>type&nbsp;<wbr>&nbsp;<wbr>[the name of the type]&nbsp;<wbr>&nbsp;<wbr>Alters the gradient&#8217;s rendering algorithm between:&nbsp;<wbr> </p>
<dl>
<dt>*</p>
<dd> linear (default)</p>
<dt>*</p>
<dd> radial</dl>
<p>&nbsp;<wbr> </p>
<p> spectrum [an existing spectrum name] Causes the gradient to display the colors as defined by a given &#8216;spectrum&#8217; in the &#8216;spectra&#8217; block. </p>
<p>&nbsp;<wbr> </p>
<p> relative [a relative X coordinate] [a relative Y coordinate] Inside rel1 places the initial point, or first color, of the gradient relatively to the gradient&#8217;s container. Inside rel2 places the final point, or last color. </p>
<p>&nbsp;<wbr> </p>
<p> offset [X axis] [Y axis] Inside rel1 moves the initial point, or first color, of the gradient a fixed number of pixels along either axis. Inside rel2 moves the final point, or last color. </p>
<p> <code> program </code> </p>
<pre><code>
group
{
    programs
    {
        ..program
        {
        name:
            'programname';
        signal:
            'signalname';
        source:
            'partname';
        in:
            0.3 0.0;
        action:
            STATE_SET 'statename' state_value;
        transition:
            LINEAR 0.5;
        target:
            'partname';
        target:
            'anotherpart';
        after:
            'programname';
        after:
            'anotherprogram';
        }
        ..
    }
}
</code></pre>
<p>&nbsp;<wbr>Programs define how your interface reacts to events. Programs can change the state of parts, react to events or trigger other events.&nbsp;<wbr> </p>
<p>&nbsp;<wbr> </p>
<p> name [program name] Symbolic name of program as a unique identifier. </p>
<p>&nbsp;<wbr> </p>
<p> signal [signal name] Specifies signal(s) that should cause the program to run. The signal received must match the specified source to run. Signals may be globbed, but only one signal keyword per program may be used. ex: signal: &#8216;mouse,clicked,*&#8217;; (clicking any mouse button that matches source starts program). </p>
<p>&nbsp;<wbr> </p>
<p> source [source name] Source of accepted signal. Sources may be globbed, but only one source keyword per program may be used. ex:source: &#8216;button-*&#8217;; (Signals from any part or program named &#8216;button-*&#8217; are accepted) </p>
<p>&nbsp;<wbr> </p>
<p> in [from] [range] Wait &#8216;from&#8217; seconds before executing the program. And add a random number of seconds (from 0 to &#8216;range&#8217;) to the total waiting time. </p>
<p>&nbsp;<wbr> </p>
<p> action [type] [param1] [param2] Action to be performed by the program. Valid actions are: STATE_SET, ACTION_STOP, SIGNAL_EMIT, DRAG_VAL_SET, DRAG_VAL_STEP and DRAG_VAL_PAGE. Only one action can be specified per program. Examples: </p>
<p>&nbsp;<wbr>action: STATE_SET&nbsp;<wbr>&#8216;statename&#8217;&nbsp;<wbr>0.5; </p>
<p>&nbsp;<wbr>action: ACTION_STOP&nbsp;<wbr>&#8216;programname&#8217;; </p>
<p>&nbsp;<wbr>action: SIGNAL_EMIT&nbsp;<wbr>&#8216;signalname&#8217;&nbsp;<wbr>&#8217;emitter&#8217;;&nbsp;<wbr> </p>
<p>&nbsp;<wbr> </p>
<p> transition [type] [length] Defines how transistions occur using STATE_SET action. </p>
<p>&nbsp;<wbr>Where&nbsp;<wbr>&#8216;type&#8217;&nbsp;<wbr>is the style of the transistion and&nbsp;<wbr>&#8216;length&#8217;&nbsp;<wbr>is a double specifying the number of seconds in which to preform the transistion. </p>
<p>&nbsp;<wbr>Valid types are: LINEAR, SINUSOIDAL, ACCELERATE, and DECELERATE.&nbsp;<wbr> </p>
<p>&nbsp;<wbr> </p>
<p> target [target] Program or part on which the specified action acts. Multiple target keywords may be specified, one per target. SIGNAL_EMITs do not have targets. </p>
<p>&nbsp;<wbr> </p>
<p> after [after] Specifies a program to run after the current program completes. The source and signal parameters of a program run as an &#8216;after&#8217; are ignored. Multiple &#8216;after&#8217; statements can be specified per program. </p>
<hr>
<h2>Index</h2>
