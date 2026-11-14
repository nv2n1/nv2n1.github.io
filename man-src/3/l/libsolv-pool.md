---
title: "libsolv-pool(3)"
name: "libsolv-pool"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libsolv-pool/"
description: "libsolv-pool – Libsolv’s pool object"
---

<h2 class="name">NAME</h2>
<p> libsolv-pool &#8211; Libsolv&#8217;s pool object </p>
<h2>PUBLIC ATTRIBUTES</h2>
<p> <code>void *appdata</code></p>
<dl>
<dt>
<dd> A no-purpose pointer free to use for the library user. Freeing the pool simply discards the pointer.</dl>
<p> <code>Stringpool ss</code></p>
<dl>
<dt>
<dd> The pool of unified strings.</dl>
<p> <code>Reldep *rels</code></p>
<dl>
<dt>
<dd> The pool of unified relation dependencies.</dl>
<p> <code>int nrels</code></p>
<dl>
<dt>
<dd> Number of allocated relation dependencies.</dl>
<p> <code>Repo **repos</code></p>
<dl>
<dt>
<dd> The array of repository pointers, indexed by repository Id.</dl>
<p> <code>int nrepos</code></p>
<dl>
<dt>
<dd> Number of allocated repository array elements, i.e. the size of the repos array.</dl>
<p> <code>int urepos</code></p>
<dl>
<dt>
<dd> Number of used (i.e. non-zero) repository array elements.</dl>
<p> <code>Repo *installed</code></p>
<dl>
<dt>
<dd> Pointer to the repo holding the installed packages. You are free to read this attribute, but you should use pool_set_installed() if you want to change it.</dl>
<p> <code>Solvable *solvables</code></p>
<dl>
<dt>
<dd> The array of Solvable objects.</dl>
<p> <code>int nsolvables</code></p>
<dl>
<dt>
<dd> Number of Solvable objects, i.e. the size of the solvables array. Note that the array may contain freed solvables, in that case the repo pointer of the solvable will be zero.</dl>
<p> <code>int disttype</code></p>
<dl>
<dt>
<dd> The distribution type of your system, e.g. DISTTYPE_DEB. You are free to read this attribute, but you should use pool_setdisttype() if you want to change it.</dl>
<p> <code>Id *whatprovidesdata</code></p>
<dl>
<dt>
<dd> Multi-purpose Id storage holding zero terminated arrays of Ids. pool_whatprovides() returns an offset into this data.</dl>
<p> <code>Map *considered</code></p>
<dl>
<dt>
<dd> Optional bitmap that can make the library ignore solvables. If a bitmap is set, only solvables that have a set bit in the bitmap at their Id are considered usable.</dl>
<p> <code>int debugmask</code></p>
<dl>
<dt>
<dd> A mask that defines which debug events should be reported. pool_setdebuglevel() sets this mask.</dl>
<p> <code>Datapos pos</code></p>
<dl>
<dt>
<dd> An object storing some position in the repository data. Functions like dataiterator_set_pos() set this object, accessing data with a pseudo solvable Id of SOLVID_POS uses it.</dl>
<p> <code>Queue pooljobs</code></p>
<dl>
<dt>
<dd> A queue where fixed solver jobs can be stored. This jobs are automatically added when solver_solve() is called, they are useful to store configuration data like which packages should be multiversion installed.</dl>
<h2>CREATION AND DESTRUCTION</h2>
<dl>
<dt>
<dd>
<pre>
<code>Pool *pool_create()</code>;
</pre>
</dl>
<p> Create a new instance of a pool. </p>
<dl>
<dt>
<dd>
<pre><code>
void pool_free(Pool *pool);
</code></pre>
</dl>
<p> Free a pool and all of the data it contains, e.g. the solvables, repositories, strings.</p>
<h2>DEBUGGING AND ERROR REPORTING</h2>
<h3>Constants</h3>
<p> <code>SOLV_FATAL</code></p>
<dl>
<dt>
<dd> Report the error and call &#8220;<a href="/docs/linux/man/1-exit/">exit</a>(1)&#8221; afterwards. You cannot mask this level. Reports to stderr instead of stdout.</dl>
<p> <code>SOLV_ERROR</code></p>
<dl>
<dt>
<dd> Used to report errors. Reports to stderr instead of stdout.</dl>
<p> <code>SOLV_WARN</code></p>
<dl>
<dt>
<dd> Used to report warnings.</dl>
<p> <code>SOLV_DEBUG_STATS</code></p>
<dl>
<dt>
<dd> Used to report statistical data.</dl>
<p> <code>SOLV_DEBUG_RULE_CREATION</code></p>
<dl>
<dt>
<dd> Used to report information about the solver&#8217;s creation of rules.</dl>
<p> <code>SOLV_DEBUG_PROPAGATE</code></p>
<dl>
<dt>
<dd> Used to report information about the solver&#8217;s unit rule propagation process.</dl>
<p> <code>SOLV_DEBUG_ANALYZE</code></p>
<dl>
<dt>
<dd> Used to report information about the solver&#8217;s learnt rule generation mechanism.</dl>
<p> <code>SOLV_DEBUG_UNSOLVABLE</code></p>
<dl>
<dt>
<dd> Used to report information about the solver dealing with conflicting rules.</dl>
<p> <code>SOLV_DEBUG_SOLUTIONS</code></p>
<dl>
<dt>
<dd> Used to report information about the solver creating solutions to solve problems.</dl>
<p> <code>SOLV_DEBUG_POLICY</code></p>
<dl>
<dt>
<dd> Used to report information about the solver searching for an optimal solution.</dl>
<p> <code>SOLV_DEBUG_RESULT</code></p>
<dl>
<dt>
<dd> Used by the debug functions to output results.</dl>
<p> <code>SOLV_DEBUG_JOB</code></p>
<dl>
<dt>
<dd> Used to report information about the job rule generation process.</dl>
<p> <code>SOLV_DEBUG_SOLVER</code></p>
<dl>
<dt>
<dd> Used to report information about what the solver is currently doing.</dl>
<p> <code>SOLV_DEBUG_TRANSACTION</code></p>
<dl>
<dt>
<dd> Used to report information about the transaction generation and ordering process.</dl>
<p> <code>SOLV_DEBUG_TO_STDERR</code></p>
<dl>
<dt>
<dd> Write debug messages to stderr instead of stdout.</dl>
<h3>Functions</h3>
<dl>
<dt>
<dd>
void pool_debug(Pool *pool, int type, const char *format, &#8230;);
</dl>
<p> Report a message of the type <i>type</i>. You can filter debug messages by setting a debug mask. </p>
<dl>
<dt>
<dd>
void pool_setdebuglevel(Pool *pool, int level);
</dl>
<p> Set a predefined debug mask. A higher level generally means more bits in the mask are set, thus more messages are printed. </p>
<dl>
<dt>
<dd>
void pool_setdebugmask(Pool *pool, int mask);
</dl>
<p> Set the debug mask to filter debug messages. </p>
<dl>
<dt>
<dd>
int pool_error(Pool *pool, int ret, const char *format, &#8230;);
</dl>
<p> Set the pool&#8217;s error string. The <i>ret</i> value is simply used as a return value of the function so that you can write code like return pool_error(&#8230;);. If the debug mask contains the <code>SOLV_ERROR</code> bit, pool_debug() is also called with the message and type <code>SOLV_ERROR</code>. </p>
<dl>
<dt>
<dd>
extern char *pool_errstr(Pool *pool);
</dl>
<p> Return the current error string stored in the pool. Like with the libc&#8217;s errno value, the string is only meaningful after a function returned an error. </p>
<dl>
<dt>
<dd>
void pool_setdebugcallback(Pool *pool, void (*debugcallback)(Pool *, void *data, int type, const char *str), void *debugcallbackdata);
</dl>
<p> Set a custom debug callback function. Instead of writing to stdout or stderr, the callback function will be called.</p>
<h2>POOL CONFIGURATION</h2>
<h3>Constants</h3>
<p> <code>DISTTYPE_RPM</code></p>
<dl>
<dt>
<dd> Used for systems which use rpm as low level package manager.</dl>
<p> <code>DISTTYPE_DEB</code></p>
<dl>
<dt>
<dd> Used for systems which use dpkg as low level package manager.</dl>
<p> <code>DISTTYPE_ARCH</code></p>
<dl>
<dt>
<dd> Used for systems which use the arch linux package manager.</dl>
<p> <code>DISTTYPE_HAIKU</code></p>
<dl>
<dt>
<dd> Used for systems which use haiku packages.</dl>
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
<h3>Functions</h3>
<dl>
<dt>
<dd>
int pool_setdisttype(Pool *pool, int disttype);
</dl>
<p> Set the package type of your system. The disttype is used for example to define package comparison semantics. Libsolv&#8217;s default disttype should match the package manager of your system, so you only need to use this function if you want to use the library to solve packaging problems for different systems. The Function returns the old disttype on success, and -1 if the new disttype is not supported. </p>
<dl>
<dt>
<dd>
int pool_set_flag(Pool *pool, int flag, int value);
</dl>
<p> Set a flag to a new value. Returns the old value of the flag. </p>
<dl>
<dt>
<dd>
int pool_get_flag(Pool *pool, int flag);
</dl>
<p> Get the value of a pool flag. See the constants section about the meaning of the flags. </p>
<dl>
<dt>
<dd>
void pool_set_rootdir(Pool *pool, const char *rootdir);
</dl>
<p> Set a specific root directory. Some library functions support a flag that tells the function to prepend the rootdir to file and directory names. </p>
<dl>
<dt>
<dd>
const char *pool_get_rootdir(Pool *pool);
</dl>
<p> Return the current value of the root directory. </p>
<dl>
<dt>
<dd>
char *pool_prepend_rootdir(Pool *pool, const char *dir);
</dl>
<p> Prepend the root directory to the <i>dir</i> argument string. The returned string has been newly allocated and needs to be freed after use. </p>
<dl>
<dt>
<dd>
char *pool_prepend_rootdir_tmp(Pool *pool, const char *dir);
</dl>
<p> Same as pool_prepend_rootdir, but uses the pool&#8217;s temporary space for allocation. </p>
<dl>
<dt>
<dd>
void pool_set_installed(Pool *pool, Repo *repo);
</dl>
<p> Set which repository should be treated as the &#8220;installed&#8221; repository, i.e. the one that holds information about the installed packages. </p>
<dl>
<dt>
<dd>
void pool_set_languages(Pool *pool, const char **languages, int nlanguages);
</dl>
<p> Set the language of your system. The library provides lookup functions that return localized strings, for example for package descriptions. You can set an array of languages to provide a fallback mechanism if one language is not available. </p>
<dl>
<dt>
<dd>
void pool_setarch(Pool *pool, const char *arch);
</dl>
<p> Set the architecture of your system. The architecture is used to determine which packages are installable and which packages cannot be installed. The <i>arch</i> argument is normally the &#8220;machine&#8221; value of the &#8220;uname&#8221; system call. </p>
<dl>
<dt>
<dd>
void pool_setarchpolicy(Pool *, const char *);
</dl>
<p> Set the architecture policy for your system. This is the general version of pool_setarch (in fact pool_setarch calls pool_setarchpolicy internally). See the section about architecture policies for more information. </p>
<dl>
<dt>
<dd>
void pool_addvendorclass(Pool *pool, const char **vendorclass);
</dl>
<p> Add a new vendor equivalence class to the system. A vendor equivalence class defines if an installed package of one vendor can be replaced by a package coming from a different vendor. The <i>vendorclass</i> argument must be a NULL terminated array of strings. See the section about vendor policies for more information. </p>
<dl>
<dt>
<dd>
void pool_setvendorclasses(Pool *pool, const char **vendorclasses);
</dl>
<p> Set all allowed vendor equivalences. The vendorclasses argument must be an NULL terminated array consisting of all allowed classes concatenated. Each class itself must be NULL terminated, thus the last class ends with two NULL elements, one to finish the class and one to finish the list of classes. </p>
<dl>
<dt>
<dd>
void pool_set_custom_vendorcheck(Pool *pool, int (*vendorcheck)(Pool *, Solvable *, Solvable *));
</dl>
<p> Define a custom vendor check mechanism. You can use this if libsolv&#8217;s internal vendor equivalence class mechanism does not match your needs. </p>
<dl>
<dt>
<dd>
void pool_setloadcallback(Pool *pool, int (*cb)(Pool *, Repodata *, void *), void *loadcbdata);
</dl>
<p> Define a callback function that gets called when repository metadata needs to be loaded on demand. See the section about on demand loading in the libsolv-repodata manual. </p>
<dl>
<dt>
<dd>
void pool_setnamespacecallback(Pool *pool, Id (*cb)(Pool *, void *, Id, Id), void *nscbdata);
</dl>
<p> Define a callback function to implement custom namespace support. See the section about namespace dependencies.</p>
<h2>ID POOL MANAGEMENT</h2>
<h3>Constants</h3>
<p> <code>ID_EMPTY</code></p>
<dl>
<dt>
<dd> The Id of the empty string, it is always Id 1.</dl>
<p> <code>REL_LT</code></p>
<dl>
<dt>
<dd> Represents a &#8220;&lt;&#8221; relation.</dl>
<p> <code>REL_EQ</code></p>
<dl>
<dt>
<dd> Represents a &#8220;=&#8221; relation.</dl>
<p> <code>REL_GT</code></p>
<dl>
<dt>
<dd> Represents a &#8220;&gt;&#8221; relation. You can use combinations of REL_GT, REL_EQ, and REL_LT or-ed together to create any relation you like.</dl>
<p> <code>REL_AND</code></p>
<dl>
<dt>
<dd> A boolean AND operation, the &#8220;name&#8221; and &#8220;evr&#8221; parts of the relation can be two sub-dependencies. Packages must match both parts of the dependency.</dl>
<p> <code>REL_OR</code></p>
<dl>
<dt>
<dd> A boolean OR operation, the &#8220;name&#8221; and &#8220;evr&#8221; parts of the relation can be two sub-dependencies. Packages can match any part of the dependency.</dl>
<p> <code>REL_WITH</code></p>
<dl>
<dt>
<dd> Like REL_AND, but packages must match both dependencies simultaneously. See the section about boolean dependencies about more information.</dl>
<p> <code>REL_NAMESPACE</code></p>
<dl>
<dt>
<dd> A special namespace relation. See the section about namespace dependencies for more information.</dl>
<p> <code>REL_ARCH</code></p>
<dl>
<dt>
<dd> An architecture filter dependency. The &#8220;name&#8221; part of the relation is a sub-dependency, the &#8220;evr&#8221; part is the Id of an architecture that the matching packages must have (note that this is an exact match ignoring architecture policies).</dl>
<p> <code>REL_FILECONFLICT</code></p>
<dl>
<dt>
<dd> An internal file conflict dependency used to represent file conflicts. See the pool_add_fileconflicts_deps() function.</dl>
<p> <code>REL_COND</code></p>
<dl>
<dt>
<dd> A conditional dependency, the &#8220;name&#8221; sub-dependency is only considered if the &#8220;evr&#8221; sub-dependency is fulfilled. See the section about boolean dependencies about more information.</dl>
<p> <code>REL_COMPAT</code></p>
<dl>
<dt>
<dd> A compat dependency used in Haiku to represent version ranges. The &#8220;name&#8221; part is the actual version, the &#8220;evr&#8221; part is the backwards compatibility version.</dl>
<h3>Functions</h3>
<dl>
<dt>
<dd>
Id pool_str2id(Pool *pool, const char *str, int create);
</dl>
<p> Add a string to the pool of unified strings, returning the Id of the string. If <i>create</i> is zero, new strings will not be added to the pool, instead Id 0 is returned. </p>
<dl>
<dt>
<dd>
Id pool_strn2id(Pool *pool, const char *str, unsigned int len, int create);
</dl>
<p> Same as pool_str2id, but only <i>len</i> characters of the string are used. This can be used to add substrings to the pool. </p>
<dl>
<dt>
<dd>
Id pool_rel2id(Pool *pool, Id name, Id evr, int flags, int create);
</dl>
<p> Create a relational dependency from to other dependencies, <i>name</i> and <i>evr</i>, and a <i>flag</i>. See the <code>REL_</code> constants for the supported flags. As with pool_str2id, <i>create</i> defines if new dependencies will get added or Id zero will be returned instead. </p>
<dl>
<dt>
<dd>
Id pool_id2langid(Pool *pool, Id id, const char *lang, int create);
</dl>
<p> Attach a language suffix to a string Id. This function can be used to create language keyname Ids from keynames, it is functional equivalent to converting the <i>id</i> argument to a string, adding a &#8220;:&#8221; character and the <i>lang</i> argument to the string and then converting the result back into an Id. </p>
<dl>
<dt>
<dd>
const char *pool_id2str(const Pool *pool, Id id);
</dl>
<p> Convert an Id back into a string. If the Id is a relational Id, the &#8220;name&#8221; part will be converted instead. </p>
<dl>
<dt>
<dd>
const char *pool_id2rel(const Pool *pool, Id id);
</dl>
<p> Return the relation string of a relational Id. Returns an empty string if the passed Id is not a relation. </p>
<dl>
<dt>
<dd>
const char *pool_id2evr(const Pool *pool, Id id);
</dl>
<p> Return the &#8220;evr&#8221; part of a relational Id as string. Returns an empty string if the passed Id is not a relation. </p>
<dl>
<dt>
<dd>
const char *pool_dep2str(Pool *pool, Id id);
</dl>
<p> Convert an Id back into a string. If the passed Id belongs to a relation, a string representing the relation is returned. Note that in that case the string is allocated on the pool&#8217;s temporary space. </p>
<dl>
<dt>
<dd>
void pool_freeidhashes(Pool *pool);
</dl>
<p> Free the hashes used to unify strings and relations. You can use this function to save memory if you know that you will no longer create new strings and relations.</p>
<h2>SOLVABLE FUNCTIONS</h2>
<dl>
<dt>
<dd>
Solvable *pool_id2solvable(const Pool *pool, Id p);
</dl>
<p> Convert a solvable Id into a pointer to the solvable data. Note that the pointer may become invalid if new solvables are created or old solvables deleted, because the array storing all solvables may get reallocated. </p>
<dl>
<dt>
<dd>
const char *pool_solvid2str(Pool *pool, Id p);
</dl>
<p> Return a string representing the solvable with the Id <i>p</i>. The string will be some canonical representation of the solvable, usually a combination of the name, the version, and the architecture. </p>
<dl>
<dt>
<dd>
const char *pool_solvable2str(Pool *pool, Solvable *s);
</dl>
<p> Same as pool_solvid2str, but instead of the Id, a pointer to the solvable is passed.</p>
<h2>DEPENDENCY MATCHING</h2>
<h3>Constants</h3>
<p> <code>EVRCMP_COMPARE</code></p>
<dl>
<dt>
<dd> Compare all parts of the version, treat missing parts as empty strings.</dl>
<p> <code>EVRCMP_MATCH_RELEASE</code></p>
<dl>
<dt>
<dd> A special mode for rpm version string matching. If a version misses a release part, it matches all releases. In that case the special values &#8220;-2&#8221; and &#8220;2&#8221; are returned, depending on which of the two versions did not have a release part.</dl>
<p> <code>EVRCMP_MATCH</code></p>
<dl>
<dt>
<dd> A generic match, missing parts always match.</dl>
<p> <code>EVRCMP_COMPARE_EVONLY</code></p>
<dl>
<dt>
<dd> Only compare the epoch and the version parts, ignore the release part.</dl>
<h3>Functions</h3>
<dl>
<dt>
<dd>
int pool_evrcmp(const Pool *pool, Id evr1id, Id evr2id, int mode);
</dl>
<p> Compare two version Ids, return -1 if the first version is less than the second version, 0 if they are identical, and 1 if the first version is bigger than the second one. </p>
<dl>
<dt>
<dd>
int pool_evrcmp_str(const Pool *pool, const char *evr1, const char *evr2, int mode);
</dl>
<p> Same as pool_evrcmp(), but uses strings instead of Ids. </p>
<dl>
<dt>
<dd>
int pool_evrmatch(const Pool *pool, Id evrid, const char *epoch, const char *version, const char *release);
</dl>
<p> Match a version Id against an epoch, a version and a release string. Passing NULL means that the part should match everything. </p>
<dl>
<dt>
<dd>
int pool_match_dep(Pool *pool, Id d1, Id d2);
</dl>
<p> Returns &#8220;1&#8221; if the dependency <i>d1</i> (the provider) is matched by the dependency <i>d2</i>, otherwise &#8220;0&#8221; is returned. For two dependencies to match, both the &#8220;name&#8221; parts must match and the version range described by the &#8220;evr&#8221; parts must overlap. </p>
<dl>
<dt>
<dd>
int pool_match_nevr(Pool *pool, Solvable *s, Id d);
</dl>
<p> Like pool_match_dep, but the provider is the &quot;self-provides&quot; dependency of the Solvable <i>s</i>, i.e. the dependency &#8220;s→name = s→evr&#8221;.</p>
<h2>WHATPROVIDES INDEX</h2>
<dl>
<dt>
<dd>
void pool_createwhatprovides(Pool *pool);
</dl>
<p> Create an index that maps dependency Ids to sets of packages that provide the dependency. </p>
<dl>
<dt>
<dd>
void pool_freewhatprovides(Pool *pool);
</dl>
<p> Free the whatprovides index to save memory. </p>
<dl>
<dt>
<dd>
<pre>
<code>Id pool_whatprovides(Pool *</code><i>pool</i><code>, Id</code> <i>d</i><code>)</code>;
</pre>
</dl>
<p> Return an offset into the Pool&#8217;s whatprovidesdata array. The solvables with the Ids stored starting at that offset provide the dependency <i>d</i>. The solvable list is zero terminated. </p>
<dl>
<dt>
<dd>
<pre>
<code>Id *pool_whatprovides_ptr(Pool *</code><i>pool</i><code>, Id</code> <i>d</i><code>)</code>;
</pre>
</dl>
<p> Instead of returning the offset, return the pointer to the Ids stored at that offset. Note that this pointer has a very limit validity time, as any call that adds new values to the whatprovidesdata area may reallocate the array. </p>
<dl>
<dt>
<dd>
<pre>
<code>Id pool_queuetowhatprovides(Pool *</code><i>pool</i><code>, Queue *</code><i>q</i><code>)</code>;
</pre>
</dl>
<p> Add the contents of the Queue <i>q</i> to the end of the whatprovidesdata array, returning the offset into the array. </p>
<dl>
<dt>
<dd>
void pool_addfileprovides(Pool *pool);
</dl>
<p> Some package managers like rpm allow dependencies on files contained in other packages. To allow libsolv to deal with those dependencies in an efficient way, you need to call the addfileprovides method after creating and reading all repositories. This method will scan all dependency for file names and then scan all packages for matching files. If a filename has been matched, it will be added to the provides list of the corresponding package. </p>
<dl>
<dt>
<dd>
void pool_addfileprovides_queue(Pool *pool, Queue *idq, Queue *idqinst);
</dl>
<p> Same as pool_addfileprovides, but the added Ids are returned in two Queues, <i>idq</i> for all repositories except the one containing the &#8220;installed&#8221; packages, <i>idqinst</i> for the latter one. This information can be stored in the meta section of the repositories to speed up the next time the repository is loaded and addfileprovides is called </p>
<dl>
<dt>
<dd>
void pool_flush_namespaceproviders(Pool *pool, Id ns, Id evr);
</dl>
<p> Clear the cache of the providers for namespace dependencies matching namespace <i>ns</i>. If the <i>evr</i> argument is non-zero, the namespace dependency for exactly that dependency is cleared, otherwise all matching namespace dependencies are cleared. See the section about Namespace dependencies for further information. </p>
<dl>
<dt>
<dd>
void pool_add_fileconflicts_deps(Pool *pool, Queue *conflicts);
</dl>
<p> Some package managers like rpm report conflicts when a package installation overwrites a file of another installed package with different content. As file content information is not stored in the repository metadata, those conflicts can only be detected after the packages are downloaded. Libsolv provides a function to check for such conflicts, pool_findfileconflicts(). If conflicts are found, they can be added as special <code>REL_FILECONFLICT</code> provides dependencies, so that the solver will know about the conflict when it is re-run.</p>
<h2>UTILITY FUNCTIONS</h2>
<dl>
<dt>
<dd>
char *pool_alloctmpspace(Pool *pool, int len);
</dl>
<p> Allocate space on the pool&#8217;s temporary space area. This space has a limited lifetime, it will be automatically freed after a fixed amount (currently 16) of other pool_alloctmpspace() calls are done. </p>
<dl>
<dt>
<dd>
void pool_freetmpspace(Pool *pool, const char *space);
</dl>
<p> Give the space allocated with pool_alloctmpspace back to the system. You do not have to use this function, as the space is automatically reclaimed, but it can be useful to extend the lifetime of other pointers to the pool&#8217;s temporary space area. </p>
<dl>
<dt>
<dd>
const char *pool_bin2hex(Pool *pool, const unsigned char *buf, int len);
</dl>
<p> Convert some binary data to hexadecimal, returning a string allocated in the pool&#8217;s temporary space area. </p>
<dl>
<dt>
<dd>
char *pool_tmpjoin(Pool *pool, const char *str1, const char *str2, const char *str3);
</dl>
<p> Join three strings and return the result in the pool&#8217;s temporary space area. You can use NULL arguments if you just want to join less strings. </p>
<dl>
<dt>
<dd>
char *pool_tmpappend(Pool *pool, const char *str1, const char *str2, const char *str3);
</dl>
<p> Like pool_tmpjoin(), but if the first argument is the last allocated space in the pool&#8217;s temporary space area, it will be replaced with the result of the join and no new temporary space slot will be used. Thus you can join more than three strings by a combination of one pool_tmpjoin() and multiple pool_tmpappend() calls. Note that the <i>str1</i> pointer is no longer usable after the call.</p>
<h2>DATA LOOKUP</h2>
<h3>Constants</h3>
<p> <code>SOLVID_POS</code></p>
<dl>
<dt>
<dd> Use the data position stored in the pool for the lookup instead of looking up the data of a solvable.</dl>
<p> <code>SOLVID_META</code></p>
<dl>
<dt>
<dd> Use the data stored in the meta section of a repository (or repodata area) instead of looking up the data of a solvable. This constant does not work for the pool&#8217;s lookup functions, use it for the repo&#8217;s or repodata&#8217;s lookup functions instead. It&#8217;s just listed for completeness.</dl>
<h3>Functions</h3>
<dl>
<dt>
<dd>
const char *pool_lookup_str(Pool *pool, Id solvid, Id keyname);
</dl>
<p> Return the string value stored under the attribute <i>keyname</i> in solvable <i>solvid</i>. </p>
<dl>
<dt>
<dd>
unsigned long long pool_lookup_num(Pool *pool, Id solvid, Id keyname, unsigned long long notfound);
</dl>
<p> Return the 64bit unsigned number stored under the attribute <i>keyname</i> in solvable <i>solvid</i>. If no such number is found, the value of the <i>notfound</i> argument is returned instead. </p>
<dl>
<dt>
<dd>
<pre>
<code>Id pool_lookup_id(Pool *</code><i>pool</i><code>, Id</code> <i>solvid</i><code>, Id</code> <i>keyname</i><code>)</code>;
</pre>
</dl>
<p> Return the Id stored under the attribute <i>keyname</i> in solvable <i>solvid</i>. </p>
<dl>
<dt>
<dd>
int pool_lookup_idarray(Pool *pool, Id solvid, Id keyname, Queue *q);
</dl>
<p> Fill the queue <i>q</i> with the content of the Id array stored under the attribute <i>keyname</i> in solvable <i>solvid</i>. Returns &#8220;1&#8221; if an array was found, otherwise the queue will be empty and &#8220;0&#8221; will be returned. </p>
<dl>
<dt>
<dd>
int pool_lookup_void(Pool *pool, Id solvid, Id keyname);
</dl>
<p> Returns &#8220;1&#8221; if a void value is stored under the attribute <i>keyname</i> in solvable <i>solvid</i>, otherwise &#8220;0&#8221;. </p>
<dl>
<dt>
<dd>
const char *pool_lookup_checksum(Pool *pool, Id solvid, Id keyname, Id *typep);
</dl>
<p> Return the checksum that is stored under the attribute <i>keyname</i> in solvable <i>solvid</i>. The type of the checksum will be returned over the <i>typep</i> pointer. If no such checksum is found, NULL will be returned and the type will be set to zero. Note that the result is stored in the Pool&#8217;s temporary space area. </p>
<dl>
<dt>
<dd>
const unsigned char *pool_lookup_bin_checksum(Pool *pool, Id solvid, Id keyname, Id *typep);
</dl>
<p> Return the checksum that is stored under the attribute <i>keyname</i> in solvable <i>solvid</i>. Returns the checksum as binary data, you can use the returned type to calculate the length of the checksum. No temporary space area is needed. </p>
<dl>
<dt>
<dd>
const char *pool_lookup_deltalocation(Pool *pool, Id solvid, unsigned int *medianrp);
</dl>
<p> This is a utility lookup function to return the delta location for a delta rpm. As solvables cannot store deltas, you have to use SOLVID_POS as argument and set the Pool&#8217;s datapos pointer to point to valid delta rpm data. </p>
<dl>
<dt>
<dd>
void pool_search(Pool *pool, Id solvid, Id keyname, const char *match, int flags, int (*callback)(void *cbdata, Solvable *s, Repodata *data, Repokey *key, KeyValue *kv), void *cbdata);
</dl>
<p> Perform a search on all data stored in the pool. You can limit the search area by using the <i>solvid</i> and <i>keyname</i> arguments. The values can be optionally matched against the <i>match</i> argument, use NULL if you do not want this matching. See the Dataiterator manpage about the possible matches modes and the <i>flags</i> argument. For all (matching) values, the callback function is called with the <i>cbdata</i> callback argument and the data describing the value.</p>
<h2>JOB AND SELECTION FUNCTIONS</h2>
<p> A Job consists of two Ids, <i>how</i> and <i>what</i>. The <i>how</i> part describes the action, the job flags, and the selection method while the <i>what</i> part is in input for the selection. A Selection is a queue consisting of multiple jobs (thus the number of elements in the queue must be a multiple of two). See the Solver manpage for more information about jobs. </p>
<dl>
<dt>
<dd>
const char *pool_job2str(Pool *pool, Id how, Id what, Id flagmask);
</dl>
<p> Convert a job into a string. Useful for debugging purposes. The <i>flagmask</i> can be used to mask the flags of the job, use &#8220;0&#8221; if you do not want to see such flags, &#8220;-1&#8221; to see all flags, or a combination of the flags you want to see. </p>
<dl>
<dt>
<dd>
void pool_job2solvables(Pool *pool, Queue *pkgs, Id how, Id what);
</dl>
<p> Return a list of solvables that the specified job selects. </p>
<dl>
<dt>
<dd>
int pool_isemptyupdatejob(Pool *pool, Id how, Id what);
</dl>
<p> Return &#8220;1&#8221; if the job is an update job that does not work with any installed package, i.e. the job is basically a no-op. You can use this to turn no-op update jobs into install jobs (as done by package managers like &#8220;zypper&#8221;). </p>
<dl>
<dt>
<dd>
const char *pool_selection2str(Pool *pool, Queue *selection, Id flagmask);
</dl>
<p> Convert a selection into a string. Useful for debugging purposes. See the pool_job2str() function for the <i>flagmask</i> argument.</p>
<h2>ODDS AND ENDS</h2>
<dl>
<dt>
<dd>
void pool_freeallrepos(Pool *pool, int reuseids);
</dl>
<p> Free all repos from the pool (including all solvables). If <i>reuseids</i> is true, all Ids of the solvables are free to be reused the next time solvables are created. </p>
<dl>
<dt>
<dd>
<pre><code>
void pool_clear_pos(Pool *pool);
</code></pre>
</dl>
<p> Clear the data position stored in the pool.</p>
<h2>ARCHITECTURE POLICIES</h2>
<p> An architecture policy defines a list of architectures that can be installed on the system, and also the relationship between them (i.e. the ordering). Architectures can be delimited with three different characters: </p>
<p> <code>&#8216;:&#8217;</code></p>
<dl>
<dt>
<dd> No relationship between the architectures. A package of one architecture can not be replaced with one of the other architecture.</dl>
<p> <code>&#8216;&gt;&#8217;</code></p>
<dl>
<dt>
<dd> The first architecture is better than the second one. An installed package of the second architecture may be replaced with one from the first architecture and vice versa. The solver will select the better architecture if the versions are the same.</dl>
<p> <code>&#8216;=&#8217;</code></p>
<dl>
<dt>
<dd> The two architectures are freely exchangeable. Used to define aliases for architectures.</dl>
<p> An example would be &#8216;x86_64:i686=athlon&gt;i586&#8217;. This means that x86_64 packages can only be replaced by other x86_64 packages, i686 packages can be replaced by i686 and i586 packages (but i686 packages will be preferred) and athlon is another name for the i686 architecture. </p>
<p> You can turn off the architecture replacement checks with the Solver&#8217;s SOLVER_FLAG_ALLOW_ARCHCHANGE flag.</p>
<h2>VENDOR POLICIES</h2>
<p> Different vendors often compile packages with different features, so Libsolv only replace installed packages of one vendor with packages coming from the same vendor. Also, while the version of a package is normally defined by the upstream project, the release part of the version is set by the vendor&#8217;s package maintainer, so it&#8217;s not meaningful to do version comparisons for packages coming from different vendors. </p>
<p> Vendor in this case means the SOLVABLE_VENDOR string stored in each solvable. Sometimes a vendor changes names, or multiple vendors form a group that coordinate their package building, so libsolv offers a way to define that a group of vendors are compatible. You do that be defining vendor equivalence classes, packages from a vendor from one class may be replaced with packages from all the other vendors in the class. </p>
<p> There can be multiple equivalence classes, the set of allowed vendor changes for an installed package is calculated by building the union of all of the equivalence classes the vendor of the installed package is part of. </p>
<p> You can turn off the architecture replacement checks with the Solver&#8217;s SOLVER_FLAG_ALLOW_VENDORCHANGE flag.</p>
<h2>BOOLEAN DEPENDENCIES</h2>
<p> Boolean Dependencies allow to build complex expressions from simple dependencies. While rpm does not support boolean expressions in dependencies and debian only allows an &quot;OR&quot; expression, libsolv allows arbitrary complex expressions. The following basic types are supported: </p>
<p> <code>REL_OR</code></p>
<dl>
<dt>
<dd> The expression is true if either the first dependency or the second one is true. This is useful for package dependencies like &#8220;Requires&#8221;, where you can specify that either one of the packages need to be installed.</dl>
<p> <code>REL_AND</code></p>
<dl>
<dt>
<dd> The expression is true if both dependencies are true. The packages fulfilling the dependencies may be different, i.e. &#8220;Supplements: perl AND python&#8221; is true if both a package providing perl and a package providing python are installed. The solver currently only supports REL_AND in Supplements/Enhances dependencies, in other types of dependencies it gets treated as REL_WITH.</dl>
<p> <code>REL_WITH</code></p>
<dl>
<dt>
<dd> The expression is true if both dependencies are true and are fulfilled by the same package. Thus &#8220;Supplements: perl AND python&#8221; would only be true if a package is installed that provides both dependencies (some kind of multi-language interpreter).</dl>
<p> <code>REL_COND</code></p>
<dl>
<dt>
<dd> The expression is true if the first dependency is true or the second dependency is false. Libsolv currently does not support this type of dependency in the solver code.</dl>
<p> Each sub-dependency of a boolean dependency can in turn be a boolean dependency, so you can chain them to create complex dependencies.</p>
<h2>NAMESPACE DEPENDENCIES</h2>
<p> Namespace dependencies can be used to implement dependencies on attributes external to libsolv. An example would be a dependency on the language set by the user. This types of dependencies are usually only used for &#8220;Conflicts&#8221; or &#8220;Supplements&#8221; dependencies, as the underlying package manager does not know how to deal with them. </p>
<p> If the library needs to evaluate a namespace dependency, it calls the namespace callback function set in the pool. The callback function can return a set of packages that &#8220;provide&#8221; the dependency. If the dependency is provided by the system, the returned set should consist of just the system solvable (Solvable Id 1). </p>
<p> The returned set of packages must be returned as offset into the whatprovidesdata array. You can use the pool_queuetowhatprovides function to convert a queue into such an offset. To ease programming the callback function, the return values &#8220;0&#8221; and &#8220;1&#8221; are not interpreted as an offset. &#8220;0&#8221; means that no package is in the return set, &#8220;1&#8221; means that just the system solvable is in the set. </p>
<p> The returned set is cached, so that for each namespace dependency the callback is just called once. If you need to flush the cache (maybe because the user has selected a different language), use the pool_flush_namespaceproviders() function.</p>
<h2>AUTHOR</h2>
<p> Michael Schroeder &lt;mls [at] suse.de&gt; </p>
<h2>Index</h2>
