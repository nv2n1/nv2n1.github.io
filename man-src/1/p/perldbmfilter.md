---

title: "perldbmfilter(1)"
name: "perldbmfilter"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perldbmfilter/"
description: "perldbmfilter – Perl DBM Filters"
---

<p> perldbmfilter &#8211; Perl DBM Filters </p>
<h2>SYNOPSIS</h2>
<pre><code>
$db = tie % hash, 'DBM', ... $old_filter = $db-&gt;filter_store_key(sub{...});
$old_filter = $db-&gt;filter_store_value(sub{...});
$old_filter = $db-&gt;filter_fetch_key(sub{...});
$old_filter = $db-&gt;filter_fetch_value(sub{...});
</code></pre>
<h2>DESCRIPTION</h2>
<p> The four <tt>&quot;filter_*&quot;</tt> methods shown above are available in all the <font SIZE="-1">DBM</font> modules that ship with Perl, namely DB_File, GDBM_File, NDBM_File, ODBM_File and SDBM_File. </p>
<p> Each of the methods works identically, and is used to install (or uninstall) a single <font SIZE="-1">DBM</font> Filter. The only difference between them is the place that the filter is installed. </p>
<p> To summarise:</p>
<dl>
<dt><code>filter_store_key</code></dt>
<dd> If a filter has been installed with this method, it will be invoked every time you write a key to a <font SIZE="-1">DBM</font> database.</dd>
<dt><code>filter_store_value</code></dt>
<dd> If a filter has been installed with this method, it will be invoked every time you write a value to a <font SIZE="-1">DBM</font> database.</dd>
<dt><code>filter_fetch_key</code></dt>
<dd> If a filter has been installed with this method, it will be invoked every time you read a key from a <font SIZE="-1">DBM</font> database.</dd>
<dt><code>filter_fetch_value</code></dt>
<dd> If a filter has been installed with this method, it will be invoked every time you read a value from a <font SIZE="-1">DBM</font> database.</dd></dl>
<p> You can use any combination of the methods from none to all four. </p>
<p> All filter methods return the existing filter, if present, or <tt>&quot;undef&quot;</tt> if not. </p>
<p> To delete a filter pass <tt>&quot;undef&quot;</tt> to it.</p>
<h3>The Filter</h3>
<p> When each filter is called by Perl, a local copy of <tt>$_</tt> will contain the key or value to be filtered. Filtering is achieved by modifying the contents of <tt>$_</tt>. The return code from the filter is ignored.</p>
<h3>An Example: the <font SIZE="-1">NULL</font> termination problem.</h3>
<p> <font SIZE="-1">DBM</font> Filters are useful for a class of problems where you <i>always</i> want to make the same transformation to all keys, all values or both. </p>
<p> For example, consider the following scenario. You have a <font SIZE="-1">DBM</font> database that you need to share with a third-party C application. The C application assumes that <i>all</i> keys and values are <font SIZE="-1">NULL</font> terminated. Unfortunately when Perl writes to <font SIZE="-1">DBM</font> databases it doesn&#8217;t use <font SIZE="-1">NULL</font> termination, so your Perl application will have to manage <font SIZE="-1">NULL</font> termination itself. When you write to the database you will have to use something like this: </p>
<pre>
    $hash{&quot;$key\0&quot;} = &quot;$value\0&quot;;
</code></pre>
<p> Similarly the <font SIZE="-1">NULL</font> needs to be taken into account when you are considering the length of existing keys/values. </p>
<p> It would be much better if you could ignore the <font SIZE="-1">NULL</font> terminations issue in the main application code and have a mechanism that automatically added the terminating <font SIZE="-1">NULL</font> to all keys and values whenever you write to the database and have them removed when you read from the database. As I&#8217;m sure you have already guessed, this is a problem that <font SIZE="-1">DBM</font> Filters can fix very easily. </p>
<pre><code>    use strict;
    use warnings;
    use SDBM_File;
    use Fcntl;
    my %hash;
    my $filename = &quot;filt&quot;;
    unlink $filename;
    my $db = tie(%hash, 'SDBM_File', $filename, O_RDWR|O_CREAT, 0640)
      or die &quot;Cannot open $filename: $!\n&quot;;
    # Install DBM Filters
    $db-&gt;filter_fetch_key ( sub { s/\0$// } );
    $db-&gt;filter_store_key ( sub { $_ .= &quot;\0&quot; } );
    $db-&gt;filter_fetch_value(
        sub { no warnings 'uninitialized'; s/\0$// } );
    $db-&gt;filter_store_value( sub { $_ .= &quot;\0&quot; } );
    $hash{&quot;abc&quot;} = &quot;def&quot;;
    my $a = $hash{&quot;ABC&quot;};
    # ...
    undef $db;
    untie %hash;
</code></pre>
<p> The code above uses SDBM_File, but it will work with any of the <font SIZE="-1">DBM</font> modules. </p>
<p> Hopefully the contents of each of the filters should be self-explanatory. Both ``fetch&#8217;&#8216; filters remove the terminating <font SIZE="-1">NULL,</font> and both ``store&#8217;&#8216; filters add a terminating <font SIZE="-1">NULL.</font>  </p>
<h3>Another Example: Key is a C int.</h3>
<p> Here is another real-life example. By default, whenever Perl writes to a <font SIZE="-1">DBM</font> database it always writes the key and value as strings. So when you use this: </p>
<pre><code>    $hash{12345} = &quot;something&quot;;
</code></pre>
<p> the key 12345 will get stored in the <font SIZE="-1">DBM</font> database as the 5 byte string ``12345&#8217;&#8216;. If you actually want the key to be stored in the <font SIZE="-1">DBM</font> database as a C int, you will have to use <code>&quot;pack&quot;</code> when writing, and <code>&quot;unpack&quot;</code> when reading. </p>
<p> Here is a <font SIZE="-1">DBM</font> Filter that does it: </p>
<pre><code>    use strict;
    use warnings;
    use DB_File;
    my %hash;
    my $filename = &quot;filt&quot;;
    unlink $filename;
    my $db = tie %hash, 'DB_File', $filename, O_CREAT|O_RDWR, 0666,
        $DB_HASH or die &quot;Cannot open $filename: $!\n&quot;;
    $db-&gt;filter_fetch_key ( sub { $_ = unpack(&quot;i&quot;, $_) } );
    $db-&gt;filter_store_key ( sub { $_ = pack (&quot;i&quot;, $_) } );
    $hash{123} = &quot;def&quot;;
    # ...
    undef $db;
    untie %hash;
</code></pre>
<p> The code above uses DB_File, but again it will work with any of the <font SIZE="-1">DBM</font> modules. </p>
<p> This time only two filters have been used; we only need to manipulate the contents of the key, so it wasn&#8217;t necessary to install any value filters.  </p>
<h2>SEE ALSO</h2>
<p> DB_File, GDBM_File, NDBM_File, ODBM_File and SDBM_File.  </p>
<h2>AUTHOR</h2>
<p> Paul Marquess </p>
