---
title: "perltie(1)"
name: "perltie"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perltie/"
description: "perltie – how to hide an object class in a simple variable"
---

<h2 class="name">NAME</h2>
<p> perltie &#8211; how to hide an object class in a simple variable </p>
<h2>SYNOPSIS</h2>
<pre>
 tie VARIABLE, CLASSNAME, LIST
 $object = tied VARIABLE
 untie VARIABLE
</pre>
<h2>DESCRIPTION</h2>
<p> Prior to release 5.0 of Perl, a programmer could use <code>dbmopen()</code> to connect an on-disk database in the standard Unix <code><a href="//www.systutorials.com/docs/linux/man/3x-dbm/">dbm</a></code>(3x) format magically to a <tt>%HASH</tt> in their program. However, their Perl was either built with one particular dbm library or another, but not both, and you couldn&#8217;t extend this mechanism to other packages or types of variables. </p>
<p> Now you can. </p>
<p> The <code>tie()</code> function binds a variable to a class (package) that will provide the implementation for access methods for that variable. Once this magic has been performed, accessing a tied variable automatically triggers method calls in the proper class. The complexity of the class is hidden behind magic methods calls. The method names are in <font SIZE="-1">ALL CAPS,</font> which is a convention that Perl uses to indicate that they&#8217;re called implicitly rather than explicitly&#8212;just like the <font SIZE="-1"><code>BEGIN</code></font><code>()</code> and <font SIZE="-1"><code>END</code></font><code>()</code> functions. </p>
<p> In the <code>tie()</code> call, <tt>&quot;VARIABLE&quot;</tt> is the name of the variable to be enchanted. <tt>&quot;CLASSNAME&quot;</tt> is the name of a class implementing objects of the correct type. Any additional arguments in the <tt>&quot;LIST&quot;</tt> are passed to the appropriate constructor method for that class&#8212;meaning <font SIZE="-1"><code>TIESCALAR</code></font><code>()</code>, <font SIZE="-1"><code>TIEARRAY</code></font><code>()</code>, <font SIZE="-1"><code>TIEHASH</code></font><code>()</code>, or <font SIZE="-1"><code>TIEHANDLE</code></font><code>()</code>. (Typically these are arguments such as might be passed to the <code>dbminit()</code> function of C.) The object returned by the &#8220;new&#8221; method is also returned by the <code>tie()</code> function, which would be useful if you wanted to access other methods in <tt>&quot;CLASSNAME&quot;</tt>. (You don&#8217;t actually have to return a reference to a right &#8220;type&#8221; (e.g., <font SIZE="-1">HASH</font> or <tt>&quot;CLASSNAME&quot;</tt>) so long as it&#8217;s a properly blessed object.) You can also retrieve a reference to the underlying object using the <code>tied()</code> function. </p>
<p> Unlike <code>dbmopen()</code>, the <code>tie()</code> function will not <tt>&quot;use&quot;</tt> or <tt>&quot;require&quot;</tt> a module for you&#8212;you need to do that explicitly yourself.</p>
<h3>Tying Scalars</h3>
<p> A class implementing a tied scalar should define the following methods: <font SIZE="-1">TIESCALAR, FETCH, STORE,</font> and possibly <font SIZE="-1">UNTIE</font> and/or <font SIZE="-1">DESTROY.</font> </p>
<p> Let&#8217;s look at each in turn, using as an example a tie class for scalars that allows the user to do something like: </p>
<pre><code>
tie $his_speed, 'Nice', getppid();
tie $my_speed, 'Nice', $$;
</code></pre>
<p> And now whenever either of those variables is accessed, its current system priority is retrieved and returned. If those variables are set, then the process&#8217;s priority is changed! </p>
<p> We&#8217;ll use Jarkko Hietaniemi &lt;<i>jhi [at] iki.fi</i>&gt;&#8217;s BSD::Resource class (not included) to access the <font SIZE="-1">PRIO_PROCESS, PRIO_MIN,</font> and <font SIZE="-1">PRIO_MAX</font> constants from your system, as well as the <code>getpriority()</code> and <code>setpriority()</code> system calls. Here&#8217;s the preamble of the class. </p>
<p>package Nice;<br />
use Carp;<br />
use BSD::Resource;<br />
use strict;<br />
$Nice::DEBUG = 0 unless defined $Nice::DEBUG;</p>
<dl>
<dt><font SIZE="-1">TIESCALAR</font> classname, <font SIZE="-1">LIST</font></p>
<dd> This is the constructor for the class. That means it is expected to return a blessed reference to a new scalar (probably anonymous) that it&#8217;s creating. For example: </p>
<p>sub TIESCALAR<br />
{<br />
    my $class = shift;<br />
    my $pid = shift || $$;<br />
# 0 means me if ($pid !~/ ^\d + $ /)<br />
    {<br />
        carp &#8220;Nice::Tie::Scalar got non-numeric pid $pid&#8221; if $ ^ W;<br />
        return undef;<br />
    }<br />
    unless(kill 0, $pid)<br />
    {<br />
#EPERM or ERSCH, no doubt<br />
                                 carp &#8220;Nice::Tie::Scalar got bad pid $pid: $!&#8221; if $ ^<br />
                             W;<br />
        return undef;<br />
    }<br />
    return bless \$pid, $class;<br />
}</p>
<p> This tie class has chosen to return an error rather than raising an exception if its constructor should fail. While this is how <code>dbmopen()</code> works, other classes may well not wish to be so forgiving. It checks the global variable <tt>$^W</tt> to see whether to emit a bit of noise anyway.</p>
<dt><font SIZE="-1">FETCH</font> this</p>
<dd> This method will be triggered every time the tied variable is accessed (read). It takes no arguments beyond its self reference, which is the object representing the scalar we&#8217;re dealing with. Because in this case we&#8217;re using just a <font SIZE="-1">SCALAR</font> ref for the tied scalar object, a simple $$self allows the method to get at the real value stored there. In our example below, that real value is the process <font SIZE="-1">ID</font> to which we&#8217;ve tied our variable. </p>
<p>sub FETCH<br />
{<br />
    my $self = shift;<br />
    confess &#8220;wrong type&#8221; unless ref $self;<br />
    croak &#8220;usage error&#8221; if @_;<br />
    my $nicety;<br />
    local($ !) = 0;<br />
    $nicety = getpriority(PRIO_PROCESS, $$self);<br />
    if ($ !) {<br />
        croak &#8220;getpriority failed: $!&#8221;<br />
    }<br />
    return $nicety;<br />
}</p>
<p> This time we&#8217;ve decided to blow up (raise an exception) if the renice fails&#8212;there&#8217;s no place for us to return an error otherwise, and it&#8217;s probably the right thing to do.</p>
<dt><font SIZE="-1">STORE</font> this, value</p>
<dd> This method will be triggered every time the tied variable is set (assigned). Beyond its self reference, it also expects one (and only one) argument: the new value the user is trying to assign. Don&#8217;t worry about returning a value from <font SIZE="-1">STORE</font>; the semantic of assignment returning the assigned value is implemented with <font SIZE="-1">FETCH.</font> </p>
<p>sub STORE<br />
{<br />
    my $self = shift;<br />
    confess &#8220;wrong type&#8221; unless ref $self;<br />
    my $new_nicety = shift;<br />
    croak &#8220;usage error&#8221; if @_;<br />
    if ($new_nicety &lt; PRIO_MIN) {<br />
        carp sprintf<br />
            &#8220;WARNING: priority %d less than minimum system priority %d&#8221;,<br />
            $new_nicety, PRIO_MIN if $ ^ W;<br />
        $new_nicety = PRIO_MIN;<br />
    }<br />
    if ($new_nicety &gt; PRIO_MAX) {<br />
        carp sprintf<br />
            &#8220;WARNING: priority %d greater than maximum system priority %d&#8221;,<br />
            $new_nicety, PRIO_MAX if $ ^ W;<br />
        $new_nicety = PRIO_MAX;<br />
    }<br />
    unless(defined setpriority(PRIO_PROCESS,<br />
                               $$self,<br />
                               $new_nicety))<br />
    {<br />
        confess &#8220;setpriority failed: $!&#8221;;<br />
    }<br />
}</p>
<dt><font SIZE="-1">UNTIE</font> this</p>
<dd> This method will be triggered when the <tt>&quot;untie&quot;</tt> occurs. This can be useful if the class needs to know when no further calls will be made. (Except <font SIZE="-1">DESTROY</font> of course.) See &quot;The <tt>&quot;untie&quot;</tt> Gotcha&quot; below for more details.</p>
<dt><font SIZE="-1">DESTROY</font> this</p>
<dd> This method will be triggered when the tied variable needs to be destructed. As with other object classes, such a method is seldom necessary, because Perl deallocates its moribund object&#8217;s memory for you automatically&#8212;this isn&#8217;t C<font SIZE="-2">++</font>, you know. We&#8217;ll use a <font SIZE="-1">DESTROY</font> method here for debugging purposes only. </p>
<p>sub DESTROY<br />
{<br />
    my $self = shift;<br />
    confess &#8220;wrong type&#8221; unless ref $self;<br />
    carp &#8220;[ Nice::DESTROY pid $$self ]&#8221; if $Nice::DEBUG;<br />
}
</dl>
<p> That&#8217;s about all there is to it. Actually, it&#8217;s more than all there is to it, because we&#8217;ve done a few nice things here for the sake of completeness, robustness, and general aesthetics. Simpler <font SIZE="-1">TIESCALAR</font> classes are certainly possible.</p>
<h3>Tying Arrays</h3>
<p> A class implementing a tied ordinary array should define the following methods: <font SIZE="-1">TIEARRAY, FETCH, STORE, FETCHSIZE, STORESIZE, CLEAR</font> and perhaps <font SIZE="-1">UNTIE</font> and/or <font SIZE="-1">DESTROY.</font> </p>
<p> <font SIZE="-1">FETCHSIZE</font> and <font SIZE="-1">STORESIZE</font> are used to provide <tt>$#array</tt> and equivalent <tt>&quot;scalar(@array)&quot;</tt> access. </p>
<p> The methods <font SIZE="-1">POP, PUSH, SHIFT, UNSHIFT, SPLICE, DELETE,</font> and <font SIZE="-1">EXISTS</font> are required if the perl operator with the corresponding (but lowercase) name is to operate on the tied array. The <code>Tie::Array</code> class can be used as a base class to implement the first five of these in terms of the basic methods above. The default implementations of <font SIZE="-1">DELETE</font> and <font SIZE="-1">EXISTS</font> in <code>Tie::Array</code> simply <tt>&quot;croak&quot;</tt>. </p>
<p> In addition <font SIZE="-1">EXTEND</font> will be called when perl would have pre-extended allocation in a real array. </p>
<p> For this discussion, we&#8217;ll implement an array whose elements are a fixed size at creation. If you try to create an element larger than the fixed size, you&#8217;ll take an exception. For example: </p>
<p>use FixedElem_Array;<br />
tie @array, &#8216;FixedElem_Array&#8217;, 3;<br />
$array[0] = &#8216;cat&#8217;;<br />
#ok.$array[1] = &#8216;dogs&#8217;;<br />
#exception, length(&#8216;dogs&#8217;)&gt; 3.</p>
<p> The preamble code for the class is as follows: </p>
<pre>
    package FixedElem_Array;
    use Carp;
    use strict;
