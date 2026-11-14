---
title: "libsolv-bindings(3)"
name: "libsolv-bindings"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libsolv-bindings/"
description: "libsolv-bindings – access libsolv from perl/python/ruby"
---

<h2 class="name">NAME</h2>
<p> libsolv-bindings &#8211; access libsolv from perl/python/ruby </p>
<h2>DESCRIPTION</h2>
<p> Libsolv&#8217;s language bindings offer an abstract, object orientated interface to the library. The supported languages are currently perl, python, and ruby. All example code (except in the specifics sections, of course) lists first the &#8220;C-ish&#8221; interface, then the syntax for perl, python, and ruby (in that order).</p>
<h2>PERL SPECIFICS</h2>
<p> Libsolv&#8217;s perl bindings can be loaded with the following statement: </p>
<dl>
<dt>
<dd>
<pre>
<code>use solv</code>;
</pre>
</dl>
<p> Objects are either created by calling the new() method on a class or they are returned by calling methods on other objects. </p>
<dl>
<dt>
<dd>
<pre><code>
my $pool = solv::Pool-&gt;new ();
my $repo = $pool-&gt;add_repo("my_first_repo");
</code></pre>
</dl>
<p> Swig encapsulates all objects as tied hashes, thus the attributes can be accessed by treating the object as standard hash reference: </p>
<dl>
<dt>
<dd>
$pool-&gt;{appdata} = 42;<br />
printf &#8220;appdata is %d
&#8221;, $pool-&gt;{appdata};
</dl>
<p> A special exception to this are iterator objects, they are encapsulated as tied arrays so that it is possible to iterate with a for() statement: </p>
<dl>
<dt>
<dd>
my $iter = $pool-&gt;solvables_iter();<br />
for<br />
    my $solvable(@$iter){&#8230;};
</dl>
<p> As a downside of this approach, iterator objects cannot have attributes. </p>
<p> If an array needs to be passed to a method it is usually done by reference, if a method returns an array it returns it on the stack: </p>
<dl>
<dt>
<dd>
my @problems = $solver-&gt;solve(\@jobs);
</dl>
<p> Due to a bug in swig, stringification does not work for libsolv&#8217;s objects. Instead, you have to call the object&#8217;s str() method. </p>
<dl>
<dt>
<dd>
<pre>
<code>print</code> <i>$dep</i><code>-&gt;str() . &quot;\</code><i>n</i><code>&quot;</code>;
</pre>
</dl>
<p> Swig implements all constants as numeric variables (instead of the more natural constant subs), so don&#8217;t forget the leading &#8220;$&#8221; when accessing a constant. Also do not forget to prepend the namespace of the constant: </p>
<dl>
<dt>
<dd>
$pool-&gt;set_flag($solv::Pool::POOL_FLAG_OBSOLETEUSESCOLORS, 1);
</dl>
<h2>PYTHON SPECIFICS</h2>
<p> The python bindings can be loaded with: </p>
<dl>
<dt>
<dd>
<pre>
<code>import solv</code>
</pre>
</dl>
<p> Objects are either created by calling the constructor method for a class or they are returned by calling methods on other objects. </p>
<dl>
<dt>
<dd>
<pre>
<i>pool</i> <code>= solv.Pool()</code>
<i>repo</i> <code>=</code> <i>pool</i><code>.add_repo(&quot;my_first_repo&quot;)</code>
</pre>
</dl>
<p> Attributes can be accessed as usual: </p>
<dl>
<dt>
<dd>
<pre>
<i>pool</i><code>.appdata = 42</code>
<code>print &quot;appdata is %d&quot; % (</code><i>pool</i><code>.appdata)</code>
</pre>
</dl>
<p> Iterators also work as expected: </p>
<dl>
<dt>
<dd>
<pre>
<code>for</code> <i>solvable</i> <code>in</code> <i>pool</i><code>.solvables_iter():</code>
</pre>
</dl>
<p> Arrays are passed and returned as list objects: </p>
<dl>
<dt>
<dd>
<pre>
<i>jobs</i> <code>= []</code>
<i>problems</i> <code>=</code> <i>solver</i><code>.solve(</code><i>jobs</i><code>)</code>
</pre>
</dl>
<p> The bindings define stringification for many classes, some also have a <i>repr</i> method to ease debugging. </p>
<dl>
<dt>
<dd>
<pre>
<code>print</code> <i>dep</i>
<code>print repr(</code><i>repo</i><code>)</code>
</pre>
</dl>
<p> Constants are attributes of the classes: </p>
<dl>
<dt>
<dd>
<pre>
<i>pool</i><code>.set_flag(solv.Pool.POOL_FLAG_OBSOLETEUSESCOLORS, 1)</code>;
</pre>
</dl>
<h2>RUBY SPECIFICS</h2>
<p> The ruby bindings can be loaded with: </p>
<dl>
<dt>
<dd>
<pre>
<code>require 'solv'</code>
</pre>
</dl>
<p> Objects are either created by calling the new method on a class or they are returned by calling methods on other objects. Note that all classes start with an uppercase letter in ruby, so the class is called &#8220;Solv&#8221;. </p>
<dl>
<dt>
<dd>
<pre>
<i>pool</i> <code>= Solv::Pool.new</code>
<i>repo</i> <code>=</code> <i>pool</i><code>.add_repo(&quot;my_first_repo&quot;)</code>
</pre>
</dl>
<p> Attributes can be accessed as usual: </p>
<dl>
<dt>
<dd>
<pre>
<i>pool</i><code>.appdata = 42</code>
<code>puts &quot;appdata is #{</code><i>pool</i><code>.appdata}&quot;</code>
</pre>
</dl>
<p> Iterators also work as expected: </p>
<dl>
<dt>
<dd>
<pre>
<code>for</code> <i>solvable</i> <code>in</code> <i>pool</i><code>.solvables_iter() do ...</code>
</pre>
</dl>
<p> Arrays are passed and returned as array objects: </p>
<dl>
<dt>
<dd>
<pre>
<i>jobs</i> <code>= []</code>
<i>problems</i> <code>=</code> <i>solver</i><code>.solve(</code><i>jobs</i><code>)</code>
</pre>
</dl>
<p> Most classes define a to_s method, so objects can be easily stringified. Many also define an inspect() method. </p>
<dl>
<dt>
<dd>
<pre>
<code>puts</code> <i>dep</i>
<code>puts</code> <i>repo</i><code>.inspect</code>
</pre>
</dl>
<p> Constants live in the namespace of the class they belong to: </p>
<dl>
<dt>
<dd>
<pre>
<i>pool</i><code>.set_flag(Solv::Pool::POOL_FLAG_OBSOLETEUSESCOLORS, 1)</code>;
</pre>
</dl>
<p> Note that boolean methods have an added trailing &#8220;?&#8221;, to be consistent with other ruby modules: </p>
<dl>
<dt>
<dd>
<pre>
<code>puts &quot;empty&quot; if</code> <i>repo</i><code>.isempty?</code>
</pre>
</dl>
<h2>TCL SPECIFICS</h2>
<p> Libsolv&#8217;s tcl bindings can be loaded with the following statement: </p>
<dl>
<dt>
<dd>
<pre>
<code>package require solv</code>
</pre>
</dl>
<p> Objects are either created by calling class name prefixed with &#8220;new_&#8221;, or they are returned by calling methods on other objects. </p>
<dl>
<dt>
<dd>
set pool[solv::new_Pool] set repo[$pool add_repo &#8220;my_first_repo&#8221;]
</dl>
<p> Swig provides a &#8220;cget&#8221; method to read object attributes, and a &#8220;configure&#8221; method to write them: </p>
<dl>
<dt>
<dd>
<pre>
<i>$pool</i> <code>configure -appdata 42</code>
<code>puts &quot;appdata is [</code><i>$pool</i> <code>cget -appdata]&quot;</code>
</pre>
</dl>
<p> The tcl bindings provide a little helper to work with iterators in a foreach style: </p>
<dl>
<dt>
<dd>
set iter[$pool solvables_iter] solv::iter s $iter<br />
{<br />
    &#8230;<br />
}
</dl>
<p> libsolv&#8217;s arrays are mapped to tcl&#8217;s lists: </p>
<dl>
<dt>
<dd>
set jobs[list $job1 $job2] set problems[$solver solve $jobs] puts &#8220;We have [llength $problems] problems&#8230;&#8221;
</dl>
<p> Stringification is done by calling the object&#8217;s &#8220;str&#8221; method. </p>
<dl>
<dt>
<dd>
<pre>
<code>puts [</code><i>$dep</i> <code>str]</code>
</pre>
</dl>
<p> There is one exception: you have to use &#8220;stringify&#8221; for Datamatch objects, as swig reports a clash with the &#8220;str&#8221; attribute. Some objects also support a &#8220;==&#8221; method for equality tests, and a &#8220;!=&#8221; method. </p>
<p> Swig implements all constants as numeric variables, constants belonging to a libsolv class are prefixed with the class name: </p>
<dl>
<dt>
<dd>
<pre>
<i>$pool</i> <code>set_flag</code> <i>$solv::Pool_POOL_FLAG_OBSOLETEUSESCOLORS</i>  <code>1</code>
<code>puts [</code><i>$solvable</i> <code>lookup_str</code> <i>$solv::SOLVABLE_SUMMARY</i><code>]</code>
</pre>
</dl>
<h2>THE SOLV CLASS</h2>
<p> This is the main namespace of the library, you cannot create objects of this type but it contains some useful constants.</p>
<h3>CONSTANTS</h3>
<p> Relational flag constants, the first three can be or-ed together </p>
<p> <code>REL_LT</code></p>
<dl>
<dt>
<dd> the &#8220;less than&#8221; bit</dl>
<p> <code>REL_EQ</code></p>
<dl>
<dt>
<dd> the &#8220;equals to&#8221; bit</dl>
<p> <code>REL_GT</code></p>
<dl>
<dt>
<dd> the &#8220;greater than&#8221; bit</dl>
<p> <code>REL_ARCH</code></p>
<dl>
<dt>
<dd> used for relations that describe an extra architecture filter, the version part of the relation is interpreted as architecture.</dl>
<p> Special Solvable Ids </p>
<p> <code>SOLVID_META</code></p>
<dl>
<dt>
<dd> Access the meta section of a repository or repodata area. This is like an extra Solvable that has the Id SOLVID_META.</dl>
<p> <code>SOLVID_POS</code></p>
<dl>
<dt>
<dd> Use the data position stored inside of the pool instead of accessing some solvable by Id. The bindings have the Datapos objects as an abstraction mechanism, so you do not need this constant.</dl>
<p> Constant string Ids </p>
<p> <code>ID_NULL</code></p>
<dl>
<dt>
<dd> Always zero</dl>
<p> <code>ID_EMPTY</code></p>
<dl>
<dt>
<dd> Always one, describes the empty string</dl>
<p> <code>SOLVABLE_NAME</code></p>
<dl>
<dt>
<dd> The keyname Id of the name of the solvable.</dl>
<p> <code>&#8230;</code></p>
<dl>
<dt>
<dd> see the libsolv-constantids manpage for a list of fixed Ids.</dl>
<h2>THE POOL CLASS</h2>
<p> The pool is libsolv&#8217;s central resource manager. A pool consists of Solvables, Repositories, Dependencies, each indexed by Ids.</p>
<h3>CLASS METHODS</h3>
<dl>
<dt>
<dd>
Pool *Pool()<br />
    my $pool = solv::Pool-&gt;new ();<br />
pool = solv.Pool()<br />
           pool = Solv::Pool.new()
</dl>
<p> Create a new pool instance. In most cases you just need one pool. Note that the returned object &quot;owns&quot; the pool, i.e. if the object is freed, the pool is also freed. You can use the disown method to break this ownership relation.</p>
<h3>ATTRIBUTES</h3>
<dl>
<dt>
<dd>
void *appdata; /* read/write */<br />
$pool-&gt;{appdata} pool.appdata<br />
    pool.appdata
</dl>
<p> Application specific data that may be used in any way by the code using the pool. </p>
<dl>
<dt>
<dd>
Solvable solvables[]; /* read only */<br />
my $solvable = $pool-&gt;<br />
{<br />
    solvables<br />
    } -&gt; [$solvid];<br />
solvable = pool.solvables[solvid] solvable = pool.solvables[solvid]
</dl>
<p> Look up a Solvable by its id. </p>
<dl>
<dt>
<dd>
Repo repos[]; /* read only */<br />
my $repo = $pool-&gt;<br />
{<br />
    repos<br />
    } -&gt; [$repoid];<br />
repo = pool.repos[repoid] repo = pool.repos[repoid]
</dl>
<p> Look up a Repository by its id. </p>
<dl>
<dt>
<dd>
Repo *installed; /* read/write */<br />
$pool-&gt;{installed} = $repo;<br />
pool.installed = repo<br />
                     pool.installed = repo
</dl>
<p> Define which repository contains all the installed packages. </p>
<dl>
<dt>
<dd>
const char *errstr; /* read only */<br />
my $err = $pool-&gt;{errstr};<br />
err = pool.errstr<br />
          err = pool.errstr
</dl>
<p> Return the last error string that was stored in the pool.</p>
<h3>CONSTANTS</h3>
<p> <code>POOL_FLAG_PROMOTEEPOCH</code></p>
<dl>
<dt>
<dd> Promote the epoch of the providing dependency to the requesting dependency if it does not contain an epoch. Used at some time in old rpm versions, modern systems should never need this.</dl>
<p> <code>POOL_FLAG_FORBIDSELFCONFLICTS</code></p>
<dl>
<dt>
<dd> Disallow the installation of packages that conflict with themselves. Debian always allows self-conflicting packages, rpm used to forbid them but switched to also allowing them recently.</dl>
<p> <code>POOL_FLAG_OBSOLETEUSESPROVIDES</code></p>
<dl>
<dt>
<dd> Make obsolete type dependency match against provides instead of just the name and version of packages. Very old versions of rpm used the name/version, then it got switched to provides and later switched back again to just name/version.</dl>
<p> <code>POOL_FLAG_IMPLICITOBSOLETEUSESPROVIDES</code></p>
<dl>
<dt>
<dd> An implicit obsoletes is the internal mechanism to remove the old package on an update. The default is to remove all packages with the same name, rpm-5 switched to also removing packages providing the same name.</dl>
<p> <code>POOL_FLAG_OBSOLETEUSESCOLORS</code></p>
<dl>
<dt>
<dd> Rpm&#8217;s multilib implementation (used in RedHat and Fedora) distinguishes between 32bit and 64bit packages (the terminology is that they have a different color). If obsoleteusescolors is set, packages with different colors will not obsolete each other.</dl>
<p> <code>POOL_FLAG_IMPLICITOBSOLETEUSESCOLORS</code></p>
<dl>
<dt>
<dd> Same as POOL_FLAG_OBSOLETEUSESCOLORS, but used to find out if packages of the same name can be installed in parallel. For current Fedora systems, POOL_FLAG_OBSOLETEUSESCOLORS should be false and POOL_FLAG_IMPLICITOBSOLETEUSESCOLORS should be true (this is the default if FEDORA is defined when libsolv is compiled).</dl>
<p> <code>POOL_FLAG_NOINSTALLEDOBSOLETES</code></p>
<dl>
<dt>
<dd> New versions of rpm consider the obsoletes of installed packages when checking for dependency, thus you may not install a package that is obsoleted by some other installed package, unless you also erase the other package.</dl>
<p> <code>POOL_FLAG_HAVEDISTEPOCH</code></p>
<dl>
<dt>
<dd> Mandriva added a new field called distepoch that gets checked in version comparison if the epoch/version/release of two packages are the same.</dl>
<p> <code>POOL_FLAG_NOOBSOLETESMULTIVERSION</code></p>
<dl>
<dt>
<dd> If a package is installed in multiversionmode, rpm used to ignore both the implicit obsoletes and the obsolete dependency of a package. This was changed to ignoring just the implicit obsoletes, thus you may install multiple versions of the same name, but obsoleted packages still get removed.</dl>
<p> <code>POOL_FLAG_ADDFILEPROVIDESFILTERED</code></p>
<dl>
<dt>
<dd> Make the addfileprovides method only add files from the standard locations (i.e. the &#8220;bin&#8221; and &#8220;etc&#8221; directories). This is useful if you have only few packages that use non-standard file dependencies, but you still want the fast speed that addfileprovides() generates.</dl>
<h3>METHODS</h3>
<dl>
<dt>
<dd>
void free()<br />
    $pool-&gt;free();<br />
pool.free()<br />
    pool.free()
</dl>
<p> Force a free of the pool. After this call, you must not access any object that still references the pool. </p>
<dl>
<dt>
<dd>
void disown()<br />
    $pool-&gt;disown();<br />
pool.disown()<br />
    pool.disown()
</dl>
<p> Break the ownership relation between the binding object and the pool. After this call, the pool will not get freed even if the object goes out of scope. This also means that you must manually call the free method to free the pool data. </p>
<dl>
<dt>
<dd>
void setdebuglevel(int level)<br />
    $pool-&gt;setdebuglevel($level);<br />
pool.setdebuglevel(level)<br />
    pool.setdebuglevel(level)
</dl>
<p> Set the debug level. A value of zero means no debug output, the higher the value, the more output is generated. </p>
<dl>
<dt>
<dd>
int set_flag(int flag, int value)<br />
    my $oldvalue = $pool-&gt;set_flag($flag, $value);<br />
oldvalue = pool.set_flag(flag, value)<br />
               oldvalue = pool.set_flag(flag, value)
</dl>
<dl>
<dt>
<dd>
int get_flag(int flag)<br />
    my $value = $pool-&gt;get_flag($flag);<br />
value = pool.get_flag(flag)<br />
            value = pool.get_flag(flag)
</dl>
<p> Set/get a pool specific flag. The flags define how the system works, e.g. how the package manager treats obsoletes. The default flags should be sane for most applications, but in some cases you may want to tweak a flag, for example if you want to solv package dependencies for some other system than yours. </p>
<dl>
<dt>
<dd>
void set_rootdir(const char *rootdir)<br />
    $pool-&gt;set_rootdir(rootdir);<br />
pool.set_rootdir(rootdir)<br />
    pool.set_rootdir(rootdir)
</dl>
<dl>
<dt>
<dd>
const char *get_rootdir()<br />
    my $rootdir = $pool-&gt;get_rootdir();<br />
rootdir = pool.get_rootdir()<br />
              rootdir = pool.get_rootdir()
</dl>
<p> Set/get the rootdir to use. This is useful if you want package management to work only in some directory, for example if you want to setup a chroot jail. Note that the rootdir will only be prepended to file paths if the <code>REPO_USE_ROOTDIR</code> flag is used. </p>
<dl>
<dt>
<dd>
void setarch(const char *arch = 0)<br />
    $pool-&gt;setarch();<br />
pool.setarch()<br />
    pool.setarch()
</dl>
<p> Set the architecture for your system. The architecture is used to determine which packages are installable. It defaults to the result of &#8220;uname -m&#8221;. </p>
<dl>
<dt>
<dd>
Repo add_repo(const char *name)<br />
    $repo = $pool-&gt;add_repo($name);<br />
repo = pool.add_repo(name)<br />
           repo = pool.add_repo(name)
</dl>
<p> Add a Repository with the specified name to the pool. The repository is empty on creation, use the repository methods to populate it with packages. </p>
<dl>
<dt>
<dd>
Repoiterator repos_iter()<br />
for my $repo (@{$pool-&gt;repos_iter()})<br />
for repo in pool.repos_iter():<br />
for repo in pool.repos_iter()
</dl>
<p> Iterate over the existing repositories. </p>
<dl>
<dt>
<dd>
Solvableiterator solvables_iter()<br />
for my $solvable (@{$pool-&gt;solvables_iter()})<br />
for solvable in pool.solvables_iter():<br />
for solvable in pool.solvables_iter()
</dl>
<p> Iterate over the existing solvables. </p>
<dl>
<dt>
<dd>
Dep Dep(const char *str, bool create = 1)<br />
    my $dep = $pool-&gt;Dep($string);<br />
dep = pool.Dep(string)<br />
          dep = pool.Dep(string)
</dl>
<p> Create an object describing a string or dependency. If the string is currently not in the pool and <i>create</i> is false, <code>undef</code>/<code>None</code>/<code>nil</code> is returned. </p>
<dl>
<dt>
<dd>
void addfileprovides()<br />
    $pool-&gt;addfileprovides();<br />
pool.addfileprovides()<br />
    pool.addfileprovides()
</dl>
<dl>
<dt>
<dd>
Id *addfileprovides_queue()<br />
    my @ids = $pool-&gt;addfileprovides_queue();<br />
ids = pool.addfileprovides_queue()<br />
          ids = pool.addfileprovides_queue()
</dl>
<p> Some package managers like rpm allow dependencies on files contained in other packages. To allow libsolv to deal with those dependencies in an efficient way, you need to call the addfileprovides method after creating and reading all repositories. This method will scan all dependency for file names and then scan all packages for matching files. If a filename has been matched, it will be added to the provides list of the corresponding package. The addfileprovides_queue variant works the same way but returns an array containing all file dependencies. This information can be stored in the meta section of the repositories to speed up the next time the repository is loaded and addfileprovides is called. </p>
<dl>
<dt>
<dd>
void createwhatprovides()<br />
    $pool-&gt;createwhatprovides();<br />
pool.createwhatprovides()<br />
    pool.createwhatprovides()
</dl>
<p> Create the internal &#8220;whatprovides&#8221; hash over all of the provides of all packages. This method must be called before doing any lookups on provides. It&#8217;s encouraged to do it right after all repos are set up, usually right after the call to addfileprovides(). </p>
<dl>
<dt>
<dd>
Solvable *whatprovides(DepId dep)<br />
    my @solvables = $pool-&gt;whatprovides($dep);<br />
solvables = pool.whatprovides(dep)<br />
                solvables = pool.whatprovides(dep)
</dl>
<p> Return all solvables that provide the specified dependency. You can use either a Dep object or a simple Id as argument. </p>
<dl>
<dt>
<dd>
Id *matchprovidingids(const char *match, int flags)<br />
    my @ids = $pool-&gt;matchprovidingids($match, $flags);<br />
ids = pool.matchprovidingids(match, flags)<br />
          ids = pool.matchprovidingids(match, flags)
</dl>
<p> Search the names of all provides and return the ones matching the specified string. See the Dataiterator class for the allowed flags. </p>
<dl>
<dt>
<dd>
Id towhatprovides(Id *ids)<br />
    my $offset = $pool-&gt;towhatprovides(\@ids);<br />
offset = pool.towhatprovides(ids)<br />
             offset = pool.towhatprovides(ids)
</dl>
<p> &#8220;Internalize&#8221; an array containing Ids. The returned value can be used to create solver jobs working on a specific set of packages. See the Solver class for more information. </p>
<dl>
<dt>
<dd>
bool isknownarch(DepId id)<br />
    my $bool = $pool-&gt;isknownarch($id);<br />
bool = pool.isknownarch(id) bool = pool.isknownarch ? (id)
</dl>
<p> Return true if the specified Id describes a known architecture. </p>
<dl>
<dt>
<dd>
Solver Solver()<br />
    my $solver = $pool-&gt;Solver();<br />
solver = pool.Solver()<br />
             solver = pool.Solver()
</dl>
<p> Create a new solver object. </p>
<dl>
<dt>
<dd>
Job Job(int how, Id what)<br />
    my $job = $pool-&gt;Job($how, $what);<br />
job = pool.Job(how, what)<br />
          job = pool.Job(how, what)
</dl>
<p> Create a new Job object. Kind of low level, in most cases you would use a Selection or Dep job constructor instead. </p>
<dl>
<dt>
<dd>
Selection Selection()<br />
    my $sel = $pool-&gt;Selection();<br />
sel = pool.Selection()<br />
          sel = pool.Selection()
</dl>
<p> Create an empty selection. Useful as a starting point for merging other selections. </p>
<dl>
<dt>
<dd>
Selection Selection_all()<br />
    my $sel = $pool-&gt;Selection_all();<br />
sel = pool.Selection_all()<br />
          sel = pool.Selection_all()
</dl>
<p> Create a selection containing all packages. Useful as starting point for intersecting other selections or for update/distupgrade jobs. </p>
<dl>
<dt>
<dd>
Selection select(const char *name, int flags)<br />
    my $sel = $pool-&gt;select($name, $flags);<br />
sel = pool.select(name, flags)<br />
          sel = pool.select(name, flags)
</dl>
<p> Create a selection by matching packages against the specified string. See the Selection class for a list of flags and how to create solver jobs from a selection. </p>
<dl>
<dt>
<dd>
void setpooljobs(Jobs *jobs)<br />
    $pool-&gt;setpooljobs(\@jobs);<br />
pool.setpooljobs(jobs)<br />
    pool.setpooljobs(jobs)
</dl>
<dl>
<dt>
<dd>
Job *getpooljobs()<br />
    @jobs = $pool-&gt;getpooljobs();<br />
jobs = pool.getpooljobs()<br />
           jobs = pool.getpooljobs()
</dl>
<p> Get/Set fixed jobs stored in the pool. Those jobs are automatically appended to all solver jobs, they are meant for fixed configurations like which packages can be multiversion installed, which packages were userinstalled or must not be erased. </p>
<dl>
<dt>
<dd>
void set_loadcallback(Callable *callback)<br />
    $pool-&gt;setloadcallback(\&amp;callbackfunction);<br />
pool.setloadcallback(callbackfunction)<br />
    pool.setloadcallback<br />
{<br />
    | repodata | &#8230;<br />
}
</dl>
<p> Set the callback function called when repository metadata needs to be loaded on demand. To make use of this feature, you need to create repodata stubs that tell the library which data is available but not loaded. If later on the data needs to be accessed, the callback function is called with a repodata argument. You can then load the data (maybe fetching it first from a remote server). The callback should return true if the data has been made available. </p>
<dl>
<dt>
<dd>
<pre>
/* bindings only */
<i>$pool</i><code>-&gt;appdata_disown()</code>
<i>pool</i><code>.appdata_disown()</code>
<i>pool</i><code>.appdata_disown()</code>
</pre>
</dl>
<p> Decrement the reference count of the appdata object. This can be used to break circular references (e.g. if the pool&#8217;s appdata value points to some meta data structure that contains a pool handle). If used incorrectly, this method can lead to application crashes, so beware. (This method is a no-op for ruby and tcl.)</p>
<h3>DATA RETRIEVAL METHODS</h3>
<p> In the following functions, the <i>keyname</i> argument describes what to retrieve. For the standard cases you can use the available Id constants. For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>$solv::SOLVABLE_SUMMARY</code>
<code>solv.SOLVABLE_SUMMARY</code>
<code>Solv::SOLVABLE_SUMMARY</code>
</pre>
</dl>
<p> selects the &#8220;Summary&#8221; entry of a solvable. The <i>solvid</i> argument selects the desired solvable by Id. </p>
<dl>
<dt>
<dd>
const char *lookup_str(Id solvid, Id keyname)<br />
    my $string = $pool-&gt;lookup_str($solvid, $keyname);<br />
string = pool.lookup_str(solvid, keyname)<br />
             string = pool.lookup_str(solvid, keyname)
</dl>
<dl>
<dt>
<dd>
Id lookup_id(Id solvid, Id keyname)<br />
    my $id = $pool-&gt;lookup_id($solvid, $keyname);<br />
id = pool.lookup_id(solvid, keyname)<br />
         id = pool.lookup_id(solvid, keyname)
</dl>
<dl>
<dt>
<dd>
unsigned long long lookup_num(Id solvid, Id keyname, unsigned long long notfound = 0)<br />
    my $num = $pool-&gt;lookup_num($solvid, $keyname);<br />
num = pool.lookup_num(solvid, keyname)<br />
          num = pool.lookup_num(solvid, keyname)
</dl>
<dl>
<dt>
<dd>
bool lookup_void(Id solvid, Id keyname)<br />
    my $bool = $pool-&gt;lookup_void($solvid, $keyname);<br />
bool = pool.lookup_void(solvid, keyname) bool = pool.lookup_void(solvid, keyname)
</dl>
<dl>
<dt>
<dd>
Id *lookup_idarray(Id solvid, Id keyname)<br />
    my @ids = $pool-&gt;lookup_idarray($solvid, $keyname);<br />
ids = pool.lookup_idarray(solvid, keyname)<br />
          ids = pool.lookup_idarray(solvid, keyname)
</dl>
<dl>
<dt>
<dd>
Chksum lookup_checksum(Id solvid, Id keyname)<br />
    my $chksum = $pool-&gt;lookup_checksum($solvid, $keyname);<br />
chksum = pool.lookup_checksum(solvid, keyname)<br />
             chksum = pool.lookup_checksum(solvid, keyname)
</dl>
<p> Lookup functions. Return the data element stored in the specified solvable. You should probably use the methods of the Solvable class instead. </p>
<dl>
<dt>
<dd>
Dataiterator Dataiterator(Id keyname, const char *match = 0, int flags = 0)<br />
    my $di = $pool-&gt;Dataiterator($keyname, $match, $flags);<br />
di = pool.Dataiterator(keyname, match, flags)<br />
         di = pool.Dataiterator(keyname, match, flags)
</dl>
<dl>
<dt>
<dd>
Dataiterator Dataiterator_solvid(Id solvid, Id keyname, const char *match = 0, int flags = 0)<br />
    my $di = $pool-&gt;Dataiterator($solvid, $keyname, $match, $flags);<br />
di = pool.Dataiterator(solvid, keyname, match, flags)<br />
         di = pool.Dataiterator(solvid, keyname, match, flags)
</dl>
<dl>
<dt>
<dd>
<pre>
<code>for my</code> <i>$d</i> <code>(</code><i>@$di</i><code>)</code>
<code>for</code> <i>d</i> <code>in</code> <i>di</i><code>:</code>
<code>for</code> <i>d</i> <code>in</code> <i>di</i>
</pre>
</dl>
<p> Iterate over the matching data elements. See the Dataiterator class for more information. The Dataiterator method iterates over all solvables in the pool, whereas the Dataiterator_solvid only iterates over the specified solvable.</p>
<h3>ID METHODS</h3>
<p> The following methods deal with Ids, i.e. integers representing objects in the pool. They are considered &#8220;low level&#8221;, in most cases you would not use them but instead the object orientated methods. </p>
<dl>
<dt>
<dd>
Repo id2repo(Id id)<br />
    $repo = $pool-&gt;id2repo($id);<br />
repo = pool.id2repo(id)<br />
           repo = pool.id2repo(id)
</dl>
<p> Lookup an existing Repository by id. You can also do this by using the <code>repos</code> attribute. </p>
<dl>
<dt>
<dd>
Solvable id2solvable(Id id)<br />
    $solvable = $pool-&gt;id2solvable($id);<br />
solvable = pool.id2solvable(id)<br />
               solvable = pool.id2solvable(id)
</dl>
<p> Lookup an existing Repository by id. You can also do this by using the <code>solvables</code> attribute. </p>
<dl>
<dt>
<dd>
const char *solvid2str(Id id)<br />
    my $str = $pool-&gt;solvid2str($id);<br />
str = pool.solvid2str(id)<br />
          str = pool.solvid2str(id)
</dl>
<p> Return a string describing the Solvable with the specified id. The string consists of the name, version, and architecture of the Solvable. </p>
<dl>
<dt>
<dd>
Id str2id(const char *str, bool create = 1)<br />
    my $id = pool-&gt;str2id($string);<br />
id = pool.str2id(string)<br />
         id = pool.str2id(string)
</dl>
<dl>
<dt>
<dd>
const char *id2str(Id id)<br />
    $string = pool-&gt;id2str($id);<br />
string = pool.id2str(id)<br />
             string = pool.id2str(id)
</dl>
<p> Convert a string into an Id and back. If the string is currently not in the pool and <i>create</i> is false, zero is returned. </p>
<dl>
<dt>
<dd>
Id rel2id(Id name, Id evr, int flags, bool create = 1)<br />
    my $id = pool-&gt;rel2id($nameid, $evrid, $flags);<br />
id = pool.rel2id(nameid, evrid, flags)<br />
         id = pool.rel2id(nameid, evrid, flags)
</dl>
<p> Create a &#8220;relational&#8221; dependency. Such dependencies consist of a name part, the <i>flags</i> describing the relation, and a version part. The flags are: </p>
<dl>
<dt>
<dd>
<pre>
<code>$solv::REL_EQ | $solv::REL_GT | $solv::REL_LT</code>
<code>solv.REL_EQ | solv.REL_GT | solv.REL_LT</code>
<code>Solv::REL_EQ | Solv::REL_GT | Solv::REL_LT</code>
</pre>
</dl>
<p> Thus, if you want a &#8220;&lt;=&#8221; relation, you would use <code>REL_LT | REL_EQ</code>. </p>
<dl>
<dt>
<dd>
Id id2langid(Id id, const char *lang, bool create = 1)<br />
    my $id = $pool-&gt;id2langid($id, $language);<br />
id = pool.id2langid(id, language)<br />
         id = pool.id2langid(id, language)
</dl>
<p> Create a language specific Id from some other id. This function simply converts the id into a string, appends a dot and the specified language to the string and converts the result back into an Id. </p>
<dl>
<dt>
<dd>
const char *dep2str(Id id)<br />
    $string = pool-&gt;dep2str($id);<br />
string = pool.dep2str(id)<br />
             string = pool.dep2str(id)
</dl>
<p> Convert a dependency id into a string. If the id is just a string, this function has the same effect as id2str(). For relational dependencies, the result is the correct &#8220;name relation evr&#8221; string.</p>
<h2>THE DEPENDENCY CLASS</h2>
<p> The dependency class is an object orientated way to work with strings and dependencies. Internally, dependencies are represented as Ids, i.e. simple numbers. Dependency objects can be constructed by using the Pool&#8217;s Dep() method.</p>
<h3>ATTRIBUTES</h3>
<dl>
<dt>
<dd>
Pool *pool; /* read only */<br />
$dep-&gt;{pool} dep.pool<br />
    dep.pool
</dl>
<p> Back reference to the pool this dependency belongs to. </p>
<dl>
<dt>
<dd>
Id id; /* read only */<br />
$dep-&gt;{id} dep.id<br />
    dep.id
</dl>
<p> The id of this dependency.</p>
<h2>METHODS</h2>
<dl>
<dt>
<dd>
Dep Rel(int flags, DepId evrid, bool create = 1)<br />
    my $reldep = $dep-&gt;Rel($flags, $evrdep);<br />
reldep = dep.Rel(flags, evrdep)<br />
             reldep = dep.Rel(flags, evrdep)
</dl>
<p> Create a relational dependency from to string dependencies and a flags argument. See the pool&#8217;s rel2id method for a description of the flags. </p>
<dl>
<dt>
<dd>
Selection Selection_name(int setflags = 0)<br />
    my $sel = $dep-&gt;Selection_name();<br />
sel = dep.Selection_name()<br />
          sel = dep.Selection_name()
</dl>
<p> Create a Selection from a dependency. The selection consists of all packages that have a name equal to the dependency. If the dependency is of a relational type, the packages version must also fulfill the dependency. </p>
<dl>
<dt>
<dd>
Selection Selection_provides(int setflags = 0)<br />
    my $sel = $dep-&gt;Selection_provides();<br />
sel = dep.Selection_provides()<br />
          sel = dep.Selection_provides()
</dl>
<p> Create a Selection from a dependency. The selection consists of all packages that have at least one provides matching the dependency. </p>
<dl>
<dt>
<dd>
const char *str()<br />
    my $str = $dep-&gt;str();<br />
str = $dep.str()<br />
          str = $dep.str()
</dl>
<p> Return a string describing the dependency. </p>
<dl>
<dt>
<dd>
<pre>
<code>&lt;stringification&gt;</code>
my <i>$str</i> <code>=</code> <i>$dep</i><code>-&gt;str</code>;
<i>str</i> <code>= str(</code><i>dep</i><code>)</code>
<i>str</i> <code>=</code> <i>dep</i><code>.to_s</code>
</pre>
</dl>
<p> Same as calling the str() method. </p>
<dl>
<dt>
<dd>
&lt;equality&gt;<br />
if ($dep1 == $dep2)<br />
if dep1 == dep2:<br />
if dep1 == dep2
</dl>
<p> The dependencies are equal if they are part of the same pool and have the same ids.</p>
<h2>THE REPOSITORY CLASS</h2>
<p> A Repository describes a group of packages, normally coming from the same source. Repositories are created by the Pool&#8217;s add_repo() method.</p>
<h3>ATTRIBUTES</h3>
<dl>
<dt>
<dd>
Pool *pool; /* read only */<br />
$repo-&gt;{pool} repo.pool<br />
    repo.pool
</dl>
<p> Back reference to the pool this dependency belongs to. </p>
<dl>
<dt>
<dd>
Id id; /* read only */<br />
$repo-&gt;{id} repo.id<br />
    repo.id
</dl>
<p> The id of the repository. </p>
<dl>
<dt>
<dd>
const char *name; /* read/write */<br />
$repo-&gt;{name} repo.name<br />
    repo.name
</dl>
<p> The repositories name. To libsolv, the name is just a string with no specific meaning. </p>
<dl>
<dt>
<dd>
int priority; /* read/write */<br />
$repo-&gt;{priority} repo.priority<br />
    repo.priority
</dl>
<p> The priority of the repository. A higher number means that packages of this repository will be chosen over other repositories, even if they have a greater package version. </p>
<dl>
<dt>
<dd>
int subpriority; /* read/write */<br />
$repo-&gt;{subpriority} repo.subpriority<br />
    repo.subpriority
</dl>
<p> The sub-priority of the repository. This value is compared when the priorities of two repositories are the same. It is useful to make the library prefer on-disk repositories to remote ones. </p>
<dl>
<dt>
<dd>
int nsolvables; /* read only */<br />
$repo-&gt;{nsolvables} repo.nsolvables<br />
    repo.nsolvables
</dl>
<p> The number of solvables in this repository. </p>
<dl>
<dt>
<dd>
void *appdata; /* read/write */<br />
$repo-&gt;{appdata} repo.appdata<br />
    repo.appdata
</dl>
<p> Application specific data that may be used in any way by the code using the repository. </p>
<dl>
<dt>
<dd>
Datapos *meta; /* read only */<br />
$repo-&gt;{meta} repo.meta<br />
    repo.meta
</dl>
<p> Return a Datapos object of the repodata&#8217;s metadata. You can use the lookup methods of the Datapos class to lookup metadata attributes, like the repository timestamp.</p>
<h3>CONSTANTS</h3>
<p> <code>REPO_REUSE_REPODATA</code></p>
<dl>
<dt>
<dd> Reuse the last repository data area (&#8220;repodata&#8221;) instead of creating a new one.</dl>
<p> <code>REPO_NO_INTERNALIZE</code></p>
<dl>
<dt>
<dd> Do not internalize the added repository data. This is useful if you plan to add more data because internalization is a costly operation.</dl>
<p> <code>REPO_LOCALPOOL</code></p>
<dl>
<dt>
<dd> Use the repodata&#8217;s pool for Id storage instead of the global pool. Useful if you don&#8217;t want to pollute the global pool with many unneeded ids, like when storing the filelist.</dl>
<p> <code>REPO_USE_LOADING</code></p>
<dl>
<dt>
<dd> Use the repodata that is currently being loaded instead of creating a new one. This only makes sense if used in a load callback.</dl>
<p> <code>REPO_EXTEND_SOLVABLES</code></p>
<dl>
<dt>
<dd> Do not create new solvables for the new data, but match existing solvables and add the data to them. Repository metadata is often split into multiple parts, with one primary file describing all packages and other parts holding information that is normally not needed, like the changelog.</dl>
<p> <code>REPO_USE_ROOTDIR</code></p>
<dl>
<dt>
<dd> Prepend the pool&#8217;s rootdir to the path when doing file operations.</dl>
<p> <code>REPO_NO_LOCATION</code></p>
<dl>
<dt>
<dd> Do not add a location element to the solvables. Useful if the solvables are not in the final position, so you can add the correct location later in your code.</dl>
<p> <code>SOLV_ADD_NO_STUBS</code></p>
<dl>
<dt>
<dd> Do not create stubs for repository parts that can be downloaded on demand.</dl>
<p> <code>SUSETAGS_RECORD_SHARES</code></p>
<dl>
<dt>
<dd> This is specific to the add_susetags() method. Susetags allows one to refer to already read packages to save disk space. If this data sharing needs to work over multiple calls to add_susetags, you need to specify this flag so that the share information is made available to subsequent calls.</dl>
<h3>METHODS</h3>
<dl>
<dt>
<dd>
void free(bool reuseids = 0)<br />
    $repo-&gt;free();<br />
repo.free()<br />
    repo.free()
</dl>
<p> Free the repository and all solvables it contains. If <i>reuseids</i> is set to true, the solvable ids and the repository id may be reused by the library when added new solvables. Thus you should leave it false if you are not sure that somebody holds a reference. </p>
<dl>
<dt>
<dd>
void empty(bool reuseids = 0)<br />
    $repo-&gt;empty();<br />
repo.empty()<br />
    repo.empty()
</dl>
<p> Free all the solvables in a repository. The repository will be empty after this call. See the free() method for the meaning of <i>reuseids</i>. </p>
<dl>
<dt>
<dd>
<pre>
<code>bool isempty()</code>
<i>$repo</i><code>-&gt;isempty()</code>
<i>repo</i><code>.empty()</code>
<i>repo</i><code>.empty?</code>
</pre>
</dl>
<p> Return true if there are no solvables in this repository. </p>
<dl>
<dt>
<dd>
void internalize()<br />
    $repo-&gt;internalize();<br />
repo.internalize()<br />
    repo.internalize()
</dl>
<p> Internalize added data. Data must be internalized before it is available to the lookup and data iterator functions. </p>
<dl>
<dt>
<dd>
<pre>
<code>bool write(FILE *</code><i>fp</i><code>)</code>
<i>$repo</i><code>-&gt;write(</code><i>$fp</i><code>)</code>
<i>repo</i><code>.write(</code><i>fp</i><code>)</code>
<i>repo</i><code>.write(</code><i>fp</i><code>)</code>
</pre>
</dl>
<p> Write a repo as a &#8220;solv&#8221; file. These files can be read very fast and thus are a good way to cache repository data. Returns false if there was some error writing the file. </p>
<dl>
<dt>
<dd>
Solvableiterator solvables_iter()<br />
for my $solvable (@{$repo-&gt;solvables_iter()})<br />
for solvable in repo.solvables_iter():<br />
for solvable in repo.solvables_iter()
</dl>
<p> Iterate over all solvables in a repository. </p>
<dl>
<dt>
<dd>
Repodata add_repodata(int flags = 0)<br />
    my $repodata = $repo-&gt;add_repodata();<br />
repodata = repo.add_repodata()<br />
               repodata = repo.add_repodata()
</dl>
<p> Add a new repodata area to the repository. This is normally automatically done by the repo_add methods, so you need this method only in very rare circumstances. </p>
<dl>
<dt>
<dd>
void create_stubs()<br />
    $repo-&gt;create_stubs();<br />
repo.create_stubs()<br />
    repo.create_stubs()
</dl>
<p> Calls the create_stubs() repodata method for the last repodata of the repository. </p>
<dl>
<dt>
<dd>
<pre>
<code>bool iscontiguous()</code>
<i>$repo</i><code>-&gt;iscontiguous()</code>
<i>repo</i><code>.iscontiguous()</code>
<i>repo</i><code>.iscontiguous?</code>
</pre>
</dl>
<p> Return true if the solvables of this repository are all in a single block with no holes, i.e. they have consecutive ids. </p>
<dl>
<dt>
<dd>
Repodata first_repodata()<br />
    my $repodata = $repo-&gt;first_repodata();<br />
repodata = repo.first_repodata()<br />
               repodata = repo.first_repodata()
</dl>
<p> Checks if all repodatas but the first repodata are extensions, and return the first repodata if this is the case. Useful if you want to do a store/retrieve sequence on the repository to reduce the memory using and enable paging, as this does not work if the repository contains multiple non-extension repodata areas. </p>
<dl>
<dt>
<dd>
Selection Selection(int setflags = 0)<br />
    my $sel = $repo-&gt;Selection();<br />
sel = repo.Selection()<br />
          sel = repo.Selection()
</dl>
<p> Create a Selection consisting of all packages in the repository. </p>
<dl>
<dt>
<dd>
Dataiterator Dataiterator(Id key, const char *match = 0, int flags = 0)<br />
    my $di = $repo-&gt;Dataiterator($keyname, $match, $flags);<br />
di = repo.Dataiterator(keyname, match, flags)<br />
         di = repo.Dataiterator(keyname, match, flags)
</dl>
<dl>
<dt>
<dd>
Dataiterator Dataiterator_meta(Id key, const char *match = 0, int flags = 0)<br />
    my $di = $repo-&gt;Dataiterator_meta($keyname, $match, $flags);<br />
di = repo.Dataiterator_meta(keyname, match, flags)<br />
         di = repo.Dataiterator_meta(keyname, match, flags)
</dl>
<dl>
<dt>
<dd>
<pre>
<code>for my</code> <i>$d</i> <code>(</code><i>@$di</i><code>)</code>
<code>for</code> <i>d</i> <code>in</code> <i>di</i><code>:</code>
<code>for</code> <i>d</i> <code>in</code> <i>di</i>
</pre>
</dl>
<p> Iterate over the matching data elements in this repository. See the Dataiterator class for more information. The Dataiterator() method iterates over all solvables in a repository, whereas the Dataiterator_meta method only iterates over the repository&#8217;s meta data. </p>
<dl>
<dt>
<dd>
<pre>
<code>&lt;stringification&gt;</code>
my <i>$str</i> <code>=</code> <i>$repo</i><code>-&gt;str</code>;
<i>str</i> <code>= str(</code><i>repo</i><code>)</code>
<i>str</i> <code>=</code> <i>repo</i><code>.to_s</code>
</pre>
</dl>
<p> Return the name of the repository, or &quot;Repo#&lt;id&gt;&quot; if no name is set. </p>
<dl>
<dt>
<dd>
&lt;equality&gt;<br />
if ($repo1 == $repo2)<br />
if repo1 == repo2:<br />
if repo1 == repo2
</dl>
<p> Two repositories are equal if they belong to the same pool and have the same id.</p>
<h3>DATA ADD METHODS</h3>
<dl>
<dt>
<dd>
Solvable add_solvable()<br />
    $repo-&gt;add_solvable();<br />
repo.add_solvable()<br />
    repo.add_solvable()
</dl>
<p> Add a single empty solvable to the repository. Returns a Solvable object, see the Solvable class for more information. </p>
<dl>
<dt>
<dd>
bool add_solv(const char *name, int flags = 0)<br />
    $repo-&gt;add_solv($name);<br />
repo.add_solv(name)<br />
    repo.add_solv(name)
</dl>
<dl>
<dt>
<dd>
bool add_solv(FILE *fp, int flags = 0)<br />
    $repo-&gt;add_solv($fp);<br />
repo.add_solv(fp)<br />
    repo.add_solv(fp)
</dl>
<p> Read a &#8220;solv&#8221; file and add its contents to the repository. These files can be written with the write() method and are normally used as fast cache for repository metadata. </p>
<dl>
<dt>
<dd>
bool add_rpmdb(int flags = 0)<br />
    $repo-&gt;add_rpmdb();<br />
repo.add_rpmdb()<br />
    repo.add_rpmdb()
</dl>
<dl>
<dt>
<dd>
bool add_rpmdb_reffp(FILE *reffp, int flags = 0)<br />
    $repo-&gt;add_rpmdb_reffp($reffp);<br />
repo.add_rpmdb_reffp(reffp)<br />
    repo.add_rpmdb_reffp(reffp)
</dl>
<p> Add the contents of the rpm database to the repository. If a solv file containing an old version of the database is available, it can be passed as reffp to speed up reading. </p>
<dl>
<dt>
<dd>
Solvable add_rpm(const char *filename, int flags = 0)<br />
    my $solvable = $repo-&gt;add_rpm($filename);<br />
solvable = repo.add_rpm(filename)<br />
               solvable = repo.add_rpm(filename)
</dl>
<p> Add the metadata of a single rpm package to the repository. </p>
<dl>
<dt>
<dd>
bool add_rpmdb_pubkeys(int flags = 0)<br />
    $repo-&gt;add_rpmdb_pubkeys();<br />
repo.add_rpmdb_pubkeys()<br />
    repo.add_rpmdb_pubkeys()
</dl>
<p> Add all pubkeys contained in the rpm database to the repository. Note that newer rpm versions also allow to store the pubkeys in some directory instead of the rpm database. </p>
<dl>
<dt>
<dd>
Solvable add_pubkey(const char *keyfile, int flags = 0)<br />
    my $solvable = $repo-&gt;add_pubkey($keyfile);<br />
solvable = repo.add_pubkey(keyfile)<br />
               solvable = repo.add_pubkey(keyfile)
</dl>
<p> Add a pubkey from a file to the repository. </p>
<dl>
<dt>
<dd>
bool add_rpmmd(FILE *fp, const char *language, int flags = 0)<br />
    $repo-&gt;add_rpmmd($fp, undef);<br />
repo.add_rpmmd(fp, None)<br />
    repo.add_rpmmd(fp, nil)
</dl>
<p> Add metadata stored in the &quot;rpm-md&quot; format (i.e. from files in the &#8220;repodata&#8221; directory) to a repository. Supported files are &quot;primary&quot;, &quot;filelists&quot;, &quot;other&quot;, &quot;suseinfo&quot;. Do not forget to specify the <code>REPO_EXTEND_SOLVABLES</code> for extension files like &quot;filelists&quot; and &quot;other&quot;. Use the <i>language</i> parameter if you have language extension files, otherwise simply use a <code>undef</code>/<code>None</code>/<code>nil</code> parameter. </p>
<dl>
<dt>
<dd>
bool add_repomdxml(FILE *fp, int flags = 0)<br />
    $repo-&gt;add_repomdxml($fp);<br />
repo.add_repomdxml(fp)<br />
    repo.add_repomdxml(fp)
</dl>
<p> Add the repomd.xml meta description from the &quot;rpm-md&quot; format to the repository. This file contains information about the repository like keywords, and also a list of all database files with checksums. The data is added to the &quot;meta&quot; section of the repository, i.e. no package gets created. </p>
<dl>
<dt>
<dd>
bool add_updateinfoxml(FILE *fp, int flags = 0)<br />
    $repo-&gt;add_updateinfoxml($fp);<br />
repo.add_updateinfoxml(fp)<br />
    repo.add_updateinfoxml(fp)
</dl>
<p> Add the updateinfo.xml file containing available maintenance updates to the repository. All updates are created as special packages that have a &quot;patch:&quot; prefix in their name. </p>
<dl>
<dt>
<dd>
bool add_deltainfoxml(FILE *fp, int flags = 0)<br />
    $repo-&gt;add_deltainfoxml($fp);<br />
repo.add_deltainfoxml(fp)<br />
    repo.add_deltainfoxml(fp)
</dl>
<p> Add the deltainfo.xml file (also called prestodelta.xml) containing available delta-rpms to the repository. The data is added to the &quot;meta&quot; section, i.e. no package gets created. </p>
<dl>
<dt>
<dd>
bool add_debdb(int flags = 0)<br />
    $repo-&gt;add_debdb();<br />
repo.add_debdb()<br />
    repo.add_debdb()
</dl>
<p> Add the contents of the debian installed package database to the repository. </p>
<dl>
<dt>
<dd>
bool add_debpackages(FILE *fp, int flags = 0)<br />
    $repo-&gt;add_debpackages($fp);<br />
repo.add_debpackages($fp)<br />
    repo.add_debpackages($fp)
</dl>
<p> Add the contents of the debian repository metadata (the &quot;packages&quot; file) to the repository. </p>
<dl>
<dt>
<dd>
Solvable add_deb(const char *filename, int flags = 0)<br />
    my $solvable = $repo-&gt;add_deb($filename);<br />
solvable = repo.add_deb(filename)<br />
               solvable = repo.add_deb(filename)
</dl>
<p> Add the metadata of a single deb package to the repository. </p>
<dl>
<dt>
<dd>
bool add_mdk(FILE *fp, int flags = 0)<br />
    $repo-&gt;add_mdk($fp);<br />
repo.add_mdk(fp)<br />
    repo.add_mdk(fp)
</dl>
<p> Add the contents of the mageia/mandriva repository metadata (the &quot;synthesis.hdlist&quot; file) to the repository. </p>
<dl>
<dt>
<dd>
bool add_mdk_info(FILE *fp, int flags = 0)<br />
    $repo-&gt;add_mdk($fp);<br />
repo.add_mdk(fp)<br />
    repo.add_mdk(fp)
</dl>
<p> Extend the packages from the synthesis file with the info.xml and files.xml data. Do not forget to specify <code>REPO_EXTEND_SOLVABLES</code>. </p>
<dl>
<dt>
<dd>
bool add_arch_repo(FILE *fp, int flags = 0)<br />
    $repo-&gt;add_arch_repo($fp);<br />
repo.add_arch_repo(fp)<br />
    repo.add_arch_repo(fp)
</dl>
<p> Add the contents of the archlinux repository metadata (the &quot;.db.tar&quot; file) to the repository. </p>
<dl>
<dt>
<dd>
bool add_arch_local(const char *dir, int flags = 0)<br />
    $repo-&gt;add_arch_local($dir);<br />
repo.add_arch_local(dir)<br />
    repo.add_arch_local(dir)
</dl>
<p> Add the contents of the archlinux installed package database to the repository. The <i>dir</i> parameter is usually set to &quot;/var/lib/pacman/local&quot;. </p>
<dl>
<dt>
<dd>
bool add_content(FILE *fp, int flags = 0)<br />
    $repo-&gt;add_content($fp);<br />
repo.add_content(fp)<br />
    repo.add_content(fp)
</dl>
<p> Add the &#8220;content&#8221; meta description from the susetags format to the repository. This file contains information about the repository like keywords, and also a list of all database files with checksums. The data is added to the &quot;meta&quot; section of the repository, i.e. no package gets created. </p>
<dl>
<dt>
<dd>
bool add_susetags(FILE *fp, Id defvendor, const char *language, int flags = 0)<br />
    $repo-&gt;add_susetags($fp, $defvendor, $language);<br />
repo.add_susetags(fp, defvendor, language)<br />
    repo.add_susetags(fp, defvendor, language)
</dl>
<p> Add repository metadata in the susetags format to the repository. Like with add_rpmmd, you can specify a language if you have language extension files. The <i>defvendor</i> parameter provides a default vendor for packages with missing vendors, it is usually provided in the content file. </p>
<dl>
<dt>
<dd>
bool add_products(const char *dir, int flags = 0)<br />
    $repo-&gt;add_products($dir);<br />
repo.add_products(dir)<br />
    repo.add_products(dir)
</dl>
<p> Add the installed SUSE products database to the repository. The <i>dir</i> parameter is usually &quot;/etc/products.d&quot;.</p>
<h2>THE SOLVABLE CLASS</h2>
<p> A solvable describes all the information of one package. Each solvable belongs to one repository, it can be added and filled manually but in most cases solvables will get created by the repo_add methods.</p>
<h3>ATTRIBUTES</h3>
<dl>
<dt>
<dd>
Repo *repo; /* read only */<br />
$solvable-&gt;{repo} solvable.repo<br />
    solvable.repo
</dl>
<p> The repository this solvable belongs to. </p>
<dl>
<dt>
<dd>
Pool *pool; /* read only */<br />
$solvable-&gt;{pool} solvable.pool<br />
    solvable.pool
</dl>
<p> The pool this solvable belongs to, same as the pool of the repo. </p>
<dl>
<dt>
<dd>
Id id; /* read only */<br />
$solvable-&gt;{id} solvable.id<br />
    solvable.id
</dl>
<p> The specific id of the solvable. </p>
<dl>
<dt>
<dd>
char *name; /* read/write */<br />
$solvable-&gt;{name} solvable.name<br />
    solvable.name
</dl>
<dl>
<dt>
<dd>
char *evr; /* read/write */<br />
$solvable-&gt;{evr} solvable.evr<br />
    solvable.evr
</dl>
<dl>
<dt>
<dd>
char *arch; /* read/write */<br />
$solvable-&gt;{arch} solvable.arch<br />
    solvable.arch
</dl>
<dl>
<dt>
<dd>
char *vendor; /* read/write */<br />
$solvable-&gt;{vendor} solvable.vendor<br />
    solvable.vendor
</dl>
<p> Easy access to often used attributes of solvables. They are internally stored as Ids. </p>
<dl>
<dt>
<dd>
Id nameid; /* read/write */<br />
$solvable-&gt;{nameid} solvable.nameid<br />
    solvable.nameid
</dl>
<dl>
<dt>
<dd>
Id evrid; /* read/write */<br />
$solvable-&gt;{evrid} solvable.evrid<br />
    solvable.evrid
</dl>
<dl>
<dt>
<dd>
Id archid; /* read/write */<br />
$solvable-&gt;{archid} solvable.archid<br />
    solvable.archid
</dl>
<dl>
<dt>
<dd>
Id vendorid; /* read/write */<br />
$solvable-&gt;{vendorid} solvable.vendorid<br />
    solvable.vendorid
</dl>
<p> Raw interface to the ids. Useful if you want to search for a specific id and want to avoid the string compare overhead.</p>
<h3>METHODS</h3>
<dl>
<dt>
<dd>
const char *lookup_str(Id keyname)<br />
    my $string = $solvable-&gt;lookup_str($keyname);<br />
string = solvable.lookup_str(keyname)<br />
             string = solvable.lookup_str(keyname)
</dl>
<dl>
<dt>
<dd>
Id lookup_id(Id keyname)<br />
    my $id = $solvable-&gt;lookup_id($keyname);<br />
id = solvable.lookup_id(solvid)<br />
         id = solvable.lookup_id(solvid)
</dl>
<dl>
<dt>
<dd>
unsigned long long lookup_num(Id solvid, Id keyname, unsigned long long notfound = 0)<br />
    my $num = $solvable-&gt;lookup_num($keyname);<br />
num = solvable.lookup_num(keyname)<br />
          num = solvable.lookup_num(keyname)
</dl>
<dl>
<dt>
<dd>
bool lookup_void(Id keyname)<br />
    my $bool = $solvable-&gt;lookup_void($keyname);<br />
bool = solvable.lookup_void(keyname) bool = solvable.lookup_void(keyname)
</dl>
<dl>
<dt>
<dd>
Chksum lookup_checksum(Id keyname)<br />
    my $chksum = $solvable-&gt;lookup_checksum($keyname);<br />
chksum = solvable.lookup_checksum(keyname)<br />
             chksum = solvable.lookup_checksum(keyname)
</dl>
<dl>
<dt>
<dd>
Id *lookup_idarray(Id keyname, Id marker = -1)<br />
    my @ids = $solvable-&gt;lookup_idarray($keyname);<br />
ids = solvable.lookup_idarray(keyname)<br />
          ids = solvable.lookup_idarray(keyname)
</dl>
<dl>
<dt>
<dd>
Dep *lookup_deparray(Id keyname, Id marker = -1)<br />
    my @deps = $solvable-&gt;lookup_deparray($keyname);<br />
deps = solvable.lookup_deparray(keyname)<br />
           deps = solvable.lookup_deparray(keyname)
</dl>
<p> Generic lookup methods. Retrieve data stored for the specific keyname. The lookup_idarray() method will return an array of Ids, use lookup_deparray if you want an array of Dependency objects instead. Some Id arrays contain two parts of data divided by a specific marker, for example the provides array uses the SOLVABLE_FILEMARKER id to store both the ids provided by the package and the ids added by the addfileprovides method. The default, -1, translates to the correct marker for the keyname and returns the first part of the array, use 1 to select the second part or 0 to retrieve all ids including the marker. </p>
<dl>
<dt>
<dd>
const char *lookup_location(unsigned int *OUTPUT);<br />
my($location, $medianr) = $solvable-&gt;lookup_location();<br />
location, medianr = solvable.lookup_location() location, medianr = solvable.lookup_location()
</dl>
<p> Return a tuple containing the on-media location and an optional media number for multi-part repositories (e.g. repositories spawning multiple DVDs). </p>
<dl>
<dt>
<dd>
Dataiterator Dataiterator(Id keyname, const char *match = 0, int flags = 0)<br />
    my $di = $solvable-&gt;Dataiterator($keyname, $match, $flags);<br />
di = solvable.Dataiterator(keyname, match, flags)<br />
         di = solvable.Dataiterator(keyname, match, flags)
</dl>
<dl>
<dt>
<dd>
<pre>
<code>for my</code> <i>$d</i> <code>(</code><i>@$di</i><code>)</code>
<code>for</code> <i>d</i> <code>in</code> <i>di</i><code>:</code>
<code>for</code> <i>d</i> <code>in</code> <i>di</i>
</pre>
</dl>
<p> Iterate over the matching data elements. See the Dataiterator class for more information. </p>
<dl>
<dt>
<dd>
void add_deparray(Id keyname, DepId dep, Id marker = -1);<br />
$solvable-&gt;add_deparray($keyname, $dep);<br />
solvable.add_deparray(keyname, dep)<br />
    solvable.add_deparray(keyname, dep)
</dl>
<p> Add a new dependency to the attributes stored in keyname. </p>
<dl>
<dt>
<dd>
void unset(Id keyname);<br />
$solvable-&gt;unset($keyname);<br />
solvable.unset(keyname)<br />
    solvable.unset(keyname)
</dl>
<p> Delete data stored for the specific keyname. </p>
<dl>
<dt>
<dd>
bool installable();<br />
$solvable-&gt;installable()<br />
    solvable.installable()<br />
        solvable.installable<br />
    ?
</dl>
<p> Return true if the solvable is installable on the system. Solvables are not installable if the system does not support their architecture. </p>
<dl>
<dt>
<dd>
bool isinstalled();<br />
$solvable-&gt;isinstalled()<br />
    solvable.isinstalled()<br />
        solvable.isinstalled<br />
    ?
</dl>
<p> Return true if the solvable is installed on the system. </p>
<dl>
<dt>
<dd>
<pre>
<code>bool identical(Solvable *</code><i>other</i><code>)</code>
<i>$solvable</i><code>-&gt;identical(</code><i>$other</i><code>)</code>
<i>$solvable</i><code>.identical(</code><i>other</i><code>)</code>
<i>$solvable</i><code>.identical?(</code><i>other</i><code>)</code>
</pre>
</dl>
<p> Return true if the two solvables are identical. </p>
<dl>
<dt>
<dd>
<pre>
<code>int evrcmp(Solvable *</code><i>other</i><code>)</code>
<i>$solvable</i><code>-&gt;evrcmp(</code><i>other</i><code>)</code>
<i>$solvable</i><code>.evrcmp(</code><i>other</i><code>)</code>
<i>$solvable</i><code>.evrcmp(</code><i>other</i><code>)</code>
</pre>
</dl>
<p> Returns -1 if the epoch/version/release of the solvable is less than the one from the other solvable, 1 if it is greater, and 0 if they are equal. Note that &quot;equal&quot; does not mean that the evr is identical. </p>
<dl>
<dt>
<dd>
Selection Selection(int setflags = 0)<br />
    my $sel = $solvable-&gt;Selection();<br />
sel = solvable.Selection()<br />
          sel = solvable.Selection()
</dl>
<p> Create a Selection containing just the single solvable. </p>
<dl>
<dt>
<dd>
const char *str()<br />
    my $str = $solvable-&gt;str();<br />
str = $solvable.str()<br />
          str = $solvable.str()
</dl>
<p> Return a string describing the solvable. The string consists of the name, version, and architecture of the Solvable. </p>
<dl>
<dt>
<dd>
<pre>
<code>&lt;stringification&gt;</code>
my <i>$str</i> <code>=</code> <i>$solvable</i><code>-&gt;str</code>;
<i>str</i> <code>= str(</code><i>solvable</i><code>)</code>
<i>str</i> <code>=</code> <i>solvable</i><code>.to_s</code>
</pre>
</dl>
<p> Same as calling the str() method. </p>
<dl>
<dt>
<dd>
&lt;equality&gt;<br />
if ($solvable1 == $solvable2)<br />
if solvable1 == solvable2:<br />
if solvable1 == solvable2
</dl>
<p> Two solvables are equal if they are part of the same pool and have the same ids.</p>
<h2>THE DATAITERATOR CLASS</h2>
<p> Dataiterators can be used to do complex string searches or to iterate over arrays. They can be created via the constructors in the Pool, Repo, and Solvable classes. The Repo and Solvable constructors will limit the search to the repository or the specific package.</p>
<h3>CONSTANTS</h3>
<p> <code>SEARCH_STRING</code></p>
<dl>
<dt>
<dd> Return a match if the search string matches the value.</dl>
<p> <code>SEARCH_STRINGSTART</code></p>
<dl>
<dt>
<dd> Return a match if the value starts with the search string.</dl>
<p> <code>SEARCH_STRINGEND</code></p>
<dl>
<dt>
<dd> Return a match if the value ends with the search string.</dl>
<p> <code>SEARCH_SUBSTRING</code></p>
<dl>
<dt>
<dd> Return a match if the search string can be matched somewhere in the value.</dl>
<p> <code>SEARCH_GLOB</code></p>
<dl>
<dt>
<dd> Do a glob match of the search string against the value.</dl>
<p> <code>SEARCH_REGEX</code></p>
<dl>
<dt>
<dd> Do a regular expression match of the search string against the value.</dl>
<p> <code>SEARCH_NOCASE</code></p>
<dl>
<dt>
<dd> Ignore case when matching strings. Works for all the above match types.</dl>
<p> <code>SEARCH_FILES</code></p>
<dl>
<dt>
<dd> Match the complete filenames of the file list, not just the base name.</dl>
<p> <code>SEARCH_COMPLETE_FILELIST</code></p>
<dl>
<dt>
<dd> When matching the file list, check every file of the package not just the subset from the primary metadata.</dl>
<p> <code>SEARCH_CHECKSUMS</code></p>
<dl>
<dt>
<dd> Allow the matching of checksum entries.</dl>
<h3>METHODS</h3>
<dl>
<dt>
<dd>
void prepend_keyname(Id keyname);<br />
$di-&gt;prepend_keyname($keyname);<br />
di.prepend_keyname(keyname)<br />
    di.prepend_keyname(keyname)
</dl>
<p> Do a sub-search in the array stored in keyname. </p>
<dl>
<dt>
<dd>
void skip_solvable();<br />
$di-&gt;kip_solvable();<br />
di.skip_solvable()<br />
    di.skip_solvable()
</dl>
<p> Stop matching the current solvable and advance to the next one. </p>
<dl>
<dt>
<dd>
<pre>
<code>&lt;iteration&gt;</code>
<code>for my</code> <i>$d</i> <code>(</code><i>@$di</i><code>)</code>
<code>for</code> <i>d</i> <code>in</code> <i>di</i><code>:</code>
<code>for</code> <i>d</i> <code>in</code> <i>di</i>
</pre>
</dl>
<p> Iterate through the matches. If there is a match, the object in d will be of type Datamatch.</p>
<h2>THE DATAMATCH CLASS</h2>
<p> Objects of this type will be created for every value matched by a dataiterator.</p>
<h3>ATTRIBUTES</h3>
<dl>
<dt>
<dd>
Pool *pool; /* read only */<br />
$d-&gt;{pool} d.pool<br />
    d.pool
</dl>
<p> Back pointer to pool. </p>
<dl>
<dt>
<dd>
Repo *repo; /* read only */<br />
$d-&gt;{repo} d.repo<br />
    d.repo
</dl>
<p> The repository containing the matched object. </p>
<dl>
<dt>
<dd>
Solvable *solvable; /* read only */<br />
$d-&gt;{solvable} d.solvable<br />
    d.solvable
</dl>
<p> The solvable containing the value that was matched. </p>
<dl>
<dt>
<dd>
Id solvid; /* read only */<br />
$d-&gt;{solvid} d.solvid<br />
    d.solvid
</dl>
<p> The id of the solvable that matched. </p>
<dl>
<dt>
<dd>
Id key_id;<br />
$d-&gt;{key_id} d.key_id<br />
    d.key_id
</dl>
<dl>
<dt>
<dd>
const char *key_idstr;<br />
$d-&gt;{key_idstr} d.key_idstr<br />
    d.key_idstr
</dl>
<p> The keyname that matched, either as id or string. </p>
<dl>
<dt>
<dd>
Id type_id;<br />
$d-&gt;{type_id} d.type_id<br />
    d.type_id
</dl>
<dl>
<dt>
<dd>
const char *type_idstr;<br />
$d-&gt;{type_idstr};<br />
d.type_idstr<br />
    d.type_idstr
</dl>
<p> The key type of the value that was matched, either as id or string. </p>
<dl>
<dt>
<dd>
Id id;<br />
$d-&gt;{id} d.id<br />
    d.id
</dl>
<dl>
<dt>
<dd>
Id idstr;<br />
$d-&gt;{idstr} d.idstr<br />
    d.idstr
</dl>
<p> The Id of the value that was matched (only valid for id types), either as id or string. </p>
<dl>
<dt>
<dd>
const char *str;<br />
$d-&gt;{str} d.str<br />
    d.str
</dl>
<p> The string value that was matched (only valid for string types). </p>
<dl>
<dt>
<dd>
unsigned long long num;<br />
$d-&gt;{num} d.num<br />
    d.num
</dl>
<p> The numeric value that was matched (only valid for numeric types). </p>
<dl>
<dt>
<dd>
unsigned int num2;<br />
$d-&gt;{num2} d.num2<br />
    d.num2
</dl>
<p> The secondary numeric value that was matched (only valid for types containing two values). </p>
<dl>
<dt>
<dd>
unsigned int binary;<br />
$d-&gt;{binary} d.binary<br />
    d.binary
</dl>
<p> The value in binary form, useful for checksums and other data that cannot be represented as a string.</p>
<h3>METHODS</h3>
<dl>
<dt>
<dd>
Datapos pos();<br />
my $pos = $d-&gt;pos();<br />
pos = d.pos()<br />
          pos = d.pos()
</dl>
<p> The position object of the current match. It can be used to do sub-searches starting at the match (if it is of an array type). See the Datapos class for more information. </p>
<dl>
<dt>
<dd>
Datapos parentpos();<br />
my $pos = $d-&gt;parentpos();<br />
pos = d.parentpos()<br />
          pos = d.parentpos()
</dl>
<p> The position object of the array containing the current match. It can be used to do sub-searches, see the Datapos class for more information. </p>
<dl>
<dt>
<dd>
<pre>
<code>&lt;stringification&gt;</code>
my <i>$str</i> <code>=</code> <i>$d</i><code>-&gt;str</code>;
<i>str</i> <code>= str(</code><i>d</i><code>)</code>
<i>str</i> <code>=</code> <i>d</i><code>.to_s</code>
</pre>
</dl>
<p> Return the stringification of the matched value. Stringification depends on the search flags, for file list entries it will return just the base name unless SEARCH_FILES is used, for checksums it will return an empty string unless SEARCH_CHECKSUMS is used. Numeric values are currently stringified to an empty string.</p>
<h2>THE SELECTION CLASS</h2>
<p> Selections are a way to easily deal with sets of packages. There are multiple constructors to create them, the most useful is probably the select() method in the Pool class.</p>
<h3>CONSTANTS</h3>
<p> <code>SELECTION_NAME</code></p>
<dl>
<dt>
<dd> Create the selection by matching package names.</dl>
<p> <code>SELECTION_PROVIDES</code></p>
<dl>
<dt>
<dd> Create the selection by matching package provides.</dl>
<p> <code>SELECTION_FILELIST</code></p>
<dl>
<dt>
<dd> Create the selection by matching package files.</dl>
<p> <code>SELECTION_CANON</code></p>
<dl>
<dt>
<dd> Create the selection by matching the canonical representation of the package. This is normally a combination of the name, the version, and the architecture of a package.</dl>
<p> <code>SELECTION_DOTARCH</code></p>
<dl>
<dt>
<dd> Allow an &#8220;.&lt;architecture&gt;&#8221; suffix when matching names or provides.</dl>
<p> <code>SELECTION_REL</code></p>
<dl>
<dt>
<dd> Allow the specification of a relation when matching names or provides, e.g. &quot;name &gt;= 1.2&quot;.</dl>
<p> <code>SELECTION_INSTALLED_ONLY</code></p>
<dl>
<dt>
<dd> Limit the package search to installed packages.</dl>
<p> <code>SELECTION_SOURCE_ONLY</code></p>
<dl>
<dt>
<dd> Limit the package search to source packages only.</dl>
<p> <code>SELECTION_WITH_SOURCE</code></p>
<dl>
<dt>
<dd> Extend the package search to also match source packages. The default is only to match binary packages.</dl>
<p> <code>SELECTION_GLOB</code></p>
<dl>
<dt>
<dd> Allow glob matching for package names, package provides, and file names.</dl>
<p> <code>SELECTION_NOCASE</code></p>
<dl>
<dt>
<dd> Ignore case when matching package names, package provides, and file names.</dl>
<p> <code>SELECTION_FLAT</code></p>
<dl>
<dt>
<dd> Return only one selection element describing the selected packages. The default is to create multiple elements for all globbed packages. Multiple elements are useful if you want to turn the selection into an install job, in that case you want an install job for every globbed package.</dl>
<h3>ATTRIBUTES</h3>
<dl>
<dt>
<dd>
Pool *pool; /* read only */<br />
$d-&gt;{pool} d.pool<br />
    d.pool
</dl>
<p> Back pointer to pool.</p>
<h3>METHODS</h3>
<dl>
<dt>
<dd>
int flags();<br />
my $flags = $sel-&gt;flags();<br />
flags = sel.flags()<br />
            flags = sel.flags()
</dl>
<p> Return the result flags of the selection. The flags are a subset of the ones used when creating the selection, they describe which method was used to get the result. For example, if you create the selection with &#8220;SELECTION_NAME | SELECTION_PROVIDES&#8221;, the resulting flags will either be SELECTION_NAME or SELECTION_PROVIDES depending if there was a package that matched the name or not. If there was no match at all, the flags will be zero. </p>
<dl>
<dt>
<dd>
bool isempty();<br />
$sel-&gt;isempty()<br />
    sel.isempty()<br />
        sel.isempty<br />
    ?
</dl>
<p> Return true if the selection is empty, i.e. no package could be matched. </p>
<dl>
<dt>
<dd>
void filter(Selection *other)<br />
    $sel-&gt;filter($other);<br />
sel.filter(other)<br />
    sel.filter(other)
</dl>
<p> Intersect two selections. Packages will only stay in the selection if there are also included in the other selecting. Does an in-place modification. </p>
<dl>
<dt>
<dd>
void add(Selection *other)<br />
    $sel-&gt;add($other);<br />
sel.add(other)<br />
    sel.add(other)
</dl>
<p> Build the union of two selections. All packages of the other selection will be added to the set of packages of the selection object. Does an in-place modification. Note that the selection flags are no longer meaningful after the add operation. </p>
<dl>
<dt>
<dd>
void add_raw(Id how, Id what)<br />
    $sel-&gt;add_raw($how, $what);<br />
sel.add_raw(how, what)<br />
    sel.add_raw(how, what)
</dl>
<p> Add a raw element to the selection. Check the Job class for information about the how and what parameters. </p>
<dl>
<dt>
<dd>
Job *jobs(int action)<br />
    my @jobs = $sel-&gt;jobs($action);<br />
jobs = sel.jobs(action)<br />
           jobs = sel.jobs(action)
</dl>
<p> Convert a selection into an array of Job objects. The action parameter is or-ed to the &#8220;how&#8221; part of the job, it describes the type of job (e.g. install, erase). See the Job class for the action and action modifier constants. </p>
<dl>
<dt>
<dd>
Solvable *solvables()<br />
    my @solvables = $sel-&gt;solvables();<br />
solvables = sel.solvables()<br />
                solvables = sel.solvables()
</dl>
<p> Convert a selection into an array of Solvable objects. </p>
<dl>
<dt>
<dd>
<pre>
<code>&lt;stringification&gt;</code>
my <i>$str</i> <code>=</code> <i>$sel</i><code>-&gt;str</code>;
<i>str</i> <code>= str(</code><i>sel</i><code>)</code>
<i>str</i> <code>=</code> <i>sel</i><code>.to_s</code>
</pre>
</dl>
<p> Return a string describing the selection.</p>
<h2>THE JOB CLASS</h2>
<p> Jobs are the way to specify to the dependency solver what to do. Most of the times jobs will get created by calling the jobs() method on a Selection object, but there is also a Job() constructor in the Pool class.</p>
<h3>CONSTANTS</h3>
<p> Selection constants: </p>
<p> <code>SOLVER_SOLVABLE</code></p>
<dl>
<dt>
<dd> The &#8220;what&#8221; part is the id of a solvable.</dl>
<p> <code>SOLVER_SOLVABLE_NAME</code></p>
<dl>
<dt>
<dd> The &#8220;what&#8221; part is the id of a package name.</dl>
<p> <code>SOLVER_SOLVABLE_PROVIDES</code></p>
<dl>
<dt>
<dd> The &#8220;what&#8221; part is the id of a package provides.</dl>
<p> <code>SOLVER_SOLVABLE_ONE_OF</code></p>
<dl>
<dt>
<dd> The &#8220;what&#8221; part is an offset into the &#8220;whatprovides&#8221; data, created by calling the towhatprovides() pool method.</dl>
<p> <code>SOLVER_SOLVABLE_REPO</code></p>
<dl>
<dt>
<dd> The &#8220;what&#8221; part is the id of a repository.</dl>
<p> <code>SOLVER_SOLVABLE_ALL</code></p>
<dl>
<dt>
<dd> The &#8220;what&#8221; part is ignored, all packages are selected.</dl>
<p> <code>SOLVER_SOLVABLE_SELECTMASK</code></p>
<dl>
<dt>
<dd> A mask containing all the above selection bits.</dl>
<p> Action constants: </p>
<p> <code>SOLVER_NOOP</code></p>
<dl>
<dt>
<dd> Do nothing.</dl>
<p> <code>SOLVER_INSTALL</code></p>
<dl>
<dt>
<dd> Install a package of the specified set of packages. It tries to install the best matching package (i.e. the highest version of the packages from the repositories with the highest priority).</dl>
<p> <code>SOLVER_ERASE</code></p>
<dl>
<dt>
<dd> Erase all of the packages from the specified set. If a package is not installed, erasing it will keep it from getting installed.</dl>
<p> <code>SOLVER_UPDATE</code></p>
<dl>
<dt>
<dd> Update the matching installed packages to their best version. If none of the specified packages are installed, try to update the installed packages to the specified versions. See the section about targeted updates about more information.</dl>
<p> <code>SOLVER_WEAKENDEPS</code></p>
<dl>
<dt>
<dd> Allow to break the dependencies of the matching packages. Handle with care.</dl>
<p> <code>SOLVER_MULTIVERSION</code></p>
<dl>
<dt>
<dd> Mark the matched packages for multiversion install. If they get to be installed because of some other job, the installation will keep the old version of the package installed (for rpm this is done by using &#8220;-i&#8221; instead of &#8220;-U&#8221;).</dl>
<p> <code>SOLVER_LOCK</code></p>
<dl>
<dt>
<dd> Do not change the state of the matched packages, i.e. when they are installed they stay installed, if not they are not selected for installation.</dl>
<p> <code>SOLVER_DISTUPGRADE</code></p>
<dl>
<dt>
<dd> Update the matching installed packages to the best version included in one of the repositories. After this operation, all come from one of the available repositories except orphaned packages. Orphaned packages are packages that have no relation to the packages in the repositories, i.e. no package in the repositories have the same name or obsolete the orphaned package. This action brings the installed packages in sync with the ones in the repository. By default it also turns of arch/vendor/version locking for the affected packages to simulate a fresh installation. This means that distupgrade can actually downgrade packages if only lower versions of a package are available in the repositories. You can tweak this behavior with the SOLVER_FLAG_DUP_ solver flags.</dl>
<p> <code>SOLVER_DROP_ORPHANED</code></p>
<dl>
<dt>
<dd> Erase all the matching installed packages if they are orphaned. This only makes sense if there is a &#8220;distupgrade all packages&#8221; job. The default is to erase orphaned packages only if they block the installation of other packages.</dl>
<p> <code>SOLVER_VERIFY</code></p>
<dl>
<dt>
<dd> Fix dependency problems of matching installed packages. The default is to ignore dependency problems for installed packages.</dl>
<p> <code>SOLVER_USERINSTALLED</code></p>
<dl>
<dt>
<dd> The matching installed packages are considered to be installed by a user, thus not installed to fulfill some dependency. This is needed input for the calculation of unneeded packages for jobs that have the SOLVER_CLEANDEPS flag set.</dl>
<p> <code>SOLVER_ALLOWUNINSTALL</code></p>
<dl>
<dt>
<dd> Allow the solver to deinstall the matching installed packages if they get into the way of resolving a dependency. This is like the SOLVER_FLAG_ALLOW_UNINSTALL flag, but limited to a specific set of packages.</dl>
<p> <code>SOLVER_JOBMASK</code></p>
<dl>
<dt>
<dd> A mask containing all the above action bits.</dl>
<p> Action modifier constants: </p>
<p> <code>SOLVER_WEAK</code></p>
<dl>
<dt>
<dd> Makes the job a weak job. The solver tries to fulfill weak jobs, but does not report a problem if it is not possible to do so.</dl>
<p> <code>SOLVER_ESSENTIAL</code></p>
<dl>
<dt>
<dd> Makes the job an essential job. If there is a problem with the job, the solver will not propose to remove the job as one solution (unless all other solutions are also to remove essential jobs).</dl>
<p> <code>SOLVER_CLEANDEPS</code></p>
<dl>
<dt>
<dd> The solver will try to also erase all packages dragged in through dependencies when erasing the package. This needs SOLVER_USERINSTALLED jobs to maximize user satisfaction.</dl>
<p> <code>SOLVER_FORCEBEST</code></p>
<dl>
<dt>
<dd> Insist on the best package for install, update, and distupgrade jobs. If this flag is not used, the solver will use the second-best package if the best package cannot be installed for some reason. When this flag is used, the solver will generate a problem instead.</dl>
<p> <code>SOLVER_TARGETED</code></p>
<dl>
<dt>
<dd> Forces targeted operation update and distupgrade jobs. See the section about targeted updates about more information.</dl>
<p> Set constants. </p>
<p> <code>SOLVER_SETEV</code></p>
<dl>
<dt>
<dd> The job specified the exact epoch and version of the package set.</dl>
<p> <code>SOLVER_SETEVR</code></p>
<dl>
<dt>
<dd> The job specified the exact epoch, version, and release of the package set.</dl>
<p> <code>SOLVER_SETARCH</code></p>
<dl>
<dt>
<dd> The job specified the exact architecture of the packages from the set.</dl>
<p> <code>SOLVER_SETVENDOR</code></p>
<dl>
<dt>
<dd> The job specified the exact vendor of the packages from the set.</dl>
<p> <code>SOLVER_SETREPO</code></p>
<dl>
<dt>
<dd> The job specified the exact repository of the packages from the set.</dl>
<p> <code>SOLVER_SETNAME</code></p>
<dl>
<dt>
<dd> The job specified the exact name of the packages from the set.</dl>
<p> <code>SOLVER_NOAUTOSET</code></p>
<dl>
<dt>
<dd> Turn of automatic set flag generation for SOLVER_SOLVABLE jobs.</dl>
<p> <code>SOLVER_SETMASK</code></p>
<dl>
<dt>
<dd> A mask containing all the above set bits.</dl>
<p> See the section about set bits for more information.</p>
<h3>ATTRIBUTES</h3>
<dl>
<dt>
<dd>
Pool *pool; /* read only */<br />
$job-&gt;{pool} d.pool<br />
    d.pool
</dl>
<p> Back pointer to pool. </p>
<dl>
<dt>
<dd>
Id how; /* read/write */<br />
$job-&gt;{how} d.how<br />
    d.how
</dl>
<p> Union of the selection, action, action modifier, and set flags. The selection part describes the semantics of the &#8220;what&#8221; Id. </p>
<dl>
<dt>
<dd>
Id what; /* read/write */<br />
$job-&gt;{what} d.what<br />
    d.what
</dl>
<p> Id describing the set of packages, the meaning depends on the selection part of the &#8220;how&#8221; attribute.</p>
<h3>METHODS</h3>
<dl>
<dt>
<dd>
Solvable *solvables()<br />
    my @solvables = $job-&gt;solvables();<br />
solvables = job.solvables()<br />
                solvables = job.solvables()
</dl>
<p> Return the set of solvables of the job as an array of Solvable objects. </p>
<dl>
<dt>
<dd>
bool isemptyupdate();<br />
$job-&gt;isemptyupdate()<br />
    job.isemptyupdate()<br />
        job.isemptyupdate<br />
    ?
</dl>
<p> Convenience function to find out if the job describes an update job with no matching packages, i.e. a job that does nothing. Some package managers like &#8220;zypper&#8221; like to turn those jobs into install jobs, i.e. an update of a not-installed package will result into the installation of the package. </p>
<dl>
<dt>
<dd>
<pre>
<code>&lt;stringification&gt;</code>
my <i>$str</i> <code>=</code> <i>$job</i><code>-&gt;str</code>;
<i>str</i> <code>= str(</code><i>job</i><code>)</code>
<i>str</i> <code>=</code> <i>job</i><code>.to_s</code>
</pre>
</dl>
<p> Return a string describing the job. </p>
<dl>
<dt>
<dd>
&lt;equality&gt;<br />
if ($job1 == $job2)<br />
if job1 == job2:<br />
if job1 == job2
</dl>
<p> Two jobs are equal if they belong to the same pool and both the &#8220;how&#8221; and the &#8220;what&#8221; attributes are the same.</p>
<h3>TARGETED UPDATES</h3>
<p> Libsolv has two modes for upgrades and distupgrade: targeted and untargeted. Untargeted mode means that the installed packages from the specified set will be updated to the best version. Targeted means that packages that can be updated to a package in the specified set will be updated to the best package of the set. </p>
<p> Here&#8217;s an example to explain the subtle difference. Suppose that you have package A installed in version &quot;1.1&quot;, &quot;A-1.2&quot; is available in one of the repositories and there is also package &quot;B&quot; that obsoletes package A. </p>
<p> An untargeted update of &quot;A&quot; will update the installed &quot;A-1.1&quot; to package &quot;B&quot;, because that is the newest version (B obsoletes A and is thus newer). </p>
<p> A targeted update of &quot;A&quot; will update &quot;A-1.1&quot; to &quot;A-1.2&quot;, as the set of packages contains both &quot;A-1.1&quot; and &quot;A-1.2&quot;, and &quot;A-1.2&quot; is the newer one. </p>
<p> An untargeted update of &quot;B&quot; will do nothing, as &quot;B&quot; is not installed. </p>
<p> An targeted update of &quot;B&quot; will update &quot;A-1.1&quot; to &quot;B&quot;. </p>
<p> Note that the default is to do &quot;auto-targeting&quot;, thus if the specified set of packages does not include an installed package, the solver will assume targeted operation even if SOLVER_TARGETED is not used. </p>
<p> This mostly matches the intent of the user, with one exception: In the example above, an update of &quot;A-1.2&quot; will update &quot;A-1.1&quot; to &quot;A-1.2&quot; (targeted mode), but a second update of &quot;A-1.2&quot; will suddenly update to &quot;B&quot;, as untargeted mode is chosen because &quot;A-1.2&quot; is now installed. </p>
<p> If you want to have full control over when targeting mode is chosen, turn off auto-targeting with the SOLVER_FLAG_NO_AUTOTARGET solver option. In that case, all updates are considered to be untargeted unless they include the SOLVER_TARGETED flag.</p>
<h3>SET BITS</h3>
<p> Set bits specify which parts of the specified packages where specified by the user. It is used by the solver when checking if an operation is allowed or not. For example, the solver will normally not allow the downgrade of an installed package. But it will not report a problem if the SOLVER_SETEVR flag is used, as it then assumes that the user specified the exact version and thus knows what he is doing. </p>
<p> So if a package &quot;screen-1-1&quot; is installed for the x86_64 architecture and version &quot;2-1&quot; is only available for the i586 architecture, installing package &quot;screen-2.1&quot; will ask the user for confirmation because of the different architecture. When using the Selection class to create jobs the set bits are automatically added, e.g. selecting &#8220;screen.i586&#8221; will automatically add SOLVER_SETARCH, and thus no problem will be reported.</p>
<h2>THE SOLVER CLASS</h2>
<p> Dependency solving is what this library is about. A solver object is needed for solving to store the result of the solver run. The solver object can be used multiple times for different jobs, reusing it allows the solver to re-use the dependency rules it already computed.</p>
<h3>CONSTANTS</h3>
<p> Flags to modify some of the solver&#8217;s behavior: </p>
<p> <code>SOLVER_FLAG_ALLOW_DOWNGRADE</code></p>
<dl>
<dt>
<dd> Allow the solver to downgrade packages without asking for confirmation (i.e. reporting a problem).</dl>
<p> <code>SOLVER_FLAG_ALLOW_ARCHCHANGE</code></p>
<dl>
<dt>
<dd> Allow the solver to change the architecture of an installed package without asking for confirmation. Note that changes to/from noarch are always considered to be allowed.</dl>
<p> <code>SOLVER_FLAG_ALLOW_VENDORCHANGE</code></p>
<dl>
<dt>
<dd> Allow the solver to change the vendor of an installed package without asking for confirmation. Each vendor is part of one or more vendor equivalence classes, normally installed packages may only change their vendor if the new vendor shares at least one equivalence class.</dl>
<p> <code>SOLVER_FLAG_ALLOW_NAMECHANGE</code></p>
<dl>
<dt>
<dd> Allow the solver to change the name of an installed package, i.e. install a package with a different name that obsoletes the installed package. This option is on by default.</dl>
<p> <code>SOLVER_FLAG_ALLOW_UNINSTALL</code></p>
<dl>
<dt>
<dd> Allow the solver to erase installed packages to fulfill the jobs. This flag also includes the above flags. You may want to set this flag if you only have SOLVER_ERASE jobs, as in that case it&#8217;s better for the user to check the transaction overview instead of approving every single package that needs to be erased.</dl>
<p> <code>SOLVER_FLAG_DUP_ALLOW_DOWNGRADE</code></p>
<dl>
<dt>
<dd> Like SOLVER_FLAG_ALLOW_DOWNGRADE, but used in distupgrade mode.</dl>
<p> <code>SOLVER_FLAG_DUP_ALLOW_ARCHCHANGE</code></p>
<dl>
<dt>
<dd> Like SOLVER_FLAG_ALLOW_ARCHCHANGE, but used in distupgrade mode.</dl>
<p> <code>SOLVER_FLAG_DUP_ALLOW_VENDORCHANGE</code></p>
<dl>
<dt>
<dd> Like SOLVER_FLAG_ALLOW_VENDORCHANGE, but used in distupgrade mode.</dl>
<p> <code>SOLVER_FLAG_DUP_ALLOW_NAMECHANGE</code></p>
<dl>
<dt>
<dd> Like SOLVER_FLAG_ALLOW_NAMECHANGE, but used in distupgrade mode.</dl>
<p> <code>SOLVER_FLAG_NO_UPDATEPROVIDE</code></p>
<dl>
<dt>
<dd> If multiple packages obsolete an installed package, the solver checks the provides of every such package and ignores all packages that do not provide the installed package name. Thus, you can have an official update candidate that provides the old name, and other packages that also obsolete the package but are not considered for updating. If you cannot use this feature, you can turn it off by setting this flag.</dl>
<p> <code>SOLVER_FLAG_SPLITPROVIDES</code></p>
<dl>
<dt>
<dd> Make the solver aware of special provides of the form &#8220;&lt;packagename&gt;:&lt;path&gt;&#8221; used in SUSE systems to support package splits.</dl>
<p> <code>SOLVER_FLAG_IGNORE_RECOMMENDED</code></p>
<dl>
<dt>
<dd> Do not process optional (aka weak) dependencies.</dl>
<p> <code>SOLVER_FLAG_ADD_ALREADY_RECOMMENDED</code></p>
<dl>
<dt>
<dd> Install recommended or supplemented packages even if they have no connection to the current transaction. You can use this feature to implement a simple way for the user to install new recommended packages that were not available in the past.</dl>
<p> <code>SOLVER_FLAG_NO_INFARCHCHECK</code></p>
<dl>
<dt>
<dd> Turn off the inferior architecture checking that is normally done by the solver. Normally, the solver allows only the installation of packages from the &quot;best&quot; architecture if a package is available for multiple architectures.</dl>
<p> <code>SOLVER_FLAG_BEST_OBEY_POLICY</code></p>
<dl>
<dt>
<dd> Make the SOLVER_FORCEBEST job option consider only packages that meet the policies for installed packages, i.e. no downgrades, no architecture change, no vendor change (see the first flags of this section). If the flag is not specified, the solver will enforce the installation of the best package ignoring the installed packages, which may conflict with the set policy.</dl>
<p> <code>SOLVER_FLAG_NO_AUTOTARGET</code></p>
<dl>
<dt>
<dd> Do not enable auto-targeting up update and distupgrade jobs. See the section on targeted updates for more information.</dl>
<p> <code>SOLVER_FLAG_KEEP_ORPHANS</code></p>
<dl>
<dt>
<dd> Do not allow orphaned packages to be deinstalled if they get in the way of resolving other packages.</dl>
<p> <code>SOLVER_FLAG_BREAK_ORPHANS</code></p>
<dl>
<dt>
<dd> Ignore dependencies of orphaned packages that get in the way of resolving non-orphaned ones. Setting the flag might result in no longer working packages in case they are orphaned.</dl>
<p> <code>SOLVER_FLAG_FOCUS_INSTALLED</code></p>
<dl>
<dt>
<dd> Resolve installed packages before resolving the given job. Setting this flag means that the solver will prefer picking a package version that fits the other installed packages over updating installed packages.</dl>
<p> Basic rule types: </p>
<p> <code>SOLVER_RULE_UNKNOWN</code></p>
<dl>
<dt>
<dd> A rule of an unknown class. You should never encounter those.</dl>
<p> <code>SOLVER_RULE_PKG</code></p>
<dl>
<dt>
<dd> A package dependency rule.</dl>
<p> <code>SOLVER_RULE_UPDATE</code></p>
<dl>
<dt>
<dd> A rule to implement the update policy of installed packages. Every installed package has an update rule that consists of the packages that may replace the installed package.</dl>
<p> <code>SOLVER_RULE_FEATURE</code></p>
<dl>
<dt>
<dd> Feature rules are fallback rules used when an update rule is disabled. They include all packages that may replace the installed package ignoring the update policy, i.e. they contain downgrades, arch changes and so on. Without them, the solver would simply erase installed packages if their update rule gets disabled.</dl>
<p> <code>SOLVER_RULE_JOB</code></p>
<dl>
<dt>
<dd> Job rules implement the job given to the solver.</dl>
<p> <code>SOLVER_RULE_DISTUPGRADE</code></p>
<dl>
<dt>
<dd> These are simple negative assertions that make sure that only packages are kept that are also available in one of the repositories.</dl>
<p> <code>SOLVER_RULE_INFARCH</code></p>
<dl>
<dt>
<dd> Infarch rules are also negative assertions, they disallow the installation of packages when there are packages of the same name but with a better architecture.</dl>
<p> <code>SOLVER_RULE_CHOICE</code></p>
<dl>
<dt>
<dd> Choice rules are used to make sure that the solver prefers updating to installing different packages when some dependency is provided by multiple packages with different names. The solver may always break choice rules, so you will not see them when a problem is found.</dl>
<p> <code>SOLVER_RULE_LEARNT</code></p>
<dl>
<dt>
<dd> These rules are generated by the solver to keep it from running into the same problem multiple times when it has to backtrack. They are the main reason why a sat solver is faster than other dependency solver implementations.</dl>
<p> Special dependency rule types: </p>
<p> <code>SOLVER_RULE_PKG_NOT_INSTALLABLE</code></p>
<dl>
<dt>
<dd> This rule was added to prevent the installation of a package of an architecture that does not work on the system.</dl>
<p> <code>SOLVER_RULE_PKG_NOTHING_PROVIDES_DEP</code></p>
<dl>
<dt>
<dd> The package contains a required dependency which was not provided by any package.</dl>
<p> <code>SOLVER_RULE_PKG_REQUIRES</code></p>
<dl>
<dt>
<dd> Similar to SOLVER_RULE_PKG_NOTHING_PROVIDES_DEP, but in this case some packages provided the dependency but none of them could be installed due to other dependency issues.</dl>
<p> <code>SOLVER_RULE_PKG_SELF_CONFLICT</code></p>
<dl>
<dt>
<dd> The package conflicts with itself. This is not allowed by older rpm versions.</dl>
<p> <code>SOLVER_RULE_PKG_CONFLICTS</code></p>
<dl>
<dt>
<dd> To fulfill the dependencies two packages need to be installed, but one of the packages contains a conflict with the other one.</dl>
<p> <code>SOLVER_RULE_PKG_SAME_NAME</code></p>
<dl>
<dt>
<dd> The dependencies can only be fulfilled by multiple versions of a package, but installing multiple versions of the same package is not allowed.</dl>
<p> <code>SOLVER_RULE_PKG_OBSOLETES</code></p>
<dl>
<dt>
<dd> To fulfill the dependencies two packages need to be installed, but one of the packages obsoletes the other one.</dl>
<p> <code>SOLVER_RULE_PKG_IMPLICIT_OBSOLETES</code></p>
<dl>
<dt>
<dd> To fulfill the dependencies two packages need to be installed, but one of the packages has provides a dependency that is obsoleted by the other one. See the POOL_FLAG_IMPLICITOBSOLETEUSESPROVIDES flag.</dl>
<p> <code>SOLVER_RULE_PKG_INSTALLED_OBSOLETES</code></p>
<dl>
<dt>
<dd> To fulfill the dependencies a package needs to be installed that is obsoleted by an installed package. See the POOL_FLAG_NOINSTALLEDOBSOLETES flag.</dl>
<p> <code>SOLVER_RULE_JOB_NOTHING_PROVIDES_DEP</code></p>
<dl>
<dt>
<dd> The user asked for installation of a package providing a specific dependency, but no available package provides it.</dl>
<p> <code>SOLVER_RULE_JOB_UNKNOWN_PACKAGE</code></p>
<dl>
<dt>
<dd> The user asked for installation of a package with a specific name, but no available package has that name.</dl>
<p> <code>SOLVER_RULE_JOB_PROVIDED_BY_SYSTEM</code></p>
<dl>
<dt>
<dd> The user asked for the erasure of a dependency that is provided by the system (i.e. for special hardware or language dependencies), this cannot be done with a job.</dl>
<p> <code>SOLVER_RULE_JOB_UNSUPPORTED</code></p>
<dl>
<dt>
<dd> The user asked for something that is not yet implemented, e.g. the installation of all packages at once.</dl>
<p> Policy error constants </p>
<p> <code>POLICY_ILLEGAL_DOWNGRADE</code></p>
<dl>
<dt>
<dd> The solver ask for permission before downgrading packages.</dl>
<p> <code>POLICY_ILLEGAL_ARCHCHANGE</code></p>
<dl>
<dt>
<dd> The solver ask for permission before changing the architecture of installed packages.</dl>
<p> <code>POLICY_ILLEGAL_VENDORCHANGE</code></p>
<dl>
<dt>
<dd> The solver ask for permission before changing the vendor of installed packages.</dl>
<p> <code>POLICY_ILLEGAL_NAMECHANGE</code></p>
<dl>
<dt>
<dd> The solver ask for permission before replacing an installed packages with a package that has a different name.</dl>
<p> Solution element type constants </p>
<p> <code>SOLVER_SOLUTION_JOB</code></p>
<dl>
<dt>
<dd> The problem can be solved by removing the specified job.</dl>
<p> <code>SOLVER_SOLUTION_POOLJOB</code></p>
<dl>
<dt>
<dd> The problem can be solved by removing the specified job that is defined in the pool.</dl>
<p> <code>SOLVER_SOLUTION_INFARCH</code></p>
<dl>
<dt>
<dd> The problem can be solved by allowing the installation of the specified package with an inferior architecture.</dl>
<p> <code>SOLVER_SOLUTION_DISTUPGRADE</code></p>
<dl>
<dt>
<dd> The problem can be solved by allowing to keep the specified package installed.</dl>
<p> <code>SOLVER_SOLUTION_BEST</code></p>
<dl>
<dt>
<dd> The problem can be solved by allowing to install the specified package that is not the best available package.</dl>
<p> <code>SOLVER_SOLUTION_ERASE</code></p>
<dl>
<dt>
<dd> The problem can be solved by allowing to erase the specified package.</dl>
<p> <code>SOLVER_SOLUTION_REPLACE</code></p>
<dl>
<dt>
<dd> The problem can be solved by allowing to replace the package with some other package.</dl>
<p> <code>SOLVER_SOLUTION_REPLACE_DOWNGRADE</code></p>
<dl>
<dt>
<dd> The problem can be solved by allowing to replace the package with some other package that has a lower version.</dl>
<p> <code>SOLVER_SOLUTION_REPLACE_ARCHCHANGE</code></p>
<dl>
<dt>
<dd> The problem can be solved by allowing to replace the package with some other package that has a different architecture.</dl>
<p> <code>SOLVER_SOLUTION_REPLACE_VENDORCHANGE</code></p>
<dl>
<dt>
<dd> The problem can be solved by allowing to replace the package with some other package that has a different vendor.</dl>
<p> <code>SOLVER_SOLUTION_REPLACE_NAMECHANGE</code></p>
<dl>
<dt>
<dd> The problem can be solved by allowing to replace the package with some other package that has a different name.</dl>
<p> Reason constants </p>
<p> <code>SOLVER_REASON_UNRELATED</code></p>
<dl>
<dt>
<dd> The package status did not change as it was not related to any job.</dl>
<p> <code>SOLVER_REASON_UNIT_RULE</code></p>
<dl>
<dt>
<dd> The package was installed/erased/kept because of a unit rule, i.e. a rule where all literals but one were false.</dl>
<p> <code>SOLVER_REASON_KEEP_INSTALLED</code></p>
<dl>
<dt>
<dd> The package was chosen when trying to keep as many packages installed as possible.</dl>
<p> <code>SOLVER_REASON_RESOLVE_JOB</code></p>
<dl>
<dt>
<dd> The decision happened to fulfill a job rule.</dl>
<p> <code>SOLVER_REASON_UPDATE_INSTALLED</code></p>
<dl>
<dt>
<dd> The decision happened to fulfill a package update request.</dl>
<p> <code>SOLVER_REASON_CLEANDEPS_ERASE</code></p>
<dl>
<dt>
<dd> The package was erased when cleaning up dependencies from other erased packages.</dl>
<p> <code>SOLVER_REASON_RESOLVE</code></p>
<dl>
<dt>
<dd> The package was installed to fulfill package dependencies.</dl>
<p> <code>SOLVER_REASON_WEAKDEP</code></p>
<dl>
<dt>
<dd> The package was installed because of a weak dependency (Recommends or Supplements).</dl>
<p> <code>SOLVER_REASON_RESOLVE_ORPHAN</code></p>
<dl>
<dt>
<dd> The decision about the package was made when deciding the fate of orphaned packages.</dl>
<p> <code>SOLVER_REASON_RECOMMENDED</code></p>
<dl>
<dt>
<dd> This is a special case of SOLVER_REASON_WEAKDEP.</dl>
<p> <code>SOLVER_REASON_SUPPLEMENTED</code></p>
<dl>
<dt>
<dd> This is a special case of SOLVER_REASON_WEAKDEP.</dl>
<h3>ATTRIBUTES</h3>
<dl>
<dt>
<dd>
Pool *pool; /* read only */<br />
$job-&gt;{pool} d.pool<br />
    d.pool
</dl>
<p> Back pointer to pool.</p>
<h3>METHODS</h3>
<dl>
<dt>
<dd>
int set_flag(int flag, int value)<br />
    my $oldvalue = $solver-&gt;set_flag($flag, $value);<br />
oldvalue = solver.set_flag(flag, value)<br />
               oldvalue = solver.set_flag(flag, value)
</dl>
<dl>
<dt>
<dd>
int get_flag(int flag)<br />
    my $value = $solver-&gt;get_flag($flag);<br />
value = solver.get_flag(flag)<br />
            value = solver.get_flag(flag)
</dl>
<p> Set/get a solver specific flag. The flags define the policies the solver has to obey. The flags are explained in the CONSTANTS section of this class. </p>
<dl>
<dt>
<dd>
Problem *solve(Job *jobs)<br />
    my @problems = $solver-&gt;solve(\@jobs);<br />
problems = solver.solve(jobs)<br />
               problems = solver.solve(jobs)
</dl>
<p> Solve a problem specified in the job list (plus the jobs defined in the pool). Returns an array of problems that need user interaction, or an empty array if no problems were encountered. See the Problem class on how to deal with problems. </p>
<dl>
<dt>
<dd>
Transaction transaction()<br />
    my $trans = $solver-&gt;transaction();<br />
trans = solver.transaction()<br />
            trans = solver.transaction()
</dl>
<p> Return the transaction to implement the calculated package changes. A transaction is available even if problems were found, this is useful for interactive user interfaces that show both the job result and the problems. </p>
<dl>
<dt>
<dd>
int reason = describe_decision(Solvable * s, Rule *OUTPUT)<br />
    my($reason, $rule) = $solver-&gt;describe_decision($solvable);<br />
(reason, rule) = solver.describe_decision(solvable)(reason, rule) = solver.describe_decision(solvable)
</dl>
<p> Return the reason why a specific solvable was installed or erased. For most of the reasons the rule that triggered the decision is also returned.</p>
<h2>THE PROBLEM CLASS</h2>
<p> Problems are the way of the solver to interact with the user. You can simply list all problems and terminate your program, but a better way is to present solutions to the user and let him pick the ones he likes.</p>
<h3>ATTRIBUTES</h3>
<dl>
<dt>
<dd>
Solver *solv; /* read only */<br />
$problem-&gt;{solv} problem.solv<br />
    problem.solv
</dl>
<p> Back pointer to solver object. </p>
<dl>
<dt>
<dd>
Id id; /* read only */<br />
$problem-&gt;{id} problem.id<br />
    problem.id
</dl>
<p> Id of the problem. The first problem has Id 1, they are numbered consecutively.</p>
<h3>METHODS</h3>
<dl>
<dt>
<dd>
Rule findproblemrule()<br />
    my $probrule = $problem-&gt;findproblemrule();<br />
probrule = problem.findproblemrule()<br />
               probrule = problem.findproblemrule()
</dl>
<p> Return the rule that caused the problem. Of course in most situations there is no single responsible rule, but many rules that interconnect with each created the problem. Nevertheless, the solver uses some heuristic approach to find a rule that somewhat describes the problem best to the user. </p>
<dl>
<dt>
<dd>
Rule *findallproblemrules(bool unfiltered = 0)<br />
    my @probrules = $problem-&gt;findallproblemrules();<br />
probrules = problem.findallproblemrule()<br />
                probrules = problem.findallproblemrule()
</dl>
<p> Return all rules responsible for the problem. The returned set of rules contains all the needed information why there was a problem, but it&#8217;s hard to present them to the user in a sensible way. The default is to filter out all update and job rules (unless the returned rules only consist of those types). </p>
<dl>
<dt>
<dd>
Solution *solutions()<br />
    my @solutions = $problem-&gt;solutions();<br />
solutions = problem.solutions()<br />
                solutions = problem.solutions()
</dl>
<p> Return an array containing multiple possible solutions to fix the problem. See the solution class for more information. </p>
<dl>
<dt>
<dd>
int solution_count()<br />
    my $cnt = $problem-&gt;solution_count();<br />
cnt = problem.solution_count()<br />
          cnt = problem.solution_count()
</dl>
<p> Return the number of solutions without creating solution objects. </p>
<dl>
<dt>
<dd>
<pre>
<code>&lt;stringification&gt;</code>
my <i>$str</i> <code>=</code> <i>$problem</i><code>-&gt;str</code>;
<i>str</i> <code>= str(</code><i>problem</i><code>)</code>
<i>str</i> <code>=</code> <i>problem</i><code>.to_s</code>
</pre>
</dl>
<p> Return a string describing the problem. This is a convenience function, it is a shorthand for calling findproblemrule(), then ruleinfo() on the problem rule and problemstr() on the ruleinfo object.</p>
<h2>THE RULE CLASS</h2>
<p> Rules are the basic block of sat solving. Each package dependency gets translated into one or multiple rules.</p>
<h3>ATTRIBUTES</h3>
<dl>
<dt>
<dd>
Solver *solv; /* read only */<br />
$rule-&gt;{solv} rule.solv<br />
    rule.solv
</dl>
<p> Back pointer to solver object. </p>
<dl>
<dt>
<dd>
Id id; /* read only */<br />
$rule-&gt;{id} rule.id<br />
    rule.id
</dl>
<p> The id of the rule. </p>
<dl>
<dt>
<dd>
int type; /* read only */<br />
$rule-&gt;{type} rule.type<br />
    rule.type
</dl>
<p> The basic type of the rule. See the constant section of the solver class for the type list.</p>
<h3>METHODS</h3>
<dl>
<dt>
<dd>
Ruleinfo info()<br />
    my $ruleinfo = $rule-&gt;info();<br />
ruleinfo = rule.info()<br />
               ruleinfo = rule.info()
</dl>
<p> Return a Ruleinfo object that contains information about why the rule was created. But see the allinfos() method below. </p>
<dl>
<dt>
<dd>
Ruleinfo *allinfos()<br />
    my @ruleinfos = $rule-&gt;allinfos();<br />
ruleinfos = rule.allinfos()<br />
                ruleinfos = rule.allinfos()
</dl>
<p> As the same dependency rule can get created because of multiple dependencies, one Ruleinfo is not enough to describe the reason. Thus the allinfos() method returns an array of all infos about a rule. </p>
<dl>
<dt>
<dd>
&lt;equality&gt;<br />
if ($rule1 == $rule2)<br />
if rule1 == rule2:<br />
if rule1 == rule2
</dl>
<p> Two rules are equal if they belong to the same solver and have the same id.</p>
<h2>THE RULEINFO CLASS</h2>
<p> A Ruleinfo describes one reason why a rule was created.</p>
<h3>ATTRIBUTES</h3>
<dl>
<dt>
<dd>
Solver *solv; /* read only */<br />
$ruleinfo-&gt;{solv} ruleinfo.solv<br />
    ruleinfo.solv
</dl>
<p> Back pointer to solver object. </p>
<dl>
<dt>
<dd>
int type; /* read only */<br />
$ruleinfo-&gt;{type} ruleinfo.type<br />
    ruleinfo.type
</dl>
<p> The type of the ruleinfo. See the constant section of the solver class for the rule type list and the special type list. </p>
<dl>
<dt>
<dd>
Dep *dep; /* read only */<br />
$ruleinfo-&gt;{dep} ruleinfo.dep<br />
    ruleinfo.dep
</dl>
<p> The dependency leading to the creation of the rule. </p>
<dl>
<dt>
<dd>
Dep *dep_id; /* read only */<br />
$ruleinfo-&gt;{&#8216;dep_id&#8217;} ruleinfo.dep_id<br />
    ruleinfo.dep_id
</dl>
<p> The Id of the dependency leading to the creation of the rule, or zero. </p>
<dl>
<dt>
<dd>
Solvable *solvable; /* read only */<br />
$ruleinfo-&gt;{solvable} ruleinfo.solvable<br />
    ruleinfo.solvable
</dl>
<p> The involved Solvable, e.g. the one containing the dependency. </p>
<dl>
<dt>
<dd>
Solvable *othersolvable; /* read only */<br />
$ruleinfo-&gt;{othersolvable} ruleinfo.othersolvable<br />
    ruleinfo.othersolvable
</dl>
<p> The other involved Solvable (if any), e.g. the one containing providing the dependency for conflicts. </p>
<dl>
<dt>
<dd>
const char *problemstr();<br />
my $str = $ruleinfo-&gt;problemstr();<br />
str = ruleinfo.problemstr()<br />
          str = ruleinfo.problemstr()
</dl>
<p> A string describing the ruleinfo from a problem perspective. This probably only makes sense if the rule is part of a problem.</p>
<h2>THE SOLUTION CLASS</h2>
<p> A solution solves one specific problem. It consists of multiple solution elements that all need to be executed.</p>
<h3>ATTRIBUTES</h3>
<dl>
<dt>
<dd>
Solver *solv; /* read only */<br />
$solution-&gt;{solv} solution.solv<br />
    solution.solv
</dl>
<p> Back pointer to solver object. </p>
<dl>
<dt>
<dd>
Id problemid; /* read only */<br />
$solution-&gt;{problemid} solution.problemid<br />
    solution.problemid
</dl>
<p> Id of the problem the solution solves. </p>
<dl>
<dt>
<dd>
Id id; /* read only */<br />
$solution-&gt;{id} solution.id<br />
    solution.id
</dl>
<p> Id of the solution. The first solution has Id 1, they are numbered consecutively.</p>
<h3>METHODS</h3>
<dl>
<dt>
<dd>
Solutionelement *elements(bool expandreplaces = 0)<br />
    my @solutionelements = $solution-&gt;elements();<br />
solutionelements = solution.elements()<br />
                       solutionelements = solution.elements()
</dl>
<p> Return an array containing the elements describing what needs to be done to implement the specific solution. If expandreplaces is true, elements of type SOLVER_SOLUTION_REPLACE will be replaced by one or more elements replace elements describing the policy mismatches. </p>
<dl>
<dt>
<dd>
int element_count()<br />
    my $cnt = $solution-&gt;solution_count();<br />
cnt = solution.element_count()<br />
          cnt = solution.element_count()
</dl>
<p> Return the number of solution elements without creating objects. Note that the count does not match the number of objects returned by the elements() method of expandreplaces is set to true.</p>
<h2>THE SOLUTIONELEMENT CLASS</h2>
<p> A solution element describes a single action of a solution. The action is always either to remove one specific job or to add a new job that installs or erases a single specific package.</p>
<h3>ATTRIBUTES</h3>
<dl>
<dt>
<dd>
Solver *solv; /* read only */<br />
$solutionelement-&gt;{solv} solutionelement.solv<br />
    solutionelement.solv
</dl>
<p> Back pointer to solver object. </p>
<dl>
<dt>
<dd>
Id problemid; /* read only */<br />
$solutionelement-&gt;{problemid} solutionelement.problemid<br />
    solutionelement.problemid
</dl>
<p> Id of the problem the element (partly) solves. </p>
<dl>
<dt>
<dd>
Id solutionid; /* read only */<br />
$solutionelement-&gt;{solutionid} solutionelement.solutionid<br />
    solutionelement.solutionid
</dl>
<p> Id of the solution the element is a part of. </p>
<dl>
<dt>
<dd>
Id id; /* read only */<br />
$solutionelement-&gt;{id} solutionelement.id<br />
    solutionelement.id
</dl>
<p> Id of the solution element. The first element has Id 1, they are numbered consecutively. </p>
<dl>
<dt>
<dd>
Id type; /* read only */<br />
$solutionelement-&gt;{type} solutionelement.type<br />
    solutionelement.type
</dl>
<p> Type of the solution element. See the constant section of the solver class for the existing types. </p>
<dl>
<dt>
<dd>
Solvable *solvable; /* read only */<br />
$solutionelement-&gt;{solvable} solutionelement.solvable<br />
    solutionelement.solvable
</dl>
<p> The installed solvable that needs to be replaced for replacement elements. </p>
<dl>
<dt>
<dd>
Solvable *replacement; /* read only */<br />
$solutionelement-&gt;{replacement} solutionelement.replacement<br />
    solutionelement.replacement
</dl>
<p> The solvable that needs to be installed to fix the problem. </p>
<dl>
<dt>
<dd>
int jobidx; /* read only */<br />
$solutionelement-&gt;{jobidx} solutionelement.jobidx<br />
    solutionelement.jobidx
</dl>
<p> The index of the job that needs to be removed to fix the problem, or -1 if the element is of another type. Note that it&#8217;s better to change the job to SOLVER_NOOP type so that the numbering of other elements does not get disturbed. This method works both for types SOLVER_SOLUTION_JOB and SOLVER_SOLUTION_POOLJOB.</p>
<h3>METHODS</h3>
<dl>
<dt>
<dd>
Solutionelement *replaceelements()<br />
    my @solutionelements = $solutionelement-&gt;replaceelements();<br />
solutionelements = solutionelement.replaceelements()<br />
                       solutionelements = solutionelement.replaceelements()
</dl>
<p> If the solution element is of type SOLVER_SOLUTION_REPLACE, return an array of elements describing the policy mismatches, otherwise return a copy of the element. See also the &#8220;expandreplaces&#8221; option in the solution&#8217;s elements() method. </p>
<dl>
<dt>
<dd>
int illegalreplace()<br />
    my $illegal = $solutionelement-&gt;illegalreplace();<br />
illegal = solutionelement.illegalreplace()<br />
              illegal = solutionelement.illegalreplace()
</dl>
<p> Return an integer that contains the policy mismatch bits or-ed together, or zero if there was no policy mismatch. See the policy error constants in the solver class. </p>
<dl>
<dt>
<dd>
Job Job()<br />
    my $job = $solutionelement-&gt;Job();<br />
illegal = solutionelement.Job()<br />
              illegal = solutionelement.Job()
</dl>
<p> Create a job that implements the solution element. Add this job to the array of jobs for all elements of type different to SOLVER_SOLUTION_JOB and SOLVER_SOLUTION_POOLJOB. For the later two, a SOLVER_NOOB Job is created, you should replace the old job with the new one. </p>
<dl>
<dt>
<dd>
const char *str()<br />
    my $str = $solutionelement-&gt;str();<br />
str = solutionelement.str()<br />
          str = solutionelement.str()
</dl>
<p> A string describing the change the solution element consists of.</p>
<h2>THE TRANSACTION CLASS</h2>
<p> Transactions describe the output of a solver run. A transaction contains a number of transaction elements, each either the installation of a new package or the removal of an already installed package. The Transaction class supports a classify() method that puts the elements into different groups so that a transaction can be presented to the user in a meaningful way.</p>
<h3>CONSTANTS</h3>
<p> Transaction element types, both active and passive </p>
<p> <code>SOLVER_TRANSACTION_IGNORE</code></p>
<dl>
<dt>
<dd> This element does nothing. Used to map element types that do not match the view mode.</dl>
<p> <code>SOLVER_TRANSACTION_INSTALL</code></p>
<dl>
<dt>
<dd> This element installs a package.</dl>
<p> <code>SOLVER_TRANSACTION_ERASE</code></p>
<dl>
<dt>
<dd> This element erases a package.</dl>
<p> <code>SOLVER_TRANSACTION_MULTIINSTALL</code></p>
<dl>
<dt>
<dd> This element installs a package with a different version keeping the other versions installed.</dl>
<p> <code>SOLVER_TRANSACTION_MULTIREINSTALL</code></p>
<dl>
<dt>
<dd> This element reinstalls an installed package keeping the other versions installed.</dl>
<p> Transaction element types, active view </p>
<p> <code>SOLVER_TRANSACTION_REINSTALL</code></p>
<dl>
<dt>
<dd> This element re-installs a package, i.e. installs the same package again.</dl>
<p> <code>SOLVER_TRANSACTION_CHANGE</code></p>
<dl>
<dt>
<dd> This element installs a package with same name, version, architecture but different content.</dl>
<p> <code>SOLVER_TRANSACTION_UPGRADE</code></p>
<dl>
<dt>
<dd> This element installs a newer version of an installed package.</dl>
<p> <code>SOLVER_TRANSACTION_DOWNGRADE</code></p>
<dl>
<dt>
<dd> This element installs an older version of an installed package.</dl>
<p> <code>SOLVER_TRANSACTION_OBSOLETES</code></p>
<dl>
<dt>
<dd> This element installs a package that obsoletes an installed package.</dl>
<p> Transaction element types, passive view </p>
<p> <code>SOLVER_TRANSACTION_REINSTALLED</code></p>
<dl>
<dt>
<dd> This element re-installs a package, i.e. installs the same package again.</dl>
<p> <code>SOLVER_TRANSACTION_CHANGED</code></p>
<dl>
<dt>
<dd> This element replaces an installed package with one of the same name, version, architecture but different content.</dl>
<p> <code>SOLVER_TRANSACTION_UPGRADED</code></p>
<dl>
<dt>
<dd> This element replaces an installed package with a new version.</dl>
<p> <code>SOLVER_TRANSACTION_DOWNGRADED</code></p>
<dl>
<dt>
<dd> This element replaces an installed package with an old version.</dl>
<p> <code>SOLVER_TRANSACTION_OBSOLETED</code></p>
<dl>
<dt>
<dd> This element replaces an installed package with a package that obsoletes it.</dl>
<p> Pseudo element types for showing extra information used by classify() </p>
<p> <code>SOLVER_TRANSACTION_ARCHCHANGE</code></p>
<dl>
<dt>
<dd> This element replaces an installed package with a package of a different architecture.</dl>
<p> <code>SOLVER_TRANSACTION_VENDORCHANGE</code></p>
<dl>
<dt>
<dd> This element replaces an installed package with a package of a different vendor.</dl>
<p> Transaction mode flags </p>
<p> <code>SOLVER_TRANSACTION_SHOW_ACTIVE</code></p>
<dl>
<dt>
<dd> Filter for active view types. The default is to return passive view type, i.e. to show how the installed packages get changed.</dl>
<p> <code>SOLVER_TRANSACTION_SHOW_OBSOLETES</code></p>
<dl>
<dt>
<dd> Do not map the obsolete view type into INSTALL/ERASE elements.</dl>
<p> <code>SOLVER_TRANSACTION_SHOW_ALL</code></p>
<dl>
<dt>
<dd> If multiple packages replace an installed package, only the best of them is kept as OBSOLETE element, the other ones are mapped to INSTALL/ERASE elements. This is because most applications want to show just one package replacing the installed one. The SOLVER_TRANSACTION_SHOW_ALL makes the library keep all OBSOLETE elements.</dl>
<p> <code>SOLVER_TRANSACTION_SHOW_MULTIINSTALL</code></p>
<dl>
<dt>
<dd> The library maps MULTIINSTALL elements to simple INSTALL elements. This flag can be used to disable the mapping.</dl>
<p> <code>SOLVER_TRANSACTION_CHANGE_IS_REINSTALL</code></p>
<dl>
<dt>
<dd> Use this flag if you want to map CHANGE elements to the REINSTALL type.</dl>
<p> <code>SOLVER_TRANSACTION_OBSOLETE_IS_UPGRADE</code></p>
<dl>
<dt>
<dd> Use this flag if you want to map OBSOLETE elements to the UPGRADE type.</dl>
<p> <code>SOLVER_TRANSACTION_MERGE_ARCHCHANGES</code></p>
<dl>
<dt>
<dd> Do not add extra categories for every architecture change, instead cumulate them in one category.</dl>
<p> <code>SOLVER_TRANSACTION_MERGE_VENDORCHANGES</code></p>
<dl>
<dt>
<dd> Do not add extra categories for every vendor change, instead cumulate them in one category.</dl>
<p> <code>SOLVER_TRANSACTION_RPM_ONLY</code></p>
<dl>
<dt>
<dd> Special view mode that just returns IGNORE, ERASE, INSTALL, MULTIINSTALL elements. Useful if you want to find out what to feed to the underlying package manager.</dl>
<p> Transaction order flags </p>
<p> <code>SOLVER_TRANSACTION_KEEP_ORDERDATA</code></p>
<dl>
<dt>
<dd> Do not throw away the dependency graph used for ordering the transaction. This flag is needed if you want to do manual ordering.</dl>
<h3>ATTRIBUTES</h3>
<dl>
<dt>
<dd>
Pool *pool; /* read only */<br />
$trans-&gt;{pool} trans.pool<br />
    trans.pool
</dl>
<p> Back pointer to pool.</p>
<h3>METHODS</h3>
<dl>
<dt>
<dd>
bool isempty();<br />
$trans-&gt;isempty()<br />
    trans.isempty()<br />
        trans.isempty<br />
    ?
</dl>
<p> Returns true if the transaction does not do anything, i.e. has no elements. </p>
<dl>
<dt>
<dd>
Solvable *newsolvables();<br />
my @newsolvables = $trans-&gt;newsolvables();<br />
newsolvables = trans.newsolvables()<br />
                   newsolvables = trans.newsolvables()
</dl>
<p> Return all packages that are to be installed by the transaction. These are the packages that need to be downloaded from the repositories. </p>
<dl>
<dt>
<dd>
Solvable *keptsolvables();<br />
my @keptsolvables = $trans-&gt;keptsolvables();<br />
keptsolvables = trans.keptsolvables()<br />
                    keptsolvables = trans.keptsolvables()
</dl>
<p> Return all installed packages that the transaction will keep installed. </p>
<dl>
<dt>
<dd>
Solvable *steps();<br />
my @steps = $trans-&gt;steps();<br />
steps = trans.steps()<br />
            steps = trans.steps()
</dl>
<p> Return all solvables that need to be installed (if the returned solvable is not already installed) or erased (if the returned solvable is installed). A step is also called a transaction element. </p>
<dl>
<dt>
<dd>
int steptype(Solvable *solvable, int mode)<br />
    my $type = $trans-&gt;steptype($solvable, $mode);<br />
type = trans.steptype(solvable, mode)<br />
           type = trans.steptype(solvable, mode)
</dl>
<p> Return the transaction type of the specified solvable. See the CONSTANTS sections for the mode argument flags and the list of returned types. </p>
<dl>
<dt>
<dd>
TransactionClass *classify(int mode = 0)<br />
    my @classes = $trans-&gt;classify();<br />
classes = trans.classify()<br />
              classes = trans.classify()
</dl>
<p> Group the transaction elements into classes so that they can be displayed in a structured way. You can use various mapping mode flags to tweak the result to match your preferences, see the mode argument flag in the CONSTANTS section. See the TransactionClass class for how to deal with the returned objects. </p>
<dl>
<dt>
<dd>
Solvable othersolvable(Solvable *solvable);<br />
my $other = $trans-&gt;othersolvable($solvable);<br />
other = trans.othersolvable(solvable)<br />
            other = trans.othersolvable(solvable)
</dl>
<p> Return the &#8220;other&#8221; solvable for a given solvable. For installed packages the other solvable is the best package with the same name that replaces the installed package, or the best package of the obsoleting packages if the package does not get replaced by one with the same name. </p>
<p> For to be installed packages, the &#8220;other&#8221; solvable is the best installed package with the same name that will be replaced, or the best packages of all the packages that are obsoleted if the new package does not replace a package with the same name. </p>
<p> Thus, the &#8220;other&#8221; solvable is normally the package that is also shown for a given package. </p>
<dl>
<dt>
<dd>
Solvable *allothersolvables(Solvable *solvable);<br />
my @others = $trans-&gt;allothersolvables($solvable);<br />
others = trans.allothersolvables(solvable)<br />
             others = trans.allothersolvables(solvable)
</dl>
<p> For installed packages, returns all of the packages that replace us. For to be installed packages, returns all of the packages that the new package replaces. The special &#8220;other&#8221; solvable is always the first entry of the returned array. </p>
<dl>
<dt>
<dd>
int calc_installsizechange();<br />
my $change = $trans-&gt;calc_installsizechange();<br />
change = trans.calc_installsizechange()<br />
             change = trans.calc_installsizechange()
</dl>
<p> Return the size change of the installed system in kilobytes (kibibytes). </p>
<dl>
<dt>
<dd>
void order(int flags = 0);<br />
$trans-&gt;order();<br />
trans.order()<br />
    trans.order()
</dl>
<p> Order the steps in the transactions so that dependent packages are updated before packages that depend on them. For rpm, you can also use rpmlib&#8217;s ordering functionality, debian&#8217;s dpkg does not provide a way to order a transaction.</p>
<h3>ACTIVE/PASSIVE VIEW</h3>
<p> Active view lists what new packages get installed, while passive view shows what happens to the installed packages. Most often there&#8217;s not much difference between the two modes, but things get interesting if multiple packages get replaced by one new package. Say you have installed packages A-1-1 and B-1-1, and now install A-2-1 which has a new dependency that obsoletes B. The transaction elements will be </p>
<dl>
<dt>
<dd>
<pre>
updated   A-1-1 (other: A-2-1)
obsoleted B-1-1 (other: A-2-1)
</pre>
</dl>
<p> in passive mode, but </p>
<dl>
<dt>
<dd>
<pre>
update A-2-1 (other: A-1-1)
erase  B
</pre>
</dl>
<p> in active mode. If the mode contains SOLVER_TRANSACTION_SHOW_ALL, the passive mode list will be unchanged but the active mode list will just contain A-2-1.</p>
<h2>THE TRANSACTIONCLASS CLASS</h2>
<p> Objects of this type are returned by the classify() Transaction method.</p>
<h3>ATTRIBUTES</h3>
<dl>
<dt>
<dd>
Transaction *transaction; /* read only */<br />
$class-&gt;<br />
{<br />
    transaction<br />
}<br />
class.transaction class.transaction
</dl>
<p> Back pointer to transaction object. </p>
<dl>
<dt>
<dd>
int type; /* read only */<br />
$class-&gt;<br />
{<br />
    type<br />
}<br />
class.type class.type
</dl>
<p> The type of the transaction elements in the class. </p>
<dl>
<dt>
<dd>
int count; /* read only */<br />
$class-&gt;<br />
{<br />
    count<br />
}<br />
class.count class.count
</dl>
<p> The number of elements in the class. </p>
<dl>
<dt>
<dd>
const char *fromstr;<br />
$class-&gt;<br />
{<br />
    fromstr<br />
}<br />
class.fromstr class.fromstr
</dl>
<p> The old vendor or architecture. </p>
<dl>
<dt>
<dd>
const char *tostr;<br />
$class-&gt;<br />
{<br />
    tostr<br />
}<br />
class.tostr class.tostr
</dl>
<p> The new vendor or architecture. </p>
<dl>
<dt>
<dd>
Id fromid;<br />
$class-&gt;<br />
{<br />
    fromid<br />
}<br />
class.fromid class.fromid
</dl>
<p> The id of the old vendor or architecture. </p>
<dl>
<dt>
<dd>
Id toid;<br />
$class-&gt;<br />
{<br />
    toid<br />
}<br />
class.toid class.toid
</dl>
<p> The id of the new vendor or architecture.</p>
<h3>METHODS</h3>
<dl>
<dt>
<dd>
void solvables();<br />
my @solvables = $class-&gt;solvables();<br />
solvables = class.solvables()<br />
                solvables = class.solvables()
</dl>
<p> Return the solvables for all transaction elements in the class.</p>
<h2>CHECKSUMS</h2>
<p> Checksums (also called hashes) are used to make sure that downloaded data is not corrupt and also as a fingerprint mechanism to check if data has changed.</p>
<h3>CLASS METHODS</h3>
<dl>
<dt>
<dd>
Chksum Chksum(Id type)<br />
    my $chksum = solv::Chksum-&gt;new ($type);<br />
chksum = solv.Chksum(type)<br />
             chksum = Solv::Chksum.new(type)
</dl>
<p> Create a checksum object. Currently the following types are supported: </p>
<dl>
<dt>
<dd>
<pre>
<code>REPOKEY_TYPE_MD5</code>
<code>REPOKEY_TYPE_SHA1</code>
<code>REPOKEY_TYPE_SHA256</code>
</pre>
</dl>
<p> These keys are constants in the <code>solv</code> class. </p>
<dl>
<dt>
<dd>
Chksum Chksum(Id type, const char *hex)<br />
    my $chksum = solv::Chksum-&gt;new ($type, $hex);<br />
chksum = solv.Chksum(type, hex)<br />
             chksum = Solv::Chksum.new(type, hex)
</dl>
<p> Create an already finalized checksum object from a hex string. </p>
<dl>
<dt>
<dd>
Chksum Chksum_from_bin(Id type, char *bin)<br />
    my $chksum = solv::Chksum-&gt;from_bin($type, $bin);<br />
chksum = solv.Chksum.from_bin(type, bin)<br />
             chksum = Solv::Chksum.from_bin(type, bin)
</dl>
<p> Create an already finalized checksum object from a binary checksum.</p>
<h3>ATTRIBUTES</h3>
<dl>
<dt>
<dd>
Id type; /* read only */<br />
$chksum-&gt;{type} chksum.type<br />
    chksum.type
</dl>
<p> Return the type of the checksum object.</p>
<h3>METHODS</h3>
<dl>
<dt>
<dd>
void add(const char *str)<br />
    $chksum-&gt;add($str);<br />
chksum.add(str)<br />
    chksum.add(str)
</dl>
<p> Add a (binary) string to the checksum. </p>
<dl>
<dt>
<dd>
void add_fp(FILE *fp)<br />
    $chksum-&gt;add_fp($file);<br />
chksum.add_fp(file)<br />
    chksum.add_fp(file)
</dl>
<p> Add the contents of a file to the checksum. </p>
<dl>
<dt>
<dd>
void add_stat(const char *filename)<br />
    $chksum-&gt;add_stat($filename);<br />
chksum.add_stat(filename)<br />
    chksum.add_stat(filename)
</dl>
<p> Stat the file and add the dev/ino/size/mtime member to the checksum. If the stat fails, the members are zeroed. </p>
<dl>
<dt>
<dd>
void add_fstat(int fd)<br />
    $chksum-&gt;add_fstat($fd);<br />
chksum.add_fstat(fd)<br />
    chksum.add_fstat(fd)
</dl>
<p> Same as add_stat, but instead of the filename a file descriptor is used. </p>
<dl>
<dt>
<dd>
unsigned char *raw()<br />
    my $raw = $chksum-&gt;raw();<br />
raw = chksum.raw()<br />
          raw = chksum.raw()
</dl>
<p> Finalize the checksum and return the result as raw bytes. This means that the result can contain NUL bytes or unprintable characters. </p>
<dl>
<dt>
<dd>
const char *hex()<br />
    my $raw = $chksum-&gt;hex();<br />
raw = chksum.hex()<br />
          raw = chksum.hex()
</dl>
<p> Finalize the checksum and return the result as hex string. </p>
<dl>
<dt>
<dd>
const char *typestr()<br />
    my $typestr = $chksum-&gt;typestr();<br />
typestr = chksum.typestr<br />
              typestr = chksum.typestr
</dl>
<p> Return the type of the checksum as a string, e.g. &quot;sha256&quot;. </p>
<dl>
<dt>
<dd>
&lt;equality&gt;<br />
if ($chksum1 == $chksum2)<br />
if chksum1 == chksum2:<br />
if chksum1 == chksum2
</dl>
<p> Checksums are equal if they are of the same type and the finalized results are the same. </p>
<dl>
<dt>
<dd>
<pre>
<code>&lt;stringification&gt;</code>
my <i>$str</i> <code>=</code> <i>$chksum</i><code>-&gt;str</code>;
<i>str</i> <code>= str(</code><i>chksum</i><code>)</code>
<i>str</i> <code>=</code> <i>chksum</i><code>.to_s</code>
</pre>
</dl>
<p> If the checksum is finished, the checksum is returned as &quot;&lt;type&gt;:&lt;hex&gt;&quot; string. Otherwise &quot;&lt;type&gt;:unfinished&quot; is returned.</p>
<h2>FILE MANAGEMENT</h2>
<p> This functions were added because libsolv uses standard <code>FILE</code> pointers to read/write files, but languages like perl have their own implementation of files. The libsolv functions also support decompression and compression, the algorithm is selected by looking at the file name extension. </p>
<dl>
<dt>
<dd>
FILE *xfopen(char *fn, char *mode = &#8220;r&#8221;)<br />
    my $file = solv::xfopen($path);<br />
file = solv.xfopen(path)<br />
           file = Solv::xfopen(path)
</dl>
<p> Open a file at the specified path. The mode argument is passed on to the stdio library. </p>
<dl>
<dt>
<dd>
FILE *xfopen_fd(char *fn, int fileno)<br />
    my $file = solv::xfopen_fd($path, $fileno);<br />
file = solv.xfopen_fd(path, fileno)<br />
           file = Solv::xfopen_fd(path, fileno)
</dl>
<p> Create a file handle from the specified file descriptor. The path argument is only used to select the correct (de-)compression algorithm, use an empty path if you want to make sure to read/write raw data. The file descriptor is dup()ed before the file handle is created.</p>
<h3>METHODS</h3>
<dl>
<dt>
<dd>
int fileno()<br />
    my $fileno = $file-&gt;fileno();<br />
fileno = file.fileno()<br />
             fileno = file.fileno()
</dl>
<p> Return file file descriptor of the file. If the file is not open, -1 is returned. </p>
<dl>
<dt>
<dd>
<pre>
<code>void cloexec(bool</code> <i>state</i><code>)</code>
<i>$file</i><code>-&gt;cloexec(</code><i>$state</i><code>)</code>
<i>file</i><code>.cloexec(</code><i>state</i><code>)</code>
<i>file</i><code>.cloexec(</code><i>state</i><code>)</code>
</pre>
</dl>
<p> Set the close-on-exec flag of the file descriptor. The xfopen function returns files with close-on-exec turned on, so if you want to pass a file to some other process you need to call cloexec(0) before calling exec. </p>
<dl>
<dt>
<dd>
int dup()<br />
    my $fileno = $file-&gt;dup();<br />
fileno = file.dup()<br />
             fileno = file.dup()
</dl>
<p> Return a copy of the descriptor of the file. If the file is not open, -1 is returned. </p>
<dl>
<dt>
<dd>
bool flush()<br />
    $file-&gt;flush();<br />
file.flush()<br />
    file.flush()
</dl>
<p> Flush the file. Returns false if there was an error. Flushing a closed file always returns true. </p>
<dl>
<dt>
<dd>
bool close()<br />
    $file-&gt;close();<br />
file.close()<br />
    file.close()
</dl>
<p> Close the file. This is needed for languages like Ruby that do not destruct objects right after they are no longer referenced. In that case, it is good style to close open files so that the file descriptors are freed right away. Returns false if there was an error.</p>
<h2>THE REPODATA CLASS</h2>
<p> The Repodata stores attributes for packages and the repository itself, each repository can have multiple repodata areas. You normally only need to directly access them if you implement lazy downloading of repository data. Repodata areas are created by calling the repository&#8217;s add_repodata() method or by using repo_add methods without the REPO_REUSE_REPODATA or REPO_USE_LOADING flag.</p>
<h3>ATTRIBUTES</h3>
<dl>
<dt>
<dd>
Repo *repo; /* read only */<br />
$data-&gt;{repo} data.repo<br />
    data.repo
</dl>
<p> Back pointer to repository object. </p>
<dl>
<dt>
<dd>
Id id; /* read only */<br />
$data-&gt;{id} data.id<br />
    data.id
</dl>
<p> The id of the repodata area. Repodata ids of different repositories overlap.</p>
<h3>METHODS</h3>
<dl>
<dt>
<dd>
internalize();<br />
$data-&gt;internalize();<br />
data.internalize()<br />
    data.internalize()
</dl>
<p> Internalize newly added data. The lookup functions will only see the new data after it has been internalized. </p>
<dl>
<dt>
<dd>
bool write(FILE *fp);<br />
$data-&gt;write($fp);<br />
data.write(fp)<br />
    data.write(fp)
</dl>
<p> Write the contents of the repodata area as solv file. </p>
<dl>
<dt>
<dd>
bool add_solv(FILE *fp, int flags = 0);<br />
$data-&gt;add_solv($fp);<br />
data.add_solv(fp)<br />
    data.add_solv(fp)
</dl>
<p> Replace a stub repodata object with the data from a solv file. This method automatically adds the REPO_USE_LOADING flag. It should only be used from a load callback. </p>
<dl>
<dt>
<dd>
void create_stubs();<br />
$data-&gt;create_stubs()<br />
    data.create_stubs()<br />
        data.create_stubs()
</dl>
<p> Create stub repodatas from the information stored in the repodata meta area. </p>
<dl>
<dt>
<dd>
void extend_to_repo();<br />
$data-&gt;extend_to_repo();<br />
data.extend_to_repo()<br />
    data.extend_to_repo()
</dl>
<p> Extend the repodata so that it has the same size as the repo it belongs to. This method is only needed when switching to a just written repodata extension to make the repodata match the written extension (which is always of the size of the repo). </p>
<dl>
<dt>
<dd>
&lt;equality&gt;<br />
if ($data1 == $data2)<br />
if data1 == data2:<br />
if data1 == data2
</dl>
<p> Two repodata objects are equal if they belong to the same repository and have the same id.</p>
<h3>DATA RETRIEVAL METHODS</h3>
<dl>
<dt>
<dd>
const char *lookup_str(Id solvid, Id keyname)<br />
    my $string = $data-&gt;lookup_str($solvid, $keyname);<br />
string = data.lookup_str(solvid, keyname)<br />
             string = data.lookup_str(solvid, keyname)
</dl>
<dl>
<dt>
<dd>
Id *lookup_idarray(Id solvid, Id keyname)<br />
    my @ids = $data-&gt;lookup_idarray($solvid, $keyname);<br />
ids = data.lookup_idarray(solvid, keyname)<br />
          ids = data.lookup_idarray(solvid, keyname)
</dl>
<dl>
<dt>
<dd>
Chksum lookup_checksum(Id solvid, Id keyname)<br />
    my $chksum = $data-&gt;lookup_checksum($solvid, $keyname);<br />
chksum = data.lookup_checksum(solvid, keyname)<br />
             chksum = data.lookup_checksum(solvid, keyname)
</dl>
<p> Lookup functions. Return the data element stored in the specified solvable. The methods probably only make sense to retrieve data from the special SOLVID_META solvid that stores repodata meta information.</p>
<h3>DATA STORAGE METHODS</h3>
<dl>
<dt>
<dd>
void set_id(Id solvid, Id keyname, DepId id);<br />
$data-&gt;set_id($solvid, $keyname, $id);<br />
data.set_id(solvid, keyname, id)<br />
    data.set_id(solvid, keyname, id)
</dl>
<dl>
<dt>
<dd>
void set_str(Id solvid, Id keyname, const char *str);<br />
$data-&gt;set_str($solvid, $keyname, $str);<br />
data.set_str(solvid, keyname, str)<br />
    data.set_str(solvid, keyname, str)
</dl>
<dl>
<dt>
<dd>
void set_poolstr(Id solvid, Id keyname, const char *str);<br />
$data-&gt;set_poolstr($solvid, $keyname, $str);<br />
data.set_poolstr(solvid, keyname, str)<br />
    data.set_poolstr(solvid, keyname, str)
</dl>
<dl>
<dt>
<dd>
void set_checksum(Id solvid, Id keyname, Chksum *chksum);<br />
$data-&gt;set_checksum($solvid, $keyname, $chksum);<br />
data.set_checksum(solvid, keyname, chksum)<br />
    data.set_checksum(solvid, keyname, chksum)
</dl>
<dl>
<dt>
<dd>
void add_idarray(Id solvid, Id keyname, DepId id);<br />
$data-&gt;add_idarray($solvid, $keyname, $id);<br />
data.add_idarray(solvid, keyname, id)<br />
    data.add_idarray(solvid, keyname, id)
</dl>
<dl>
<dt>
<dd>
Id new_handle();<br />
my $handle = $data-&gt;new_handle();<br />
handle = data.new_handle()<br />
             handle = data.new_handle()
</dl>
<dl>
<dt>
<dd>
void add_flexarray(Id solvid, Id keyname, Id handle);<br />
$data-&gt;add_flexarray($solvid, $keyname, $handle);<br />
data.add_flexarray(solvid, keyname, handle)<br />
    data.add_flexarray(solvid, keyname, handle)
</dl>
<p> Data storage methods. Probably only useful to store data in the special SOLVID_META solvid that stores repodata meta information. Note that repodata areas can have their own Id pool (see the REPO_LOCALPOOL flag), so be careful if you need to store ids. Arrays are created by calling the add function for every element. A flexarray is an array of sub-structures, call new_handle to create a new structure, use the handle as solvid to fill the structure with data and call add_flexarray to put the structure in an array.</p>
<h2>THE DATAPOS CLASS</h2>
<p> Datapos objects describe a specific position in the repository data area. Thus they are only valid until the repository is modified in some way. Datapos objects can be created by the pos() and parentpos() methods of a Datamatch object or by accessing the &#8220;meta&#8221; attribute of a repository.</p>
<h3>ATTRIBUTES</h3>
<dl>
<dt>
<dd>
Repo *repo; /* read only */<br />
$data-&gt;{repo} data.repo<br />
    data.repo
</dl>
<p> Back pointer to repository object.</p>
<h3>METHODS</h3>
<dl>
<dt>
<dd>
Dataiterator(Id keyname, const char *match, int flags)<br />
    my $di = $datapos-&gt;Dataiterator($keyname, $match, $flags);<br />
di = datapos.Dataiterator(keyname, match, flags)<br />
         di = datapos.Dataiterator(keyname, match, flags)
</dl>
<p> Create a Dataiterator at the position of the datapos object. </p>
<dl>
<dt>
<dd>
const char *lookup_deltalocation(unsigned int *OUTPUT);<br />
my($location, $medianr) = $datapos-&gt;lookup_deltalocation();<br />
location, medianr = datapos.lookup_deltalocation() location, medianr = datapos.lookup_deltalocation()
</dl>
<p> Return a tuple containing the on-media location and an optional media number for a delta rpm. This obviously only works if the data position points to structure describing a delta rpm. </p>
<dl>
<dt>
<dd>
const char *lookup_deltaseq();<br />
my $seq = $datapos-&gt;lookup_deltaseq();<br />
seq = datapos.lookup_deltaseq();<br />
seq = datapos.lookup_deltaseq();
</dl>
<p> Return the delta rpm sequence from the structure describing a delta rpm.</p>
<h3>DATA RETRIEVAL METHODS</h3>
<dl>
<dt>
<dd>
const char *lookup_str(Id keyname)<br />
    my $string = $datapos-&gt;lookup_str($keyname);<br />
string = datapos.lookup_str(keyname)<br />
             string = datapos.lookup_str(keyname)
</dl>
<dl>
<dt>
<dd>
Id lookup_id(Id solvid, Id keyname)<br />
    my $id = $datapos-&gt;lookup_id($keyname);<br />
id = datapos.lookup_id(keyname)<br />
         id = datapos.lookup_id(keyname)
</dl>
<dl>
<dt>
<dd>
unsigned long long lookup_num(Id keyname, unsigned long long notfound = 0)<br />
    my $num = $datapos-&gt;lookup_num($keyname);<br />
num = datapos.lookup_num(keyname)<br />
          num = datapos.lookup_num(keyname)
</dl>
<dl>
<dt>
<dd>
bool lookup_void(Id keyname)<br />
    my $bool = $datapos-&gt;lookup_void($keyname);<br />
bool = datapos.lookup_void(keyname) bool = datapos.lookup_void(keyname)
</dl>
<dl>
<dt>
<dd>
Id *lookup_idarray(Id keyname)<br />
    my @ids = $datapos-&gt;lookup_idarray($keyname);<br />
ids = datapos.lookup_idarray(keyname)<br />
          ids = datapos.lookup_idarray(keyname)
</dl>
<dl>
<dt>
<dd>
Chksum lookup_checksum(Id keyname)<br />
    my $chksum = $datapos-&gt;lookup_checksum($keyname);<br />
chksum = datapos.lookup_checksum(keyname)<br />
             chksum = datapos.lookup_checksum(keyname)
</dl>
<p> Lookup functions. Note that the returned Ids are always translated into the Ids of the global pool even if the repodata area contains its own pool. </p>
<dl>
<dt>
<dd>
<pre><code>
Dataiterator Dataiterator(Id keyname, const char *match = 0, int flags = 0)
    my $di = $datapos-&gt;Dataiterator($keyname, $match, $flags);
di = datapos.Dataiterator(keyname, match, flags)
         di = datapos.Dataiterator(keyname, match, flags)
</code></pre>
</dl>
<dl>
<dt>
<dd>
<pre>
<code>for my</code> <i>$d</i> <code>(</code><i>@$di</i><code>)</code>
<code>for</code> <i>d</i> <code>in</code> <i>di</i><code>:</code>
<code>for</code> <i>d</i> <code>in</code> <i>di</i>
</pre>
</dl>
<p> Iterate over the matching data elements. See the Dataiterator class for more information.</p>
<h2>AUTHOR</h2>
<p> Michael Schroeder &lt;mls [at] suse.de&gt; </p>
<h2>Index</h2>
