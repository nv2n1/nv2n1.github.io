---
title: "pyscss(1)"
name: "pyscss"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pyscss/"
description: "pyscss – pyScss Documentation"
---

<h2>NAME</h2>
<p> pyscss &#8211; pyScss Documentation </p>
<p> <i>build-status</i> <i>coverage</i> </p>
<p> pyScss is a Python implementation of <i>Sass</i>, a CSS preprocessing language that adds variables, expressions, nested rules, mixins, inheritance, and other features that help ease the maintenance of large stylesheets. </p>
<p> pyScss also includes support for Compass, and has an extension mechanism for adding your own custom behavior. </p>
<p> pyScss is not yet fully compatible with the canonical Ruby implementation, but we&#8217;re getting there and constantly improving. Please feel free to <i>file a GitHub issue</i> for anything pyScss gets wrong. <i>Click here to lend your support to pyScss and make a donation at pledgie.com!</i> </p>
<p> Contents:</p>
<h2>INSTALLATION AND USAGE</h2>
<h3>Installation</h3>
<p> pyScss requires only Python 2.6 or later, including Python 3.x. PyPy is also known to work. Install with pip: </p>
<pre>
pip install pyScss
</pre>
<p> It has a handful of pure-Python dependencies, which pip should install for you:</p>
<dl>
<dt>&bull;</p>
<dd> <code>six</code></p>
<dt>&bull;</p>
<dd> <code>enum34</code> (for Python 3.3 and below)</p>
<dt>&bull;</p>
<dd> <code>pathlib</code> (for Python 3.3 and below) </p>
<p> There&#8217;s also an optional C speedup module, which requires having <code>libpcre</code> and its development headers installed, with UTF-8 support enabled (which it is by default).</dl>
<h3>Usage</h3>
<p> Run from the command line by using <code>-m</code>: </p>
<pre>
python -m scss &lt; file.scss
</pre>
<p> Specify directories to search for imports with <code>-I</code>. See <code>python -mscss &#8211;help</code> for more options. </p>
<p> <code>NOTE:</code> <code>-mscss</code> will only work in Python 2.7 and above. In Python 2.6, <code>-m</code> doesn&#8217;t work with packages, and you need to invoke this instead: </p>
<pre>
python -m scss.tool
</pre>
<h3>Interactive mode</h3>
<p> To get a REPL: </p>
<pre>
python -mscss --interactive
</pre>
<p> Example session: </p>
<pre><code>
$ python scss.py-- interactive &gt;&gt;&gt; @import "compass/css3" &gt;&gt;&gt; show()
                                                                  ['functions', 'mixins', 'options', 'vars'] &gt;&gt;&gt;
    show(mixins)
        ['apply-origin',
         'apply-transform',
         ... 'transparent'] &gt;&gt;&gt;
    show(mixins, transparent)
        @mixin transparent()
{
    @include opacity(0);
}
&gt;&gt;&gt; 1px + 5px 6px &gt;&gt;&gt; _
</code></pre>
<h3>Compass example</h3>
<p> With <code>&#8211;load-path</code> set to Compass and Blueprint roots, you can compile with Compass like with the following: </p>
<p>@option compress : no;<br />
$blueprint &#8211; grid &#8211; columns : 24;<br />
$blueprint &#8211; grid &#8211; width : 30px;<br />
$blueprint &#8211; grid &#8211; margin : 10px;<br />
$font &#8211; color : #333;<br />
@import &#8220;compass/reset&#8221;;<br />
@import &#8220;compass/utilities&#8221;;<br />
@import &#8220;blueprint&#8221;;<br />
// your code&#8230;</p>
<h2>PYTHON API</h2>
<h3>Legacy API</h3>
<p> <code>WARNING:</code> This API is still supported while the new API below is worked out, but it&#8217;s slated for deprecation and eventual removal. If you don&#8217;t need any of the features not yet available with the new API, consider porting as soon as possible.</p>
<h3>Compiling files</h3>
<p> Very basic usage is simple enough: </p>
<pre>
from scss import Scss
css = Scss()
css.compile(&quot;a { color: red + green; }&quot;)
</pre>
<h3>Configuration</h3>
<p> There are several configuration variables in the <code>scss.config</code> module that you may wish to change. </p>
<p> <code>PROJECT_ROOT</code>: Root of your entire project. Used only to construct defaults for other variables. Defaults to the root of the pyScss installation, which is probably not what you want. </p>
<p> <code>LOAD_PATHS</code>: An iterable of paths to search when using&#8220;@import&#8220;. </p>
<p> <code>STATIC_ROOT</code>: Used for finding sprite files. Defaults to <code>$PROJECT_ROOT/static</code>. </p>
<p> <code>ASSETS_ROOT</code>: Generated sprites are saved here. Defaults to <code>$STATIC_ROOT/assets</code>. </p>
<p> <code>CACHE_ROOT</code>: Used for storing cached sprite information. Defaults to <code>ASSETS_ROOT</code>. </p>
<p> <code>STATIC_URL</code>: URL equivalent to <code>STATIC_ROOT</code>. Defaults to <code>static/</code>. </p>
<p> <code>ASSETS_URL</code>: URL equivalent to <code>ASSETS_ROOT</code>. Defaults to <code>static/assets/</code>. </p>
<p> <code>SPRTE_MAP_DIRECTION</code>: Direction in which to arrange sprites in a spritesheet. Defaults to <code>vertical</code>; may be changed to <code>horizontal</code>, <code>diagonal</code>, or <code>smart</code>. </p>
<p> <code>VERBOSITY</code>: Increase spew from the compiler. Defaults to <code>1</code>. </p>
<p> <code>DEBUG</code>: Set to true to make parse errors fatal. Defaults to false.</p>
<h3>Django example</h3>
<p> A rough example of using pyScss with Django: </p>
<p>import os import fnmatch import scss from django.conf import settings from django.utils.datastructures import SortedDict from django.contrib.staticfiles import finders def finder(glob) : &#8220;&#8221;<br />
                                                                                                                                                                                           &#8221;<br />
                                                                                                                                                                                   Finds all files in the django finders for a given glob,<br />
                                                                                                                                                                                   returns the file path, if available, and the django storage object.storage objects must implement the File storage API:https: //docs.djangoproject.com/en/dev/ref/files/storage/<br />
                                                                                                                                                                                                                        &#8220;&#8221;<br />
                                                                                                                                                                                                                        &#8221;<br />
                                                                                                                                                                                                                        for finder in finders.get_finders() : for path, storage in finder.list([]) : if fnmatch.fnmatchcase(path, glob) :yield path, storage<br />