</pre>
<dl>
<dt><font SIZE="-1">TIEARRAY</font> classname, <font SIZE="-1">LIST</font></p>
<dd> This is the constructor for the class. That means it is expected to return a blessed reference through which the new array (probably an anonymous <font SIZE="-1">ARRAY</font> ref) will be accessed. </p>
<p> In our example, just to show you that you don&#8217;t <i>really</i> have to return an <font SIZE="-1">ARRAY</font> reference, we&#8217;ll choose a <font SIZE="-1">HASH</font> reference to represent our object. A <font SIZE="-1">HASH</font> works out well as a generic record type: the <tt>&quot;{ELEMSIZE}&quot;</tt> field will store the maximum element size allowed, and the <tt>&quot;{ARRAY}&quot;</tt> field will hold the true <font SIZE="-1">ARRAY</font> ref. If someone outside the class tries to dereference the object returned (doubtless thinking it an <font SIZE="-1">ARRAY</font> ref), they&#8217;ll blow up. This just goes to show you that you should respect an object&#8217;s privacy. </p>
<p>sub TIEARRAY<br />
{<br />
    my $class = shift;<br />
    my $elemsize = shift;<br />
    if (@_ || $elemsize = ~ /\D /) {<br />
        croak &#8220;usage: tie ARRAY, &#8216;&#8221;.__PACKAGE__.&#8221;&#8216;, elem_size&#8221;;<br />
    }<br />
    return bless{<br />
               ELEMSIZE = &gt; $elemsize,<br />
               ARRAY = &gt; [],<br />
           },<br />
           $class;<br />
}</p>
<dt><font SIZE="-1">FETCH</font> this, index</p>
<dd> This method will be triggered every time an individual element the tied array is accessed (read). It takes one argument beyond its self reference: the index whose value we&#8217;re trying to fetch. </p>
<p>sub FETCH<br />
{<br />
    my $self = shift;<br />
    my $index = shift;<br />
    return $self-&gt;<br />
    {<br />
        ARRAY<br />
        } -&gt; [$index];<br />
}</p>
<p> If a negative array index is used to read from an array, the index will be translated to a positive one internally by calling <font SIZE="-1">FETCHSIZE</font> before being passed to <font SIZE="-1">FETCH.</font> You may disable this feature by assigning a true value to the variable <tt>$NEGATIVE_INDICES</tt> in the tied array class. </p>
<p> As you may have noticed, the name of the <font SIZE="-1">FETCH</font> method (et al.) is the same for all accesses, even though the constructors differ in names (<font SIZE="-1">TIESCALAR</font> vs <font SIZE="-1">TIEARRAY</font>). While in theory you could have the same class servicing several tied types, in practice this becomes cumbersome, and it&#8217;s easiest to keep them at simply one tie type per class.</p>
<dt><font SIZE="-1">STORE</font> this, index, value</p>
<dd> This method will be triggered every time an element in the tied array is set (written). It takes two arguments beyond its self reference: the index at which we&#8217;re trying to store something and the value we&#8217;re trying to put there. </p>
<p> In our example, <tt>&quot;undef&quot;</tt> is really <tt>&quot;$self-&gt;{ELEMSIZE}&quot;</tt> number of spaces so we have a little more work to do here: </p>
<p>sub STORE<br />
{<br />
    my $self = shift;<br />
    my($index, $value) = @_;<br />
    if (length $value &gt; $self-&gt;{ELEMSIZE}) {<br />
        croak &#8220;length of $value is greater than $self-&gt;{ELEMSIZE}&#8221;;<br />
    }<br />
#fill in the blanks<br />
    $self-&gt;EXTEND($index) if $index &gt; $self-&gt;FETCHSIZE();<br />
#right justify to keep element size for smaller elements<br />
    $self-&gt;<br />
    {<br />
        ARRAY<br />
        } -&gt; [$index] = sprintf &#8220;%$self-&gt;{ELEMSIZE}s&#8221;, $value;<br />
}</p>
<p> Negative indexes are treated the same as with <font SIZE="-1">FETCH.</font></p>
<dt><font SIZE="-1">FETCHSIZE</font> this</p>
<dd> Returns the total number of items in the tied array associated with object <i>this</i>. (Equivalent to <tt>&quot;scalar(@array)&quot;</tt>). For example: </p>
<p>sub FETCHSIZE<br />
{<br />
    my $self = shift;<br />
    return scalar @{$self-&gt;{ARRAY}};<br />
}</p>
<dt><font SIZE="-1">STORESIZE</font> this, count</p>
<dd> Sets the total number of items in the tied array associated with object <i>this</i> to be <i>count</i>. If this makes the array larger then class&#8217;s mapping of <tt>&quot;undef&quot;</tt> should be returned for new positions. If the array becomes smaller then entries beyond count should be deleted. </p>
<p> In our example, &#8216;undef&#8217; is really an element containing <tt>&quot;$self-&gt;{ELEMSIZE}&quot;</tt> number of spaces. Observe: </p>
<p>sub STORESIZE<br />
{<br />
    my $self = shift;<br />
    my $count = shift;<br />
    if ($count &gt; $self-&gt;FETCHSIZE()) {<br />
        foreach ($count &#8211; $self-&gt;FETCHSIZE()..$count) {<br />
            $self-&gt;STORE($_, &#8221; );<br />
        }<br />
    }<br />
    elsif($count &lt; $self-&gt;FETCHSIZE())<br />
    {<br />
        foreach (0..$self-&gt;FETCHSIZE() &#8211; $count &#8211; 2) {<br />
            $self-&gt;POP();<br />
        }<br />
    }<br />
}</p>
<dt><font SIZE="-1">EXTEND</font> this, count</p>
<dd> Informative call that array is likely to grow to have <i>count</i> entries. Can be used to optimize allocation. This method need do nothing. </p>
<p> In our example, we want to make sure there are no blank (<tt>&quot;undef&quot;</tt>) entries, so <tt>&quot;EXTEND&quot;</tt> will make use of <tt>&quot;STORESIZE&quot;</tt> to fill elements as needed: </p>
<p>sub EXTEND<br />
{<br />
    my $self = shift;<br />
    my $count = shift;<br />
    $self-&gt;STORESIZE($count);<br />
}</p>
<dt><font SIZE="-1">EXISTS</font> this, key</p>
<dd> Verify that the element at index <i>key</i> exists in the tied array <i>this</i>. </p>
<p> In our example, we will determine that if an element consists of <tt>&quot;$self-&gt;{ELEMSIZE}&quot;</tt> spaces only, it does not exist: </p>
<p>sub EXISTS<br />
{<br />
    my $self = shift;<br />
    my $index = shift;<br />
    return 0 if !defined $self-&gt;<br />
    {<br />
        ARRAY<br />
        } -&gt; [$index] ||<br />
            $self-&gt;<br />
        {<br />
            ARRAY<br />
            } -&gt; [$index] eq &#8216; &#8216; x $self-&gt;{ELEMSIZE};<br />
    return 1;<br />
}</p>
<dt><font SIZE="-1">DELETE</font> this, key</p>
<dd> Delete the element at index <i>key</i> from the tied array <i>this</i>. </p>
<p> In our example, a deleted item is <tt>&quot;$self-&gt;{ELEMSIZE}&quot;</tt> spaces: </p>
<p>sub DELETE<br />
{<br />
    my $self = shift;<br />
    my $index = shift;<br />
    return $self-&gt;STORE($index, &#8221; );<br />
}</p>
<dt><font SIZE="-1">CLEAR</font> this</p>
<dd> Clear (remove, delete, &#8230;) all values from the tied array associated with object <i>this</i>. For example: </p>
<p>sub CLEAR<br />
{<br />
    my $self = shift;<br />
    return $self-&gt;{ARRAY} = [];<br />
}</p>
<dt><font SIZE="-1">PUSH</font> this, <font SIZE="-1">LIST</font></p>
<dd> Append elements of <i></i><font SIZE="-1"><i>LIST</i></font><i></i> to the array. For example: </p>
<p>sub PUSH<br />
{<br />
    my $self = shift;<br />
    my @list = @_;<br />
    my $last = $self-&gt;FETCHSIZE();<br />
    $self-&gt;STORE($last + $_, $list[$_]) foreach 0..$ #list;<br />
    return $self-&gt;FETCHSIZE();<br />
}</p>
<dt><font SIZE="-1">POP</font> this</p>
<dd> Remove last element of the array and return it. For example: </p>
<p>sub POP<br />
{<br />
    my $self = shift;<br />
    return pop @{$self-&gt;{ARRAY}};<br />
}</p>
<dt><font SIZE="-1">SHIFT</font> this</p>
<dd> Remove the first element of the array (shifting other elements down) and return it. For example: </p>
<p>sub SHIFT<br />
{<br />
    my $self = shift;<br />
    return shift @{$self-&gt;{ARRAY}};<br />
}</p>
<dt><font SIZE="-1">UNSHIFT</font> this, <font SIZE="-1">LIST</font></p>
<dd> Insert <font SIZE="-1">LIST</font> elements at the beginning of the array, moving existing elements up to make room. For example: </p>
<p>sub UNSHIFT<br />
{<br />
    my $self = shift;<br />
    my @list = @_;<br />
    my $size = scalar(@list);<br />
#make room for our list<br />
    @{$self-&gt;{ARRAY}}[$size..$ #{$self-&gt;{ARRAY}} + $size] = @{$self-&gt;{ARRAY}};<br />
    $self-&gt;STORE($_, $list[$_]) foreach 0..$ #list;<br />
}</p>
<dt><font SIZE="-1">SPLICE</font> this, offset, length, <font SIZE="-1">LIST</font></p>
<dd> Perform the equivalent of <tt>&quot;splice&quot;</tt> on the array. </p>
<p> <i>offset</i> is optional and defaults to zero, negative values count back from the end of the array. </p>
<p> <i>length</i> is optional and defaults to rest of the array. </p>
<p> <i></i><font SIZE="-1"><i>LIST</i></font><i></i> may be empty. </p>
<p> Returns a list of the original <i>length</i> elements at <i>offset</i>. </p>
<p> In our example, we&#8217;ll use a little shortcut if there is a <i></i><font SIZE="-1"><i>LIST</i></font><i></i>: </p>
<p>sub SPLICE<br />
{<br />
    my $self = shift;<br />
    my $offset = shift || 0;<br />
    my $length = shift || $self-&gt;FETCHSIZE() &#8211; $offset;<br />
    my @list = ();<br />
    if (@_) {<br />
        tie @list, __PACKAGE__, $self-&gt;{ELEMSIZE};<br />
        @list = @_;<br />
    }<br />
    return splice @{$self-&gt;{ARRAY}}, $offset, $length, @list;<br />
}</p>
<dt><font SIZE="-1">UNTIE</font> this</p>
<dd> Will be called when <tt>&quot;untie&quot;</tt> happens. (See &quot;The <tt>&quot;untie&quot;</tt> Gotcha&quot; below.)</p>
<dt><font SIZE="-1">DESTROY</font> this</p>
<dd> This method will be triggered when the tied variable needs to be destructed. As with the scalar tie class, this is almost never needed in a language that does its own garbage collection, so this time we&#8217;ll just leave it out.</dl>
<h3>Tying Hashes</h3>
<p> Hashes were the first Perl data type to be tied (see <code>dbmopen()</code>). A class implementing a tied hash should define the following methods: <font SIZE="-1">TIEHASH</font> is the constructor. <font SIZE="-1">FETCH</font> and <font SIZE="-1">STORE</font> access the key and value pairs. <font SIZE="-1">EXISTS</font> reports whether a key is present in the hash, and <font SIZE="-1">DELETE</font> deletes one. <font SIZE="-1">CLEAR</font> empties the hash by deleting all the key and value pairs. <font SIZE="-1">FIRSTKEY</font> and <font SIZE="-1">NEXTKEY</font> implement the <code>keys()</code> and <code>each()</code> functions to iterate over all the keys. <font SIZE="-1">SCALAR</font> is triggered when the tied hash is evaluated in scalar context, and in 5.28 onwards, by <tt>&quot;keys&quot;</tt> in boolean context. <font SIZE="-1">UNTIE</font> is called when <tt>&quot;untie&quot;</tt> happens, and <font SIZE="-1">DESTROY</font> is called when the tied variable is garbage collected. </p>
<p> If this seems like a lot, then feel free to inherit from merely the standard Tie::StdHash module for most of your methods, redefining only the interesting ones. See Tie::Hash for details. </p>
<p> Remember that Perl distinguishes between a key not existing in the hash, and the key existing in the hash but having a corresponding value of <tt>&quot;undef&quot;</tt>. The two possibilities can be tested with the <tt>&quot;exists()&quot;</tt> and <tt>&quot;defined()&quot;</tt> functions. </p>
<p> Here&#8217;s an example of a somewhat interesting tied hash class: it gives you a hash representing a particular user&#8217;s dot files. You index into the hash with the name of the file (minus the dot) and you get back that dot file&#8217;s contents. For example: </p>
<p>use DotFiles;<br />
tie % dot, &#8216;DotFiles&#8217;;<br />
if ($dot{profile} = ~ / MANPATH / ||<br />
                    $dot{login} = ~ / MANPATH / ||<br />
                                  $dot{cshrc} = ~ / MANPATH /) {<br />
    print &#8220;you seem to set your MANPATH
&#8221;;<br />
}</p>
<p> Or here&#8217;s another sample of using our tied class: </p>
<p>tie % him, &#8216;DotFiles&#8217;, &#8216;daemon&#8217;;<br />
foreach<br />
    $f(keys % him)<br />
    {<br />
        printf &#8220;daemon dot file %s is size %d
&#8221;,<br />
            $f, length $him{$f};<br />
    }</p>
<p> In our tied hash DotFiles example, we use a regular hash for the object containing several important fields, of which only the <tt>&quot;{LIST}&quot;</tt> field will be what the user thinks of as the real hash.</p>
<dl>
<dt><font SIZE="-1">USER</font></p>
<dd> whose dot files this object represents</p>
<dt><font SIZE="-1">HOME</font></p>
<dd> where those dot files live</p>
<dt><font SIZE="-1">CLOBBER</font></p>
<dd> whether we should try to change or remove those dot files</p>
<dt><font SIZE="-1">LIST</font></p>
<dd> the hash of dot file names and content mappings</dl>
<p> Here&#8217;s the start of <i>Dotfiles.pm</i>: </p>
<p>package DotFiles;<br />
use Carp;<br />
sub whowasi{(caller(1))[3].'()&#8217;} my $DEBUG = 0;<br />
sub debug<br />
{<br />
    $DEBUG = @_ ? shift : 1<br />
}</p>
<p> For our example, we want to be able to emit debugging info to help in tracing during development. We keep also one convenience function around internally to help print out warnings; <code>whowasi()</code> returns the function name that calls it. </p>
<p> Here are the methods for the DotFiles tied hash.</p>
<dl>
<dt><font SIZE="-1">TIEHASH</font> classname, <font SIZE="-1">LIST</font></p>
<dd> This is the constructor for the class. That means it is expected to return a blessed reference through which the new object (probably but not necessarily an anonymous hash) will be accessed. </p>
<p> Here&#8217;s the constructor: </p>
<p>sub TIEHASH<br />
{<br />
    my $self = shift;<br />
    my $user = shift || $ &gt; ;<br />
    my $dotdir = shift || &#8221;;<br />
    croak &#8220;usage: @{[&amp;whowasi]} [USER [DOTDIR]]&#8221; if @_;<br />
    $user = getpwuid($user) if $user = ~ / ^\d + $ / ;<br />
    my $dir = (getpwnam($user))[7] || croak &#8220;@{[&amp;whowasi]}: no user $user&#8221;;<br />
    $dir.= &#8220;/$dotdir&#8221; if $dotdir;<br />
    my $node = {<br />
        USER = &gt; $user,<br />
        HOME = &gt; $dir,<br />
        LIST = &gt; {},<br />
        CLOBBER = &gt; 0,<br />
    };<br />
    opendir(DIR, $dir) || croak &#8220;@{[&amp;whowasi]}: can&#8217;t opendir $dir: $!&#8221;;<br />
    foreach<br />
        $dot(grep / ^\./ &amp;&amp;-f &#8220;$dir/$_&#8221;, readdir(DIR))<br />
        {<br />
            $dot = ~s / ^\. //;<br />
                         $node-&gt;{<br />
                             LIST} {$dot} = undef;<br />
        }<br />
    closedir DIR;<br />
    return bless $node, $self;<br />
}</p>
<p> It&#8217;s probably worth mentioning that if you&#8217;re going to filetest the return values out of a readdir, you&#8217;d better prepend the directory in question. Otherwise, because we didn&#8217;t <code>chdir()</code> there, it would have been testing the wrong file.</p>
<dt><font SIZE="-1">FETCH</font> this, key</p>
<dd> This method will be triggered every time an element in the tied hash is accessed (read). It takes one argument beyond its self reference: the key whose value we&#8217;re trying to fetch. </p>
<p> Here&#8217;s the fetch for our DotFiles example. </p>
<p>sub FETCH<br />
{<br />
    carp &amp;whowasi if $DEBUG;<br />
    my $self = shift;<br />
    my $dot = shift;<br />
    my $dir = $self-&gt;{HOME};<br />
    my $file = &#8220;$dir/.$dot&#8221;;<br />
    unless(exists $self-&gt;{ LIST } -&gt; {$dot} || -f $file)<br />
    {<br />
        carp &#8220;@{[&amp;whowasi]}: no $dot file&#8221; if $DEBUG;<br />
        return undef;<br />
    }<br />
    if (defined $self-&gt;{ LIST } -&gt; {$dot}) {<br />
        return $self-&gt;<br />
        {<br />
            LIST<br />
            } -&gt; {$dot};<br />
    } else {<br />
        return $self-&gt;<br />
        {<br />
            LIST<br />
            } -&gt; {$dot} = `cat $dir /.$dot`;<br />
    }<br />
}</p>
<p> It was easy to write by having it call the Unix <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1) command, but it would probably be more portable to open the file manually (and somewhat more efficient). Of course, because dot files are a Unixy concept, we&#8217;re not that concerned.</p>
<dt><font SIZE="-1">STORE</font> this, key, value</p>
<dd> This method will be triggered every time an element in the tied hash is set (written). It takes two arguments beyond its self reference: the index at which we&#8217;re trying to store something, and the value we&#8217;re trying to put there. </p>
<p> Here in our DotFiles example, we&#8217;ll be careful not to let them try to overwrite the file unless they&#8217;ve called the <code>clobber()</code> method on the original object reference returned by <code>tie()</code>. </p>
<p>sub STORE<br />
{<br />
    carp &amp;whowasi if $DEBUG;<br />
    my $self = shift;<br />
    my $dot = shift;<br />
    my $value = shift;<br />
    my $file = $self-&gt;{HOME}.&#8221;/.$dot&#8221;;<br />
    my $user = $self-&gt;{USER};<br />
    croak &#8220;@{[&amp;whowasi]}: $file not clobberable&#8221; unless $self-&gt;{CLOBBER};<br />
    open(my $f, &#8216;&gt;&#8217;, $file) || croak &#8220;can&#8217;t open $file: $!&#8221;;<br />
    print $f $value;<br />
    close($f);<br />
}</p>
<p> If they wanted to clobber something, they might say: </p>
<p>$ob = tie % daemon_dots, &#8216;daemon&#8217;;<br />
$ob-&gt;clobber(1);<br />
$daemon_dots{signature} = &#8220;A true daemon
&#8221;;</p>
<p> Another way to lay hands on a reference to the underlying object is to use the <code>tied()</code> function, so they might alternately have set clobber using: </p>
<p>tie % daemon_dots, &#8216;daemon&#8217;;<br />
tied(% daemon_dots)-&gt;clobber(1);</p>
<p> The clobber method is simply: </p>
<p>sub clobber<br />
{<br />
    my $self = shift;<br />
    $self-&gt;{CLOBBER} = @_ ? shift : 1;<br />
}</p>
<dt><font SIZE="-1">DELETE</font> this, key</p>
<dd> This method is triggered when we remove an element from the hash, typically by using the <code>delete()</code> function. Again, we&#8217;ll be careful to check whether they really want to clobber files. </p>
<p>sub DELETE<br />
{<br />
    carp &amp;whowasi if $DEBUG;<br />
    my $self = shift;<br />
    my $dot = shift;<br />
    my $file = $self-&gt;{HOME}.&#8221;/.$dot&#8221;;<br />
    croak &#8220;@{[&amp;whowasi]}: won&#8217;t remove file $file&#8221; unless $self-&gt;{CLOBBER};<br />
    delete $self-&gt;<br />
    {<br />
        LIST<br />
        } -&gt; {$dot};<br />
    my $success = unlink($file);<br />
    carp &#8220;@{[&amp;whowasi]}: can&#8217;t unlink $file: $!&#8221; unless $success;<br />
    $success;<br />
}</p>
<p> The value returned by <font SIZE="-1">DELETE</font> becomes the return value of the call to <code>delete()</code>. If you want to emulate the normal behavior of <code>delete()</code>, you should return whatever <font SIZE="-1">FETCH</font> would have returned for this key. In this example, we have chosen instead to return a value which tells the caller whether the file was successfully deleted.</p>
<dt><font SIZE="-1">CLEAR</font> this</p>
<dd> This method is triggered when the whole hash is to be cleared, usually by assigning the empty list to it. </p>
<p> In our example, that would remove all the user&#8217;s dot files! It&#8217;s such a dangerous thing that they&#8217;ll have to set <font SIZE="-1">CLOBBER</font> to something higher than 1 to make it happen. </p>
<p>sub CLEAR<br />
{<br />
    carp &amp;whowasi if $DEBUG;<br />
    my $self = shift;<br />
    croak &#8220;@{[&amp;whowasi]}: won&#8217;t remove all dot files for $self-&gt;{USER}&#8221; unless $self-&gt;{CLOBBER} &gt; 1;<br />
    my $dot;<br />
    foreach<br />
        $dot(keys % {$self-&gt;{LIST}})<br />
        {<br />
            $self-&gt;DELETE($dot);<br />
        }<br />
}</p>
<dt><font SIZE="-1">EXISTS</font> this, key</p>
<dd> This method is triggered when the user uses the <code>exists()</code> function on a particular hash. In our example, we&#8217;ll look at the <tt>&quot;{LIST}&quot;</tt> hash element for this: </p>
<p>sub EXISTS<br />
{<br />
    carp &amp;whowasi if $DEBUG;<br />
    my $self = shift;<br />
    my $dot = shift;<br />
    return exists $self-&gt;<br />
    {<br />
        LIST<br />
        } -&gt; {$dot};<br />
}</p>
<dt><font SIZE="-1">FIRSTKEY</font> this</p>
<dd> This method will be triggered when the user is going to iterate through the hash, such as via a <code>keys()</code>, <code>values()</code>, or <code>each()</code> call. </p>
<p>sub FIRSTKEY<br />
{<br />
    carp &amp;whowasi if $DEBUG;<br />
    my $self = shift;<br />
    my $a = keys % {$self-&gt;{LIST}};<br />
#reset each() iterator<br />
            each %<br />
    {<br />
        $self-&gt;<br />
        {<br />
            LIST<br />
        }<br />
    }<br />
}</p>
<p> <font SIZE="-1">FIRSTKEY</font> is always called in scalar context and it should just return the first key. <code>values()</code>, and <code>each()</code> in list context, will call <font SIZE="-1">FETCH</font> for the returned keys.</p>
<dt><font SIZE="-1">NEXTKEY</font> this, lastkey</p>
<dd> This method gets triggered during a <code>keys()</code>, <code>values()</code>, or <code>each()</code> iteration. It has a second argument which is the last key that had been accessed. This is useful if you&#8217;re caring about ordering or calling the iterator from more than one sequence, or not really storing things in a hash anywhere. </p>
<p> <font SIZE="-1">NEXTKEY</font> is always called in scalar context and it should just return the next key. <code>values()</code>, and <code>each()</code> in list context, will call <font SIZE="-1">FETCH</font> for the returned keys. </p>
<p> For our example, we&#8217;re using a real hash so we&#8217;ll do just the simple thing, but we&#8217;ll have to go through the <font SIZE="-1">LIST</font> field indirectly. </p>
<p>sub NEXTKEY<br />
{<br />
    carp &amp;whowasi if $DEBUG;<br />
    my $self = shift;<br />
    return each %<br />
    {<br />
        $self-&gt;<br />
        {<br />
            LIST<br />
        }<br />
    }<br />
}</p>
<dt><font SIZE="-1">SCALAR</font> this</p>
<dd> This is called when the hash is evaluated in scalar context, and in 5.28 onwards, by <tt>&quot;keys&quot;</tt> in boolean context. In order to mimic the behaviour of untied hashes, this method must return a value which when used as boolean, indicates whether the tied hash is considered empty. If this method does not exist, perl will make some educated guesses and return true when the hash is inside an iteration. If this isn&#8217;t the case, <font SIZE="-1">FIRSTKEY</font> is called, and the result will be a false value if <font SIZE="-1">FIRSTKEY</font> returns the empty list, true otherwise. </p>
<p> However, you should <code>not</code> blindly rely on perl always doing the right thing. Particularly, perl will mistakenly return true when you clear the hash by repeatedly calling <font SIZE="-1">DELETE</font> until it is empty. You are therefore advised to supply your own <font SIZE="-1">SCALAR</font> method when you want to be absolutely sure that your hash behaves nicely in scalar context. </p>
<p> In our example we can just call <tt>&quot;scalar&quot;</tt> on the underlying hash referenced by <tt>&quot;$self-&gt;{LIST}&quot;</tt>: </p>
<p>sub SCALAR<br />
{<br />
    carp &amp;whowasi if $DEBUG;<br />
    my $self = shift;<br />
    return scalar %<br />
    {<br />
        $self-&gt;<br />
        {<br />
            LIST<br />
        }<br />
    }<br />
}</p>
<p> <font SIZE="-1">NOTE:</font> In perl 5.25 the behavior of scalar <tt>%hash</tt> on an untied hash changed to return the count of keys. Prior to this it returned a string containing information about the bucket setup of the hash. See &#8220;bucket_ratio&#8221; in Hash::Util for a backwards compatibility path.</p>
<dt><font SIZE="-1">UNTIE</font> this</p>
<dd> This is called when <tt>&quot;untie&quot;</tt> occurs. See &quot;The <tt>&quot;untie&quot;</tt> Gotcha&quot; below.</p>
<dt><font SIZE="-1">DESTROY</font> this</p>
<dd> This method is triggered when a tied hash is about to go out of scope. You don&#8217;t really need it unless you&#8217;re trying to add debugging or have auxiliary state to clean up. Here&#8217;s a very simple function: </p>
<p>sub DESTROY<br />
{<br />
    carp &amp;whowasi if $DEBUG;<br />
}
</dl>
<p> Note that functions such as <code>keys()</code> and <code>values()</code> may return huge lists when used on large objects, like <font SIZE="-1">DBM</font> files. You may prefer to use the <code>each()</code> function to iterate over such. Example: </p>
<p>#print out history file offsets<br />
use NDBM_File;<br />
tie(% HIST, &#8216;NDBM_File&#8217;, &#8216;/usr/lib/news/history&#8217;, 1, 0);<br />
while (($key, $val) = each % HIST) {<br />
    print $key, &#8216; = &#8216;, unpack(&#8216;L&#8217;, $val), &#8220;
&#8221;;<br />
}<br />
untie(% HIST);</p>
<h3>Tying FileHandles</h3>
<p> This is partially implemented now. </p>
<p> A class implementing a tied filehandle should define the following methods: <font SIZE="-1">TIEHANDLE,</font> at least one of <font SIZE="-1">PRINT, PRINTF, WRITE, READLINE, GETC, READ,</font> and possibly <font SIZE="-1">CLOSE, UNTIE</font> and <font SIZE="-1">DESTROY.</font> The class can also provide: <font SIZE="-1">BINMODE, OPEN, EOF, FILENO, SEEK, TELL</font> &#8211; if the corresponding perl operators are used on the handle. </p>
<p> When <font SIZE="-1">STDERR</font> is tied, its <font SIZE="-1">PRINT</font> method will be called to issue warnings and error messages. This feature is temporarily disabled during the call, which means you can use <tt>&quot;warn()&quot;</tt> inside <font SIZE="-1">PRINT</font> without starting a recursive loop. And just like <tt>&quot;__WARN__&quot;</tt> and <tt>&quot;__DIE__&quot;</tt> handlers, <font SIZE="-1">STDERR</font>&#8216;s <font SIZE="-1">PRINT</font> method may be called to report parser errors, so the caveats mentioned under &#8220;%SIG&#8221; in perlvar apply. </p>
<p> All of this is especially useful when perl is embedded in some other program, where output to <font SIZE="-1">STDOUT</font> and <font SIZE="-1">STDERR</font> may have to be redirected in some special way. See nvi and the Apache module for examples. </p>
<p> When tying a handle, the first argument to <tt>&quot;tie&quot;</tt> should begin with an asterisk. So, if you are tying <font SIZE="-1">STDOUT,</font> use <tt>*STDOUT</tt>. If you have assigned it to a scalar variable, say <tt>$handle</tt>, use <tt>*$handle</tt>. <tt>&quot;tie $handle&quot;</tt> ties the scalar variable <tt>$handle</tt>, not the handle inside it. </p>
<p> In our example we&#8217;re going to create a shouting handle. </p>
<pre>
    package Shout;
</pre>
<dl>
<dt><font SIZE="-1">TIEHANDLE</font> classname, <font SIZE="-1">LIST</font></p>
<dd> This is the constructor for the class. That means it is expected to return a blessed reference of some sort. The reference can be used to hold some internal information. </p>
<p>sub TIEHANDLE<br />
{<br />
    print &#8220;&lt;shout&gt;
&#8221;;<br />
    my $i;<br />
    bless \$i, shift<br />
}</p>
<dt><font SIZE="-1">WRITE</font> this, <font SIZE="-1">LIST</font></p>
<dd> This method will be called when the handle is written to via the <tt>&quot;syswrite&quot;</tt> function. </p>
<p>sub WRITE<br />
{<br />
    $r = shift;<br />
    my($buf, $len, $offset) = @_;<br />
    print &#8220;WRITE called, \$buf=$buf, \$len=$len, \$offset=$offset&#8221;;<br />
}</p>
<dt><font SIZE="-1">PRINT</font> this, <font SIZE="-1">LIST</font></p>
<dd> This method will be triggered every time the tied handle is printed to with the <tt>&quot;print()&quot;</tt> or <tt>&quot;say()&quot;</tt> functions. Beyond its self reference it also expects the list that was passed to the print function. </p>
<p>sub PRINT<br />
{<br />
    $r = shift;<br />
    $$r++;<br />
    print join($, , map(uc($_), @_)), $\<br />
}</p>
<p> <tt>&quot;say()&quot;</tt> acts just like <tt>&quot;print()&quot;</tt> except $\ will be localized to <tt>&quot;
&quot;</tt> so you need do nothing special to handle <tt>&quot;say()&quot;</tt> in <tt>&quot;PRINT()&quot;</tt>.</p>
<dt><font SIZE="-1">PRINTF</font> this, <font SIZE="-1">LIST</font></p>
<dd> This method will be triggered every time the tied handle is printed to with the <tt>&quot;printf()&quot;</tt> function. Beyond its self reference it also expects the format and list that was passed to the printf function. </p>
<p>sub PRINTF<br />
{<br />
    shift;<br />
    my $fmt = shift;<br />
    print sprintf($fmt, @_);<br />
}</p>
<dt><font SIZE="-1">READ</font> this, <font SIZE="-1">LIST</font></p>
<dd> This method will be called when the handle is read from via the <tt>&quot;read&quot;</tt> or <tt>&quot;sysread&quot;</tt> functions. </p>
<p>sub READ<br />
{<br />
    my $self = shift;<br />
    my $bufref = \$_[0];<br />
    my(undef, $len, $offset) = @_;<br />
    print &#8220;READ called, \$buf=$bufref, \$len=$len, \$offset=$offset&#8221;;<br />
#add to $$bufref, set $len to number of characters read<br />
    $len;<br />
}</p>
<dt><font SIZE="-1">READLINE</font> this</p>
<dd> This method is called when the handle is read via <tt>&quot;&lt;HANDLE&gt;&quot;</tt> or <tt>&quot;readline HANDLE&quot;</tt>. </p>
<p> As per <tt>&quot;readline&quot;</tt>, in scalar context it should return the next line, or <tt>&quot;undef&quot;</tt> for no more data. In list context it should return all remaining lines, or an empty list for no more data. The strings returned should include the input record separator <tt>$/</tt> (see perlvar), unless it is <tt>&quot;undef&quot;</tt> (which means &#8220;slurp&#8221; mode). </p>
<p>sub READLINE<br />
{<br />
    my $r = shift;<br />
    if (wantarray) {<br />
        return (&#8220;all remaining
&#8221;,<br />
                &#8220;lines up
&#8221;,<br />
                &#8220;to eof
&#8221;);<br />
    } else {<br />
        return &#8220;READLINE called &#8220;.++$$r.&#8221; times
&#8221;;<br />
    }<br />
}</p>
<dt><font SIZE="-1">GETC</font> this</p>
<dd> This method will be called when the <tt>&quot;getc&quot;</tt> function is called. </p>
<p>sub GETC<br />
{<br />
    print &#8220;Don&#8217;t GETC, Get Perl&#8221;;<br />
    return &#8220;a&#8221;;<br />
}</p>
<dt><font SIZE="-1">EOF</font> this</p>
<dd> This method will be called when the <tt>&quot;eof&quot;</tt> function is called. </p>
<p> Starting with Perl 5.12, an additional integer parameter will be passed. It will be zero if <tt>&quot;eof&quot;</tt> is called without parameter; <tt>1</tt> if <tt>&quot;eof&quot;</tt> is given a filehandle as a parameter, e.g. <tt>&quot;eof(FH)&quot;</tt>; and <tt>2</tt> in the very special case that the tied filehandle is <tt>&quot;ARGV&quot;</tt> and <tt>&quot;eof&quot;</tt> is called with an empty parameter list, e.g. <tt>&quot;eof()&quot;</tt>. </p>
<pre>
    sub EOF { not length $stringbuf }
</pre>
<dt><font SIZE="-1">CLOSE</font> this</p>
<dd> This method will be called when the handle is closed via the <tt>&quot;close&quot;</tt> function. </p>
<pre>
    sub CLOSE { print &quot;CLOSE called.
&quot; }
</pre>
<dt><font SIZE="-1">UNTIE</font> this</p>
<dd> As with the other types of ties, this method will be called when <tt>&quot;untie&quot;</tt> happens. It may be appropriate to &#8220;auto <font SIZE="-1">CLOSE&#8221;</font> when this occurs. See &quot;The <tt>&quot;untie&quot;</tt> Gotcha&quot; below.</p>
<dt><font SIZE="-1">DESTROY</font> this</p>
<dd> As with the other types of ties, this method will be called when the tied handle is about to be destroyed. This is useful for debugging and possibly cleaning up. </p>
<pre>
    sub DESTROY { print &quot;&lt;/shout&gt;
&quot; }
</pre>
</dl>
<p> Here&#8217;s how to use our little example: </p>
<p>tie(*FOO, &#8216;Shout&#8217;);<br />
print FOO &#8220;hello
&#8221;;<br />
$a = 4;<br />
$b = 6;<br />
print FOO $a, &#8221; plus &#8220;, $b, &#8221; equals &#8220;, $a + $b, &#8220;
&#8221;;<br />
print&lt;FOO&gt;;</p>
<h3><font SIZE="-1">UNTIE</font> this</h3>
<p> You can define for all tie types an <font SIZE="-1">UNTIE</font> method that will be called at <code>untie()</code>. See &quot;The <tt>&quot;untie&quot;</tt> Gotcha&quot; below.</p>
<h3>The untie Gotcha</h3>
<p> If you intend making use of the object returned from either <code>tie()</code> or <code>tied()</code>, and if the tie&#8217;s target class defines a destructor, there is a subtle gotcha you <i>must</i> guard against. </p>
<p> As setup, consider this (admittedly rather contrived) example of a tie; all it does is use a file to keep a log of the values assigned to a scalar. </p>
<p>package Remember;<br />
use strict;<br />
use warnings;<br />
use IO::File;<br />
sub TIESCALAR<br />
{<br />
    my $class = shift;<br />
    my $filename = shift;<br />
    my $handle = IO::File-&gt;new (&#8220;&gt; $filename&#8221;) or die &#8220;Cannot open $filename: $!
&#8221;;<br />
    print $handle &#8220;The Start
&#8221;;<br />
    bless{FH = &gt; $handle, Value = &gt; 0}, $class;<br />
}<br />
sub FETCH<br />
{<br />
    my $self = shift;<br />
    return $self-&gt;{Value};<br />
}<br />
sub STORE<br />
{<br />
    my $self = shift;<br />
    my $value = shift;<br />
    my $handle = $self-&gt;{FH};<br />
    print $handle &#8220;$value
&#8221;;<br />
    $self-&gt;{Value} = $value;<br />
}<br />
sub DESTROY<br />
{<br />
    my $self = shift;<br />
    my $handle = $self-&gt;{FH};<br />
    print $handle &#8220;The End
&#8221;;<br />
    close $handle;<br />
}<br />
1;</p>
<p> Here is an example that makes use of this tie: </p>
<p>use strict;<br />
use Remember;<br />
my $fred;<br />
tie $fred, &#8216;Remember&#8217;, &#8216;myfile.txt&#8217;;<br />
$fred = 1;<br />
$fred = 4;<br />
$fred = 5;<br />
untie $fred;<br />
system &#8220;cat myfile.txt&#8221;;</p>
<p> This is the output when it is executed: </p>
<pre>
    The Start
    1
    4
    5
    The End
</pre>
<p> So far so good. Those of you who have been paying attention will have spotted that the tied object hasn&#8217;t been used so far. So lets add an extra method to the Remember class to allow comments to be included in the file; say, something like this: </p>
<p>sub comment<br />
{<br />
    my $self = shift;<br />
    my $text = shift;<br />
    my $handle = $self-&gt;{FH};<br />
    print $handle $text, &#8220;
&#8221;;<br />
}</p>
<p> And here is the previous example modified to use the <tt>&quot;comment&quot;</tt> method (which requires the tied object): </p>
<p>use strict;<br />
use Remember;<br />
my($fred, $x);<br />
$x = tie $fred, &#8216;Remember&#8217;, &#8216;myfile.txt&#8217;;<br />
$fred = 1;<br />
$fred = 4;<br />
comment $x &#8220;changing&#8230;&#8221;;<br />
$fred = 5;<br />
untie $fred;<br />
system &#8220;cat myfile.txt&#8221;;</p>
<p> When this code is executed there is no output. Here&#8217;s why: </p>
<p> When a variable is tied, it is associated with the object which is the return value of the <font SIZE="-1">TIESCALAR, TIEARRAY,</font> or <font SIZE="-1">TIEHASH</font> function. This object normally has only one reference, namely, the implicit reference from the tied variable. When <code>untie()</code> is called, that reference is destroyed. Then, as in the first example above, the object&#8217;s destructor (<font SIZE="-1">DESTROY</font>) is called, which is normal for objects that have no more valid references; and thus the file is closed. </p>
<p> In the second example, however, we have stored another reference to the tied object in <tt>$x</tt>. That means that when <code>untie()</code> gets called there will still be a valid reference to the object in existence, so the destructor is not called at that time, and thus the file is not closed. The reason there is no output is because the file buffers have not been flushed to disk. </p>
<p> Now that you know what the problem is, what can you do to avoid it? Prior to the introduction of the optional <font SIZE="-1">UNTIE</font> method the only way was the good old <tt>&quot;-w&quot;</tt> flag. Which will spot any instances where you call <code>untie()</code> and there are still valid references to the tied object. If the second script above this near the top <tt>&quot;use warnings 'untie'&quot;</tt> or was run with the <tt>&quot;-w&quot;</tt> flag, Perl prints this warning message: </p>
<pre>
    untie attempted while 1 inner references still exist
</pre>
<p> To get the script to work properly and silence the warning make sure there are no valid references to the tied object <i>before</i> <code>untie()</code> is called: </p>
<pre>
    undef $x;
    untie $fred;
</pre>
<p> Now that <font SIZE="-1">UNTIE</font> exists the class designer can decide which parts of the class functionality are really associated with <tt>&quot;untie&quot;</tt> and which with the object being destroyed. What makes sense for a given class depends on whether the inner references are being kept so that non-tie-related methods can be called on the object. But in most cases it probably makes sense to move the functionality that would have been in <font SIZE="-1">DESTROY</font> to the <font SIZE="-1">UNTIE</font> method. </p>
<p> If the <font SIZE="-1">UNTIE</font> method exists then the warning above does not occur. Instead the <font SIZE="-1">UNTIE</font> method is passed the count of &#8220;extra&#8221; references and can issue its own warning if appropriate. e.g. to replicate the no <font SIZE="-1">UNTIE</font> case this method can be used: </p>
<pre><code>
sub UNTIE
{
    my($obj, $count) = @_;
    carp "untie attempted while $count inner references still exist" if $count;
}
</code></pre>
<h2>SEE ALSO</h2>
<p> See DB_File or Config for some interesting <code>tie()</code> implementations. A good starting point for many <code>tie()</code> implementations is with one of the modules Tie::Scalar, Tie::Array, Tie::Hash, or Tie::Handle.</p>
<h2>BUGS</h2>
<p> The normal return provided by <tt>&quot;scalar(%hash)&quot;</tt> is not available. What this means is that using <tt>%tied_hash</tt> in boolean context doesn&#8217;t work right (currently this always tests false, regardless of whether the hash is empty or hash elements). [ This paragraph needs review in light of changes in 5.25 ] </p>
<p> Localizing tied arrays or hashes does not work. After exiting the scope the arrays or the hashes are not restored. </p>
<p> Counting the number of entries in a hash via <tt>&quot;scalar(keys(%hash))&quot;</tt> or <tt>&quot;scalar(values(%hash)&quot;</tt>) is inefficient since it needs to iterate through all the entries with <font SIZE="-1">FIRSTKEY/NEXTKEY.</font> </p>
<p> Tied hash/array slices cause multiple <font SIZE="-1">FETCH/STORE</font> pairs, there are no tie methods for slice operations. </p>
<p> You cannot easily tie a multilevel data structure (such as a hash of hashes) to a dbm file. The first problem is that all but <font SIZE="-1">GDBM</font> and Berkeley <font SIZE="-1">DB</font> have size limitations, but beyond that, you also have problems with how references are to be represented on disk. One module that does attempt to address this need is DBM::Deep. Check your nearest <font SIZE="-1">CPAN</font> site as described in perlmodlib for source code. Note that despite its name, DBM::Deep does not use dbm. Another earlier attempt at solving the problem is <font SIZE="-1">MLDBM,</font> which is also available on the <font SIZE="-1">CPAN,</font> but which has some fairly serious limitations. </p>
<p> Tied filehandles are still incomplete. <code>sysopen()</code>, <code>truncate()</code>, <code>flock()</code>, <code>fcntl()</code>, <code>stat()</code> and -X can&#8217;t currently be trapped.</p>
<h2>AUTHOR</h2>
<p> Tom Christiansen </p>
<p> <font SIZE="-1">TIEHANDLE</font> by Sven Verdoolaege &lt;<i>skimo [at] dns.ufsia.ac.be</i>&gt; and Doug MacEachern &lt;<i>dougm [at] osf.org</i>&gt; </p>
<p> <font SIZE="-1">UNTIE</font> by Nick Ing-Simmons &lt;<i>nick [at] ing-simmons.net</i>&gt; </p>
<p> <font SIZE="-1">SCALAR</font> by Tassilo von Parseval &lt;<i>tassilo.von.parseval [at] rwth-aachen.de</i>&gt; </p>
<p> Tying Arrays by Casey West &lt;<i>casey [at] geeknest.com</i>&gt; </p>
<h2>Index</h2>
<dt><a href="#lbAK">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAL">BUGS</a></p>
<dd>
<dt><a href="#lbAM">AUTHOR</a></p>
<dd></dl>