#STATIC_ROOT is where pyScss looks for images and static data.<br />
#STATIC_ROOT can be either a fully qualified path name or a &#8220;finder&#8221;<br />
#iterable function that receives a filename or glob and returns a tuple<br />
#of the file found and its file storage object for each matching file.<br />
#(https: //docs.djangoproject.com/en/dev/ref/files/storage/)<br />
                                                                                                                                                                                                                                                                                                                                                     scss.config.STATIC_ROOT = finder scss.config.STATIC_URL = settings.STATIC_URL<br />
#ASSETS_ROOT is where the pyScss outputs the generated files such as spritemaps<br />
#and compile cache:<br />
                                                                                                                                                                                                                                                                                                                                                     scss.config.ASSETS_ROOT = os.path.join(settings.MEDIA_ROOT, &#8216;assets/&#8217;) scss.config.ASSETS_URL = settings.MEDIA_URL + &#8216;assets/&#8217;<br />
#These are the paths pyScss will look &#8220;.scss&#8221; files on.This can be the path to<br />
#the compass framework or blueprint or compass &#8211; recepies, etc.<br />
                                                                                                                                                                                                                                                                                                                                                                                            scss.config.LOAD_PATHS =[&#8216;/usr/local/www/sass/frameworks/&#8217;, &#8216;/Library/Ruby/Gems/1.8/gems/compass-0.11.5/frameworks/compass/stylesheets/&#8217;, &#8216;/Library/Ruby/Gems/1.8/gems/compass-0.11.5/frameworks/blueprint/stylesheets/&#8217;, ]<br />
#This creates the Scss object used to compile SCSS code.In this example,<br />
#_scss_vars will hold the context variables:<br />
                                                                                                                                                                                                                                                                                                                                                                                                                     _scss_vars = {} _scss = scss.Scss(scss_vars = _scss_vars, scss_opts = {&#8216;compress&#8217; :True, &#8216;debug_info&#8217; :True, })<br />
# 1. Compile from a string:<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                compiled_css_from_string = _scss.compile(&#8216;@import &#8220;file2&#8221;; a {color: red + green; }&#8217;)<br />
# 2. Compile from a file:<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             compiled_css_from_file = _scss.compile(scss_file = &#8216;file1.scss&#8217;)<br />
# 3. Compile from a set of files(use SortedDict or collections.OrderedDict to<br />
#maintain the compile order):<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        _scss._scss_files = SortedDict(((&#8216;file2.scss&#8217;, open(&#8216;file2.scss&#8217;).read()), (&#8216;file3.scss&#8217;, open(&#8216;file3.scss&#8217;).read()), (&#8216;file4.scss&#8217;, open(&#8216;file4.scss&#8217;).read()), )) compiled_css_from_files = _scss.compile()</p>
<p> <code>NOTE:</code> The API here is likely to be improved in 1.3, to avoid the need for calling underscored functions.</p>
<h3>New API</h3>
<p> The simplest example: </p>
<pre>
from scss.compiler import compile_string
print(compile_string(&quot;a { color: red + green; }&quot;))
</pre>
<p> <code>scss.compiler.compile_string()</code> is just a simple wrapper around the <code>scss.compiler.Compiler</code> class: </p>
<pre>
from scss.compiler import Compiler
compiler = Compiler()
print(compiler.compile_string(&quot;a { color: red + green; }&quot;))
</pre>
<p> The most common arguments passed to <i>Compiler</i> are:</p>
<dl>
<dt><code>search_path</code></p>
<dd> A list of paths to search for <code>@import</code>s. May be either strings or <code>pathlib.Path</code> objects.</dl>
<h3>Extending pyScss</h3>
<p> A significant advantage to using pyScss is that you can inject Python values and code into the Sass compilation process.</p>
<h3>Injecting values</h3>
<p> You can define Sass values by creating and populating a <code>scss.namespace.Namespace</code>: </p>
<p>from scss.namespace import Namespace<br />
    from scss.types import String namespace = Namespace() namespace.set_variable(&#8216;$base-url&#8217;, String(&#8216;http://localhost/&#8217;))<br />
                                                  compiler = Compiler(namespace = namespace)<br />
                                                                 compiler.compile_string(&#8216;div { background: url($base-url); }&#8217;)</p>
<p> Now, <code>$base-url</code> will be available to the compiled Sass code, just like any other variable. Note that the value given must be one of the Sass types defined in <code>scss.types</code>.</p>
<h3>Injecting functions</h3>
<p> You can inject functions the same way: </p>
<pre>
def square(x):
    return x * x
namespace.set_function('square', 1, square)
</pre>
<p> This creates a function <code>square</code> for use in your Sass source. Optional arguments, keyword arguments, and slurpy arguments are all supported automatically. The arguments are Sass types, and the return value must be one as well. </p>
<p> The second argument is the arity — the number of required arguments, or None if any number of arguments is allowed. Sass functions can be overloaded by arity, so this is required. For functions with optional arguments, adding the same function multiple times can be tedious and error-prone, so the <code>declare</code> decorator is also available: </p>
<pre>
@namespace.declare
def square(x):
    return x * x
</pre>
<p> This will inspect the arguments for you and register the function with all arities it accepts. The function name is determined from the Python name: underscores become hyphens, and trailing underscores are removed. If you&#8217;d prefer to be more explicit, there&#8217;s also a <code>declare_alias</code>: </p>
<pre>
@namespace.declare_alias('square')
def square(x):
    return x * x
</pre>
<h3>API reference</h3>
<h3>scss.compiler</h3>
<h3>scss.namespace</h3>
<h3>scss.extension</h3>
<h2>PYSCSS SYNTAX</h2>
<h3>Supported Sass features</h3>
<p> pyScss is mostly compatible with Sass 3.2 and has partial support for the upcoming Sass 3.3. The canonical syntax reference is in the Sass documentation: <i><a rel="nofollow" href="http://sass-lang.com/docs/yardoc/file.SASS_REFERENCE.html">http://sass-lang.com/docs/yardoc/file.SASS_REFERENCE.html</a></i></p>
<h3>Both syntaxes</h3>
<p> SCSS (CSS3 superset) is the primary syntax, but there&#8217;s experimental support for the SASS (YAML-like) syntax.</p>
<h3>Built-in functions</h3>
<p> All of the Sass 3.2 functions described in <i>the Sass documentation</i> are supported.</p>
<h3>Rule nesting</h3>
<p> Rule/selector nesting and the <code>&amp;</code> parent-reference selector are both supported. </p>
<p> Example: </p>
<p>.selector<br />
{<br />
    a<br />
    {<br />
    display:<br />
        block;<br />
    }<br />
    strong<br />
    {<br />
    color:<br />
        blue;<br />
    }<br />
}</p>
<p> Produces: </p>
<p>.selector a<br />
{<br />
display:<br />
    block;<br />
}<br />
.selector strong<br />
{<br />
color:<br />
    blue;<br />
}</p>
<h3>Variables, data types</h3>
<p> Variables are supported. All of the Sass data types—strings, numbers, booleans, colors, lists, maps, and null—are supported. </p>
<p> Example: </p>
<p>$main &#8211; color : #ce4dd6;<br />
$style : solid;<br />
$side : bottom;<br />
#navbar {<br />
border &#8211; #{$side}:<br />
{<br />
color:<br />
    $main &#8211; color;<br />
style:<br />
    $style;<br />
}<br />
}</p>
<p> Produces: </p>
<p>#navbar {<br />
border &#8211; bottom &#8211; color : #ce4dd6;<br />
border &#8211; bottom &#8211; style : solid;<br />
}</p>
<h3>Functions and mixins</h3>
<p> <code>@function</code>, <code>@mixin</code>, and <code>@include</code> (optionally with <code>@content</code>) are supported. </p>
<p> Named arguments (<code>foo($name: value)</code>) and slurpy arguments (<code>foo($args&#8230;)</code>) are also supported. </p>
<p> Example: </p>
<p>@mixin rounded($side, $radius : 10px)<br />
{<br />
    border &#8211; #{$side} &#8211; radius : $radius;<br />
    -moz &#8211; border &#8211; radius &#8211; #{$side} : $radius;<br />
    -webkit &#8211; border &#8211; #{$side} &#8211; radius : $radius;<br />
}<br />
#navbar li{@include rounded(top); }<br />
#footer{@include rounded(top, 5px); }<br />
#sidebar{@include rounded(left, 8px); }</p>
<p> Produces: </p>
<p>#navbar li {<br />
border &#8211; top &#8211; radius : 10px;<br />
&#8211; moz &#8211; border &#8211; radius &#8211; top:10px;<br />
&#8211; webkit &#8211; border &#8211; top &#8211; radius:10px;<br />
}<br />
#footer {<br />
border &#8211; top &#8211; radius : 5px;<br />
&#8211; moz &#8211; border &#8211; radius &#8211; top:5px;<br />
&#8211; webkit &#8211; border &#8211; top &#8211; radius:5px;<br />
}<br />
#sidebar {<br />
border &#8211; left &#8211; radius : 8px;<br />
&#8211; moz &#8211; border &#8211; radius &#8211; left:8px;<br />
&#8211; webkit &#8211; border &#8211; left &#8211; radius:8px;<br />
}</p>
<h3>Rule extension</h3>
<p> <code>@extend</code> is supported, though some particularly thorny edge cases may not produce output identical to the reference compiler. </p>
<p> Example: </p>
<p>.error<br />
{<br />
border:<br />
    1px #f00;<br />
    background &#8211; color : #fdd;<br />
}<br />
.error.intrusion<br />
{<br />
    background &#8211; image : url(&#8220;/image/hacked.png&#8221;);<br />
}<br />
.seriousError<br />
{<br />
    @extend.error;<br />
    border &#8211; width : 3px;<br />
}</p>
<p> Produces: </p>
<p>.error,<br />
    .seriousError<br />
{<br />
border:<br />
    1px red;<br />
    background &#8211; color : #fdd;<br />
}<br />
.error.intrusion,<br />
    .seriousError.intrusion<br />
{<br />
    background &#8211; image : url(&#8220;/image/hacked.png&#8221;);<br />
}<br />
.seriousError<br />
{<br />
    border &#8211; width : 3px;<br />
}</p>
<h3>Conditions</h3>
<p> <code>@if</code>, <code>@else if</code>, and <code>@else</code> are supported.</p>
<h3>Loops</h3>
<p> Both types of iteration are supported: </p>
<p>@for $n from 1 through 9<br />
{<br />
    .span &#8211; #{$n}<br />
    {<br />
    width:<br />
        $n * 10 % ;<br />
    }<br />
}<br />
@each $color in red, blue, yellow<br />
{<br />
    .button &#8211; #{$color}<br />
    {<br />
        background &#8211; color : $color;<br />
    }<br />
}</p>
<p> Additionally, the unpacking-iteration syntax in Sass trunk is supposed; see <i>maps</i>.</p>
<h3>Maps</h3>
<p> pyScss has experimental support for maps, a data type recently added to Sass trunk. Maps are defined with colons inside parentheses: </p>
<pre>
$colors: (
    text: black,
    background: white
);
</pre>
<p> Keys may be any Sass expression, not just strings. </p>
<p> Maps are manipulated with a handful of map functions: </p>
<p>a<br />
{<br />
color:<br />
    map &#8211; get($colors, text);<br />
    background &#8211; color : map &#8211; get($colors, background);<br />
}</p>
<p> A map is semantically equivalent to a list of 2-lists, stored in the order they appeared when the map was defined. Any list operation will work on a map: </p>
<p>div<br />
{<br />
// I don&#8217;t know why you&#8217;d do this  :)<br />
margin:<br />
    nth($colors, 1); // =&gt; text, black<br />
}</p>
<p> Maps may be iterated over with <code>@each</code>, of course, but each item will be a somewhat clumsy 2-list. Instead, you can give multiple variables to do an unpacking iteration: </p>
<p>@each $key, $value in $colors<br />
{<br />
    // I don&#8217;t know why you&#8217;d do this either!<br />
    [data &#8211; style = $key] {<br />
        color:<br />
            $value;<br />
    }<br />
}</p>
<p> This syntax works on any list-of-lists.</p>
<h3>Everything is a list</h3>
<p> Another change borrowed from Sass trunk: any scalar type (string, number, boolean, etc.) will also act as a list of one element when used where a list is expected. This is most useful when writing Python extensions, but may also save you from checking <code>type-of</code> in a complex API.</p>
<h3>Compass support</h3>
<p> An arbitrary cross-section of Compass 0.11 is supported:</p>
<dl>
<dt>&bull;</p>
<dd> <code>Math functions</code>: <code>sin</code>, <code>cos</code>, <code>tan</code>, <code>round</code>, <code>ceil</code>, <code>floor</code>, <code>pi</code>, <code>e</code></p>
<dt>&bull;</p>
<dd> <code>Images</code>: <code>image-url</code>, <code>image-width</code>, <code>image-height</code>&#8230;</p>
<dt>&bull;</p>
<dd> <code>Embedded (inline) images</code>: <code>inline-image</code> </p>
<p> <code>NOTE:</code> Currently, Compass support is provided by default, which has led to some surprising behavior since parts of Compass conflict with parts of CSS3. In the future, Compass will become an extension like it is for Ruby, and you will have to opt in.</dl>
<h3>Sprites</h3>
<p> Example: </p>
<p>$icons : sprite &#8211; map(&#8220;sociable/*.png&#8221;); // contains sociable/facebook.png among others.<br />
div<br />
{<br />
background:<br />
    $icons;<br />
}<br />
@each $icon in sprites($icons)<br />
{<br />
    div.#{$icon}<br />
    {<br />
    width:<br />
        image &#8211; width(sprite &#8211; file($icons, $icon));<br />
    height:<br />
        image &#8211; height(sprite &#8211; file($icons, $icon));<br />
        background &#8211; position : sprite &#8211; position($icons, $icon);<br />
    }<br />
}</p>
<p> &#8230;generates a new sprite file and produces something like: </p>
<p>div<br />
{<br />
background:<br />
    url(&#8220;/static/assets/u8Y7yEQL0UffAVw5rX7yhw.png?_=1298240989&#8221;) 0px 0px no &#8211; repeat;<br />
}<br />
div.facebook<br />
{<br />
width:<br />
    32px;<br />
height:<br />
    32px;<br />
    background &#8211; position : 0px 0px;<br />
}<br />
div.twitter<br />
{<br />
width:<br />
    32px;<br />
height:<br />
    32px;<br />
    background &#8211; position : 0px &#8211; 32px;<br />
}<br />
&#8230;</p>
<h3>pyScss-specific extensions</h3>
<p> pyScss supports some constructs that upstream Sass does not, for various reasons. Listed here are &quot;blessed&quot; features in no danger of being removed, though you should avoid them if you&#8217;re at all interested in working with the reference compiler. </p>
<p> There are also some deviations that only exist for backwards compatibility; you should <code>not</code> rely on them, they will start spewing warnings at some point in the future, and eventually they will disappear. They are listed separately in <i>deprecated-features</i>.</p>
<h3><code>@option</code></h3>
<p> Compiler options may be toggled at runtime with <code>@option</code>. At the moment the only supported option is <code>compress</code>, to control whether the output is compressed: </p>
<pre>
@option compress: true;
</pre>
<h3>Multiplying strings by numbers</h3>
<p> Much like in Python, this works: </p>
<pre>
content: &quot;foo&quot; * 3;  // =&gt; &quot;foofoofoo&quot;
</pre>
<p> This is a runtime error in the reference compiler.</p>
<h3>Deprecated features</h3>
<h3>Brackets to delimit expressions</h3>
<p> In an expression, square brackets are equivalent to parentheses: </p>
<pre>
margin-top: [1px + 2px] * 3;  // =&gt; 9px
</pre>
<p> This is a holdover from xCSS and will be removed in the future.</p>
<h3><code>extends</code></h3>
<p> There&#8217;s an alternative syntax for <code>@extend</code>: </p>
<pre>
a extends b {
    ...
}
</pre>
<p> This is identical to: </p>
<pre>
a {
    @extend b;
    ...
}
</pre>
<p> This is a holdover from xCSS and will be removed in the future.</p>
<h3><code>self</code> selector</h3>
<p> <code>self</code> is an alias for <code>&amp;</code>: </p>
<p>a<br />
{<br />
self:<br />
    hover<br />
    {<br />
        text &#8211; decoration : underline;<br />
    }<br />
}</p>
<p> This is a holdover from xCSS and will be removed in the future.</p>
<h3><code>@variables</code> block</h3>
<p> Variables may be declared in a dedicated block: </p>
<pre>
@variables {
    $color: red;
}
</pre>
<p> <code>@vars</code> is an alias for <code>@variables</code>. </p>
<p> This is a holdover from xCSS and will be removed in the future.</p>
<h3><code>+foo</code> to include a mixin</h3>
<p> This: </p>
<pre>
div {
    +border-radius 3px;
}
</pre>
<p> Is equivalent to this: </p>
<p>div<br />
{<br />
    @include border &#8211; radius(3px);<br />
}</p>
<p> This is the same as the Sass syntax, but causes some parsing ambiguity, since <code>+foo</code> with a block could be either a nested CSS block with a sibling selector or a mixin call. Its future is uncertain, but you should probably avoid using it in SCSS files.</p>
<h3>Soft errors</h3>
<p> pyScss is much more liberal in what it accepts than the reference compiler; for example, rules at the top level and missing closing braces are accepted without complaint, and attempting to use a non-existent mixin only results in a warning. </p>
<p> pyScss 2.0 is likely to be much stricter; don&#8217;t rely on any particular abuse of syntax to work in the future.</p>
<h3>Operations on lists</h3>
<p> Binary operations with a list on the left-hand side are performed element-wise: </p>
<pre><code>
p
{
margin:
    (1em 0 3em) * 0.5; // =&gt; 0.5em 0 1.5em
}
</code></pre>
<p> Given that future versions of the reference compiler are likely to introduce built-in list operations, the future of this feature is unclear.</p>
<h3>Mixin injection</h3>
<p> A mixin defined like this: </p>
<pre>
@mixin foo(...) {
    // ...
}
</pre>
<p> will accept <code>any</code> keyword arguments, which will be available as variables within the mixin. </p>
<p> This behavior exists for historical reasons and due to the lack of a <code>**kwargs</code> equivalent within Sass. Its usage makes mixin behavior harder to understand and you should not use it.</p>
<h3>Unsupported Sass features</h3>
<p> Some Sass features are not supported or have some gaps. Each of these may be considered a bug.</p>
<h3>CLI</h3>
<p> pyScss&#8217;s command-line arguments are not entirely compatible with those of the reference compiler.</p>
<h3>Sass 3.3</h3>
<p> The following Sass 3.3 improvements are not yet implemented, but are planned for the near future:</p>
<dl>
<dt>&bull;</p>
<dd> Use of <code>&amp;</code> in expressions.</p>
<dt>&bull;</p>
<dd> <code>@at-root</code></p>
<dt>&bull;</p>
<dd> Source map support.</p>
<dt>&bull;</p>
<dd> Using <code>&#8230;</code> multiple times in a function call, or passing a map of arguments with <code>&#8230;</code>. Likewise, <code>keywords()</code> is not implemented.</p>
<dt>&bull;</p>
<dd> <code>unique-id()</code>, <code>call()</code>, and the various <code>*-exists()</code> functions are not implemented.</dl>
<h2>BACK MATTER</h2>
<h3>Reporting bugs</h3>
<p> If you have any suggestions, bug reports, or minor annoyances, please report them to the issue tracker on GitHub: <i><a rel="nofollow" href="http://github.com/Kronuz/pyScss/issues">http://github.com/Kronuz/pyScss/issues</a></i></p>
<h3>Contributing</h3>
<p> Please send us pull requests on GitHub! <i><a rel="nofollow" href="https://github.com/Kronuz/pyScss">https://github.com/Kronuz/pyScss</a></i></p>
<h3>Running the test suite</h3>
<p> The test suite is built atop the excellent <i>py.test</i> library, and can be run with: </p>
<pre>
py.test
</pre>
<p> from the root of a source checkout. </p>
<p> Most of the tests are pairs of input/output files in <code>scss/tests/files</code>; the test suite scans for these, compiles all the <code>.scss</code> files, and compares the output with the <code>.css</code> file of the same name. To run only particular tests, you can pass them directly as filenames: </p>
<pre>
py.test scss/tests/files/general/000-smoketest.scss
</pre>
<p> There are also several tests borrowed from the Ruby and C implementations. Many of these don&#8217;t work (due to missing features, different error messages, slightly different formatting, etc.), so to reduce the useless noise produced by a test run, you must explicitly opt into them with <code>&#8211;include-ruby</code>, even when using a file filter. These files are in the <code>from-ruby/</code> and <code>from-sassc/</code> subdirectories. </p>
<p> Other than the borrowed tests, the directory names are arbitrary.</p>
<h3>License and copyright</h3>
<p> Copyright © 2012 German M. Bravo (Kronuz), with additional heavy contributions by Eevee (Alex Munroe). Licensed under the <i>MIT license</i>. </p>
<p> pyScss is inspired by and partially derived from various projects:</p>
<dl>
<dt>&bull;</p>
<dd> <i>Compass</i> © 2009 Christopher M. Eppstein</p>
<dt>&bull;</p>
<dd> <i>Sass</i> © 2006-2009 Hampton Catlin and Nathan Weizenbaum</p>
<dt>&bull;</p>
<dd> <i>xCSS</i> © 2010 Anton Pawlik </p>
<p> Special thanks to Yelp for allowing Eevee to contribute to pyScss during working hours. Yelp does not claim copyright.</dl>
<h3>Changelog</h3>
<h3>1.3.4 (Dec 15, 2014)</h3>
<dl>
<dt>&bull;</p>
<dd> The modulus (<code>%</code>) operator is now supported.</p>
<dt>&bull;</p>
<dd> <code>/</code> and <code>&#8211;</code> inside an expression work correctly; this fixes some cases of using vanilla CSS&#8217;s <code>/</code> syntax.</p>
<dt>&bull;</p>
<dd> Relative imports have been more fixed.</p>
<dt>&bull;</p>
<dd> Line numbers in error messages are&#8230; more likely to be correct.</p>
<dt>&bull;</p>
<dd> Sass at-blocks now parse correctly even when there&#8217;s no space after the block name, e.g. <code>@if(foo){&#8230;}</code>.</p>
<dt>&bull;</p>
<dd> A few more cases of <code>#{&#8230;}</code> being replaced lexically have been switched to real parsing. </p>
<p> With these changes, pyScss can now successfully compile Zurb Foundation 5.</dl>
<h3>1.3.3 (Nov 18, 2014)</h3>
<dl>
<dt>&bull;</p>
<dd> URLs with quotes now parse as the <i>Url</i> type, not as generic functions. Fixes some uses of <code>@import</code>.</p>
<dt>&bull;</p>
<dd> A <code>return</code> got lost in the Compass gradient code, which would break some uses of gradients.</p>
<dt>&bull;</p>
<dd> Some API work in an attempt to get django-pyscss working against 1.3.</dl>
<h3>1.3.2 (Oct 17, 2014)</h3>
<dl>
<dt>&bull;</p>
<dd> Fix another couple embarrassing bugs, this time with the CLI.</p>
<dt>&bull;</p>
<dd> Fix the auto behavior of <code>join()</code> to match Ruby.</p>
<dt>&bull;</p>
<dd> Fully allow arbitrary expressions as map keys; previously, this only worked for the first key. <a href="/docs/linux/man/1-ll/">LL</a>(1) is hard.</p>
<dt>&bull;</p>
<dd> Restore Python 3.2 compatibility.</p>
<dt>&bull;</p>
<dd> Travis CI and Coveralls are now enabled.</dl>
<h3>1.3.1 (Oct 16, 2014)</h3>
<p> Fixes an embarrassing crash when compiling multiple files together.</p>
<h3>1.3.0 (Oct 15, 2014)</h3>
<p> This is a somewhat transitional release along the road to 2.0, which will remove a lot of deprecated features.</p>
<h3>Sass/CSS compatibility</h3>
<dl>
<dt>&bull;</p>
<dd> Importing files from a parent directory with <code>../</code> now works (as long as the imported file is still on the search path).</p>
<dt>&bull;</p>
<dd> Multiple CSS imports on the same line are now left unchanged. (Previously, the line would be repeated once for each import.)</p>
<dt>&bull;</p>
<dd> CSS 3 character set detection is supported.</p>
<dt>&bull;</p>
<dd> CSS escapes within strings are supported (though, unlike Sass, are usually printed literally rather than escaped).</p>
<dt>&bull;</p>
<dd> Map keys may now be arbitrary expressions.</p>
<dt>&bull;</p>
<dd> Slurpy named arguments are now supported.</p>
<dt>&bull;</p>
<dd> <code>!global</code> on variable assignments is now supported (and does nothing, as in Sass).</p>
<dt>&bull;</p>
<dd> <i>rebeccapurple</i> is understood as a color name. </p>
<p> Additionally, a great many more constructs should now parse correctly. By default, when pyScss encounters a parse error, it replaces any interpolations and variables, and treats the result as a single opaque string. </p>
<p> This was the only way syntax like <code>url(<a rel="nofollow" href="http://foo/bar)">http://foo/bar)</a></code> was recognized, since a colon is usually not allowed in the middle of a bareword. As a result, code like <code>background: url(&#8230;) scale-color(&#8230;);</code> didn&#8217;t work, because the url would fail to parse and so pyScss would never even know that <code>scale-color</code> is supposed to be a function call. </p>
<p> Now, the parser understands most of the unusual quirks of CSS syntax:</p>
<dt>&bull;</p>
<dd> <code>()</code> is recognized as an empty list.</p>
<dt>&bull;</p>
<dd> <code>url()</code> is fully supported.</p>
<dt>&bull;</p>
<dd> <code>expression()</code>, <code>alpha(opacity=&#8230;)</code>, and <code>calc()</code> are supported (and left alone, except for interpolation).</p>
<dt>&bull;</p>
<dd> Interpolation is part of the parser, rather than being applied before parsing, so there should be far fewer bugs with it.</p>
<dt>&bull;</p>
<dd> CSS escapes within barewords are recognized (and ignored).</p>
<dt>&bull;</p>
<dd> <code>!important</code> may have whitespace after the <code>!</code>. </p>
<p> Glossing over a bad parse now spits out a deprecation warning, and will be removed entirely in 2.0.</dl>
<h3>Bug fixes</h3>
<dl>
<dt>&bull;</p>
<dd> Old-style pseudo-element selectors (<code>:before</code> and friends, written with only one colon) always stay at the end of the selector.</p>
<dt>&bull;</p>
<dd> The CSS3 <code>grayscale(90%)</code> function is now left alone, rather than being treated as a Sass function. (Previously, only unitless numbers would trigger this behavior.)</p>
<dt>&bull;</p>
<dd> Placeholder selectors (<code>%foo</code>) no longer end up in the output.</p>
<dt>&bull;</p>
<dd> Iterating over a list of lists with a single variable works (again).</p>
<dt>&bull;</p>
<dd> File path handling is much more polite with Windows directory separators.</p>
<dt>&bull;</p>
<dd> At-rules broken across several lines are now recognized correctly.</p>
<dt>&bull;</p>
<dd> <code>@for &#8230; to</code> now excludes the upper bound.</p>
<dt>&bull;</p>
<dd> <code>@extend</code> no longer shuffles rules around, and should now produce rules in the same order as Ruby Sass. It also produces rules in the correct order when extending from the same rule more than once. Hopefully it&#8217;s now correct, once and for all.</p>
<dt>&bull;</p>
<dd> Fixed a couple more Compass gradient bugs. Probably.</dl>
<h3>New features</h3>
<dl>
<dt>&bull;</p>
<dd> Compatibility with Python 3.2, allegedly.</p>
<dt>&bull;</p>
<dd> Support for building SVG font sheets from within stylesheets.</p>
<dt>&bull;</p>
<dd> Error messages have been improved once again: parse errors should be somewhat less cryptic, the source of mixins is included in a traceback, and missing closing braces are reported.</dl>
<h3>Backwards-incompatible changes</h3>
<dl>
<dt>&bull;</p>
<dd> Missing imports are now fatal.</p>
<dt>&bull;</p>
<dd> Much sloppy behavior or reliance on old xCSS features will now produce deprecation warnings. All such behaviors will be removed in pyScss 2.0.</dl>
<h3>Internals</h3>
<dl>
<dt>&bull;</p>
<dd> The C speedups module is now Unicode-aware, and works under CPython 3.</p>
<dt>&bull;</p>
<dd> There&#8217;s no longer a runtime warning if the speedups module is not found.</p>
<dt>&bull;</p>
<dd> pyScss is now (a lot more) Unicode-clean; everything internally is treated as text, not bytes.</p>
<dt>&bull;</p>
<dd> Compiling the grammar is now much less painful, and doesn&#8217;t require copy-pasting anything.</p>
<dt>&bull;</p>
<dd> Several large modules have been broken up further. <code>__init__</code> is, at last, virtually empty.</p>
<dt>&bull;</p>
<dd> All the built-in functions have been moved into built-in extensions.</dl>
<h3>1.2.0 (Oct 8, 2013)</h3>
<p> This is a significant release that greatly increases compatibility with the reference compiler; in particular, the Sass port of Bootstrap now compiles. </p>
<p> There are a lot of changes here, so please feel free to report any bugs you see! The goal is 100% compatibility with the Ruby project.</p>
<h3>Missing Sass features</h3>
<dl>
<dt>&bull;</p>
<dd> Dashes and underscores are treated as interchangeable in variable, function, and mixin names.</p>
<dt>&bull;</p>
<dd> Rule blocks in the form <code>background: red { &#8230; }</code> are now supported.</p>
<dt>&bull;</p>
<dd> Colors are output as their shortest representation, and never as <code>hsl()</code>. The separate compiler options for compressing colors have been removed.</p>
<dt>&bull;</p>
<dd> The color modification functions (<code>adjust-color</code>, etc.) now work reliably.</p>
<dt>&bull;</p>
<dd> <code>transparent</code> is recognized as a color.</p>
<dt>&bull;</p>
<dd> Unrecognized units are now supported and treated as opaque.</p>
<dt>&bull;</p>
<dd> Arbitrary combinations of units (e.g., <code>px * px</code>) are supported for intermediate values. Unit cancellation now works reliably.</p>
<dt>&bull;</p>
<dd> Comparison and addition are now more in line with the Ruby behavior.</p>
<dt>&bull;</p>
<dd> <code>/</code> is now left untouched when it appears between literals, as in <code>font: 0 / 0</code>.</p>
<dt>&bull;</p>
<dd> <code>null</code> is supported.</p>
<dt>&bull;</p>
<dd> <code>zip()</code> is supported.</p>
<dt>&bull;</p>
<dd> <code>grayscale()</code> now knows it&#8217;s also a CSS3 filter function, and won&#8217;t be evaluated if its argument is a number.</p>
<dt>&bull;</p>
<dd> Slurpy arguments (<code>some-function($args&#8230;)</code>) are supported.</p>
<dt>&bull;</p>
<dd> <code>@extend</code> has been greatly improved: it eliminates common ancestors and works in many complex cases that used to produce strange results.</p>
<dt>&bull;</p>
<dd> Several Compass functions now adhere more closely to Compass&#8217;s behavior. <code>linear-gradient()</code> is less likely to wreck valid CSS3 syntax.</p>
<dt>&bull;</p>
<dd> Compass&#8217;s <code>e()</code>, <code>pow()</code>, <code>log()</code>, and <code>sqrt()</code> are now supported.</dl>
<h3>Bug fixes</h3>
<dl>
<dt>&bull;</p>
<dd> Interactive mode works. Again.</p>
<dt>&bull;</p>
<dd> Color names in strings and selectors are no longer replaced with hex equivalents.</p>
<dt>&bull;</p>
<dd> Unrecognized <code>@</code>-rule blocks such as <code>@keyframes</code> are left alone, rather than being treated like selectors.</p>
<dt>&bull;</p>
<dd> <code>@media</code> blocks aren&#8217;t repeated for every rule inside.</p>
<dt>&bull;</p>
<dd> Pound-interpolation always drops quotes on strings.</p>
<dt>&bull;</p>
<dd> Single quoted strings no longer lose their quotes when rendered.</p>
<dt>&bull;</p>
<dd> <code>+ foo { &#8230; }</code> is now recognized as a nested block, not an include.</p>
<dt>&bull;</p>
<dd> <code>color-stop()</code> and several proposed CSS4 functions no longer produce &quot;unrecognized function&quot; warnings.</p>
<dt>&bull;</p>
<dd> Several obscure bugs with variable scoping have been fixed, though a couple others remain.</p>
<dt>&bull;</p>
<dd> Several bugfixes to the C speedups module to bring it in line with the behavior of the pure-Python scanner.</dl>
<h3>New features</h3>
<dl>
<dt>&bull;</p>
<dd> Python 3 support. As a result, Python 2.5 no longer works; whether this is a bug or a feature is not yet clear.</p>
<dt>&bull;</p>
<dd> It&#8217;s possible to write custom Sass functions in Python, though the API for this is not final.</p>
<dt>&bull;</p>
<dd> Experimental support for the map type and destructuring <code>@each</code>, both unreleased additions to the Ruby project.</p>
<dt>&bull;</p>
<dd> Support for the new string and list functions in Sass 3.3.</p>
<dt>&bull;</p>
<dd> Added <code>background-brushed</code>.</dl>
<h3>Backwards-incompatible changes</h3>
<dl>
<dt>&bull;</p>
<dd> Configuration via monkeypatching the <code>scss</code> module no longer works. Monkeypatch <code>scss.config</code> instead.</p>
<dt>&bull;</p>
<dd> <code>em</code> and <code>px</code> are no longer compatible.</p>
<dt>&bull;</p>
<dd> Unrecognized variable names are now a fatal error.</dl>
<h3>Internals</h3>
<dl>
<dt>&bull;</p>
<dd> No longer a single 5000-line file!</p>
<dt>&bull;</p>
<dd> Vastly expanded test suite, including some experimental tests borrowed from the Ruby and C implementations.</p>
<dt>&bull;</p>
<dd> Parser now produces an AST rather than evaluating expressions during the parse, which allows for heavier caching and fixes some existing cache bugs.</p>
<dt>&bull;</p>
<dd> The type system has been virtually rewritten; types now act much less like Python types, and compilation uses Sass types throughout rather than mixing Python types with Sass types.</dl>
<h3>1.1.5 (Feb 15, 2013)</h3>
<dl>
<dt>&bull;</p>
<dd> <code>debug_info</code> now properly produces rules that can be used by FireSass and Google Chrome SASS Source Maps.</p>
<dt>&bull;</p>
<dd> Improved memory usage for large sets of files to be used as sprites.</p>
<dt>&bull;</p>
<dd> Warns about IE 4095 maximum number of selectors.</p>
<dt>&bull;</p>
<dd> <code>debug_info</code> prints info as comments if specified as <code>comments</code>.</p>
<dt>&bull;</p>
<dd> Better handling of undefined variables.</p>
<dt>&bull;</p>
<dd> Added CSS filter functions and <code>skewX</code> <code>skewY</code>.</p>
<dt>&bull;</p>
<dd> Command line tool and entry point fixed.</p>
<dt>&bull;</p>
<dd> Fix cache buster URLs when paths already include queries or fragments.</p>
<dt>&bull;</p>
<dd> Hashable Values.</dl>
<h3>1.1.4 (Aug 8, 2012)</h3>
<dl>
<dt>&bull;</p>
<dd> Added <code>&#8211;debug-info</code> command line option (for <i>FireSass</i> output).</p>
<dt>&bull;</p>
<dd> Added compass helper function <code>reject()</code>.</p>
<dt>&bull;</p>
<dd> Added <code>undefined</code> keyword for undefined variables.</dl>
<h3>1.1.3 (Jan 9, 2012)</h3>
<dl>
<dt>&bull;</p>
<dd> Support for the new Sass 3.2.0 features (<code>@content</code> and placeholder selectors)</p>
<dt>&bull;</p>
<dd> Fixed bug with line numbers throwing an exception.</dl>
<h3>1.1.2 (Jan 3, 2012)</h3>
<dl>
<dt>&bull;</p>
<dd> Regression bug fixed from 1.1.1</dl>
<h3>1.1.1 (Jan 2, 2012)</h3>
<dl>
<dt>&bull;</p>
<dd> Added optional C speedup module for an amazing boost in scanning speed!</p>
<dt>&bull;</p>
<dd> Added <code>headings</code>, <code>stylesheet-url</code>, <code>font-url</code>, <code>font-files</code>, <code>inline-font-files</code> and <code>sprite-names</code>.</dl>
<h3>1.1.0 (Dec 22, 2011)</h3>
<dl>
<dt>&bull;</p>
<dd> Added <code>min()</code> and <code>max()</code> for lists.</p>
<dt>&bull;</p>
<dd> Removed exception raise.</dl>
<h3>1.0.9 (Dec 22, 2011)</h3>
<dl>
<dt>&bull;</p>
<dd> Optimizations in the scanner.</p>
<dt>&bull;</p>
<dd> Added <code>background-noise()</code> for compass-recipes support.</p>
<dt>&bull;</p>
<dd> <code>enumerate()</code> and <code>range()</code> can go backwards. Ex.: <code>range(3, 0)</code> goes from 3 to 0.</p>
<dt>&bull;</p>
<dd> Added line numbers and files for errors.</p>
<dt>&bull;</p>
<dd> Added support for <i>Firebug</i> with <i>FireSass</i>.</p>
<dt>&bull;</p>
<dd> <code><a href="/docs/linux/man/n-nth/">nth</a>(n)</code> is round (returns the <code>nth mod len</code> item of the list).</p>
<dt>&bull;</p>
<dd> <code>&#8211;watch</code> added to the command line.</p>
<dt>&bull;</p>
<dd> Several bugs fixed.</dl>
<h3>1.0.8 (May 13, 2011)</h3>
<dl>
<dt>&bull;</p>
<dd> Changed source color (<code>$src-color</code>) default to black.</p>
<dt>&bull;</p>
<dd> Moved the module filename to <code>__init__.py</code> and module renamed back to scss.</p>
<dt>&bull;</p>
<dd> <i>genindex</i></p>
<dt>&bull;</p>
<dd> <i>modindex</i></p>
<dt>&bull;</p>
<dd> <i>search</i></dl>
<h2>AUTHOR</h2>
<p> German M. Bravo (Kronuz)</p>
<h2>COPYRIGHT</h2>
<p> 2013, German M. Bravo (Kronuz) </p>
<h2>Index</h2>
<dt><a href="#lbBX">BACK MATTER</a></p>
<dd>
<dt><a href="#lbDB">AUTHOR</a></p>
<dd>
<dt><a href="#lbDC">COPYRIGHT</a></p>
<dd></dl>
