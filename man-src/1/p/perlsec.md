---
title: "perlsec(1)"
name: "perlsec"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlsec/"
description: "perlsec – Perl security"
---

<h2 class="name">NAME</h2>
<p> perlsec &#8211; Perl security </p>
<h2>DESCRIPTION</h2>
<p> Perl is designed to make it easy to program securely even when running with extra privileges, like setuid or setgid programs. Unlike most command line shells, which are based on multiple substitution passes on each line of the script, Perl uses a more conventional evaluation scheme with fewer hidden snags. Additionally, because the language has more builtin functionality, it can rely less upon external (and possibly untrustworthy) programs to accomplish its purposes.</p>
<h2>SECURITY VULNERABILITY CONTACT INFORMATION</h2>
<p> If you believe you have found a security vulnerability in Perl, please email the details to perl5-security-report [at] perl.org. This creates a new Request Tracker ticket in a special queue which isn&#8217;t initially publicly accessible. The email will also be copied to a closed subscription unarchived mailing list which includes all the core committers, who will be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN.</font> </p>
<p> When sending an initial request to the security email address, please don&#8217;t Cc any other parties, because if they reply to all, the reply will generate yet another new ticket. Once you have received an initial reply with a <tt>&quot;[perl #NNNNNN]&quot;</tt> ticket number in the headline, it&#8217;s okay to Cc subsequent replies to third parties: all emails to the perl5-security-report address with the ticket number in the subject line will be added to the ticket; without it, a new ticket will be created.</p>
<h2>SECURITY MECHANISMS AND CONCERNS</h2>
<h3>Taint mode</h3>
<p> Perl automatically enables a set of special security checks, called <i>taint mode</i>, when it detects its program running with differing real and effective user or group IDs. The setuid bit in Unix permissions is mode 04000, the setgid bit mode 02000; either or both may be set. You can also enable taint mode explicitly by using the <code>-T</code> command line flag. This flag is <i>strongly</i> suggested for server programs and any program run on behalf of someone else, such as a <font SIZE="-1">CGI</font> script. Once taint mode is on, it&#8217;s on for the remainder of your script. </p>
<p> While in this mode, Perl takes special precautions called <i>taint checks</i> to prevent both obvious and subtle traps. Some of these checks are reasonably simple, such as verifying that path directories aren&#8217;t writable by others; careful programmers have always used checks like these. Other checks, however, are best supported by the language itself, and it is these checks especially that contribute to making a set-id Perl program more secure than the corresponding C program. </p>
<p> You may not use data derived from outside your program to affect something else outside your program&#8212;at least, not by accident. All command line arguments, environment variables, locale information (see perllocale), results of certain system calls (<tt>&quot;readdir()&quot;</tt>, <tt>&quot;readlink()&quot;</tt>, the variable of <tt>&quot;shmread()&quot;</tt>, the messages returned by <tt>&quot;msgrcv()&quot;</tt>, the password, gcos and shell fields returned by the <tt>&quot;getpwxxx()&quot;</tt> calls), and all file input are marked as &#8220;tainted&#8221;. Tainted data may not be used directly or indirectly in any command that invokes a sub-shell, nor in any command that modifies files, directories, or processes, <code>with the following exceptions</code>:</p>
<dl>
<dt>&bull;</p>
<dd> Arguments to <tt>&quot;print&quot;</tt> and <tt>&quot;syswrite&quot;</tt> are <code>not</code> checked for taintedness.</p>
<dt>&bull;</p>
<dd> Symbolic methods </p>
<pre><code>
$obj-&gt;$method(@args);
</code></pre>
<p> and symbolic sub references </p>
<p>&amp;{$foo}(@args);<br />
$foo-&gt;(@args);</p>
<p> are not checked for taintedness. This requires extra carefulness unless you want external data to affect your control flow. Unless you carefully limit what these symbolic values are, people are able to call functions <code>outside</code> your Perl code, such as POSIX::system, in which case they are able to run arbitrary external code.</p>
<dt>&bull;</p>
<dd> Hash keys are <code>never</code> tainted.</dl>
<p> For efficiency reasons, Perl takes a conservative view of whether data is tainted. If an expression contains tainted data, any subexpression may be considered tainted, even if the value of the subexpression is not itself affected by the tainted data. </p>
<p> Because taintedness is associated with each scalar value, some elements of an array or hash can be tainted and others not. The keys of a hash are <code>never</code> tainted. </p>
<p> For example: </p>
<p>$arg = shift;<br />
#$arg is tainted<br />
    $hid = $arg.&#8217;bar&#8217;;<br />
#$hid is also tainted<br />
    $line = &lt; &gt;;<br />
#Tainted $line = &lt; STDIN&gt;;<br />
#Also tainted<br />
    open FOO,<br />
    &#8220;/home/me/bar&#8221; or die $ !;<br />
$line = &lt;FOO&gt;;<br />
#Still tainted<br />
    $path = $ENV{&#8216;PATH&#8217; };<br />
#Tainted, but see below<br />
              $data = &#8216;abc&#8217;;<br />
#Not tainted<br />
    system &#8220;echo $arg&#8221;;<br />
#Insecure system &#8220;/bin/echo&#8221;, $arg;<br />
#Considered insecure<br />
#(Perl doesn&#8217;t know about /bin/echo)<br />
    system &#8220;echo $hid&#8221;;<br />
#Insecure system &#8220;echo $data&#8221;;<br />
#Insecure until PATH set<br />
    $path = $ENV{&#8216;PATH&#8217; };<br />
#$path now tainted<br />
    $ENV{&#8216;PATH&#8217; } = &#8216;/bin:/usr/bin&#8217;;<br />
delete @ENV{&#8216;IFS&#8217;, &#8216;CDPATH&#8217;, &#8216;ENV&#8217;, &#8216;BASH_ENV&#8217;};<br />
$path = $ENV{&#8216;PATH&#8217;};<br />
#$path now NOT tainted<br />
    system &#8220;echo $data&#8221;;<br />
#Is secure now !open(FOO, &#8220;&lt; $arg&#8221;);<br />
#OK &#8211; read &#8211; only file open(FOO, &#8220;&gt; $arg&#8221;);<br />
#Not OK &#8211; trying to write<br />
              open(FOO, &#8220;echo $arg|&#8221;);<br />
#Not OK<br />
        open(FOO, &#8220;-|&#8221;) or<br />
    exec &#8216;echo&#8217;,<br />
    $arg;<br />
#Also not OK<br />
    $shout = `echo $arg`;<br />
#Insecure, $shout now tainted unlink $data, $arg;<br />
#Insecure umask $arg;<br />
#Insecure exec &#8220;echo $arg&#8221;;<br />
#Insecure exec &#8220;echo&#8221;, $arg;<br />
#Insecure exec &#8220;sh&#8221;, &#8216;-c&#8217;, $arg;<br />
#Very insecure !@files = &lt; *.c&gt;;<br />
#insecure(uses readdir() or similar)<br />
    @files = glob(&#8216;*.c&#8217;);<br />
#insecure(uses readdir() or similar)<br />
#In either case, the results of glob are tainted, since the list of<br />
#filenames comes from outside of the program.<br />
    $bad = ($arg, 23);<br />
#$bad will be tainted<br />
    $arg, `true`;<br />
#Insecure(although it isn&#8217;t really)</p>
<p> If you try to do something insecure, you will get a fatal error saying something like &#8220;Insecure dependency&#8221; or &#8220;Insecure <tt>$ENV</tt>{<font SIZE="-1">PATH</font>}&#8221;. </p>
<p> The exception to the principle of &#8220;one tainted value taints the whole expression&#8221; is with the ternary conditional operator <tt>&quot;?:&quot;</tt>. Since code with a ternary conditional </p>
<pre>
    $result = $tainted_value ? &quot;Untainted&quot; : &quot;Also untainted&quot;;
</pre>
<p> is effectively </p>
<p>if ($tainted_value) {<br />
    $result = &#8220;Untainted&#8221;;<br />
} else {<br />
    $result = &#8220;Also untainted&#8221;;<br />
}</p>
<p> it doesn&#8217;t make sense for <tt>$result</tt> to be tainted.</p>
<h3>Laundering and Detecting Tainted Data</h3>
<p> To test whether a variable contains tainted data, and whose use would thus trigger an &#8220;Insecure dependency&#8221; message, you can use the <tt>&quot;tainted()&quot;</tt> function of the Scalar::Util module, available in your nearby <font SIZE="-1">CPAN</font> mirror, and included in Perl starting from the release 5.8.0. Or you may be able to use the following <tt>&quot;is_tainted()&quot;</tt> function. </p>
<p>sub is_tainted<br />
{<br />
    local $ @;<br />
#Don &#8216;t pollute caller&#8217; s value.return !eval<br />
    {<br />
        eval(&#8220;#&#8221;.substr(join(&#8220;&#8221;, @_), 0, 0));<br />
        1<br />
    };<br />
}</p>
<p> This function makes use of the fact that the presence of tainted data anywhere within an expression renders the entire expression tainted. It would be inefficient for every operator to test every argument for taintedness. Instead, the slightly more efficient and conservative approach is used that if any tainted value has been accessed within the same expression, the whole expression is considered tainted. </p>
<p> But testing for taintedness gets you only so far. Sometimes you have just to clear your data&#8217;s taintedness. Values may be untainted by using them as keys in a hash; otherwise the only way to bypass the tainting mechanism is by referencing subpatterns from a regular expression match. Perl presumes that if you reference a substring using <tt>$1</tt>, <tt>$2</tt>, etc. in a non-tainting pattern, that you knew what you were doing when you wrote that pattern. That means using a bit of thought&#8212;don&#8217;t just blindly untaint anything, or you defeat the entire mechanism. It&#8217;s better to verify that the variable has only good characters (for certain values of &#8220;good&#8221;) rather than checking whether it has any bad characters. That&#8217;s because it&#8217;s far too easy to miss bad characters that you never thought of. </p>
<p> Here&#8217;s a test to make sure that the data contains nothing but &#8220;word&#8221; characters (alphabetics, numerics, and underscores), a hyphen, an at sign, or a dot. </p>
<p>if ($data = ~ / ^([-\@\w.] +) $ /) {<br />
    $data = $1;<br />
#$data now untainted<br />
} else {<br />
    die &#8220;Bad data in &#8216;$data'&#8221;;<br />
#log this somewhere<br />
}</p>
<p> This is fairly secure because <tt>&quot;/\w+/&quot;</tt> doesn&#8217;t normally match shell metacharacters, nor are dot, dash, or at going to mean something special to the shell. Use of <tt>&quot;/.+/&quot;</tt> would have been insecure in theory because it lets everything through, but Perl doesn&#8217;t check for that. The lesson is that when untainting, you must be exceedingly careful with your patterns. Laundering data using regular expression is the <i>only</i> mechanism for untainting dirty data, unless you use the strategy detailed below to fork a child of lesser privilege. </p>
<p> The example does not untaint <tt>$data</tt> if <tt>&quot;use locale&quot;</tt> is in effect, because the characters matched by <tt>&quot;\w&quot;</tt> are determined by the locale. Perl considers that locale definitions are untrustworthy because they contain data from outside the program. If you are writing a locale-aware program, and want to launder data with a regular expression containing <tt>&quot;\w&quot;</tt>, put <tt>&quot;no locale&quot;</tt> ahead of the expression in the same block. See &#8220;<font SIZE="-1">SECURITY&#8221;</font> in perllocale for further discussion and examples.</p>
<h3>Switches On the #! Line</h3>
<p> When you make a script executable, in order to make it usable as a command, the system will pass switches to perl from the script&#8217;s #! line. Perl checks that any command line switches given to a setuid (or setgid) script actually match the ones set on the #! line. Some Unix and Unix-like environments impose a one-switch limit on the #! line, so you may need to use something like <tt>&quot;-wU&quot;</tt> instead of <tt>&quot;-w -U&quot;</tt> under such systems. (This issue should arise only in Unix or Unix-like environments that support #! and setuid or setgid scripts.)</p>
<h3>Taint mode and @INC</h3>
<p> When the taint mode (<tt>&quot;-T&quot;</tt>) is in effect, the &#8220;.&#8221; directory is removed from <tt>@INC</tt>, and the environment variables <tt>&quot;PERL5LIB&quot;</tt> and <tt>&quot;PERLLIB&quot;</tt> are ignored by Perl. You can still adjust <tt>@INC</tt> from outside the program by using the <tt>&quot;-I&quot;</tt> command line option as explained in perlrun. The two environment variables are ignored because they are obscured, and a user running a program could be unaware that they are set, whereas the <tt>&quot;-I&quot;</tt> option is clearly visible and therefore permitted. </p>
<p> Another way to modify <tt>@INC</tt> without modifying the program, is to use the <tt>&quot;lib&quot;</tt> pragma, e.g.: </p>
<pre>
  perl -Mlib=/foo program
</pre>
<p> The benefit of using <tt>&quot;-Mlib=/foo&quot;</tt> over <tt>&quot;-I/foo&quot;</tt>, is that the former will automagically remove any duplicated directories, while the latter will not. </p>
<p> Note that if a tainted string is added to <tt>@INC</tt>, the following problem will be reported: </p>
<pre>
  Insecure dependency in require while running with -T switch
</pre>
<h3>Cleaning Up Your Path</h3>
<p> For &quot;Insecure <tt>$ENV{PATH}</tt>&quot; messages, you need to set <tt>$ENV{'PATH'}</tt> to a known value, and each directory in the path must be absolute and non-writable by others than its owner and group. You may be surprised to get this message even if the pathname to your executable is fully qualified. This is <i>not</i> generated because you didn&#8217;t supply a full path to the program; instead, it&#8217;s generated because you never set your <font SIZE="-1">PATH</font> environment variable, or you didn&#8217;t set it to something that was safe. Because Perl can&#8217;t guarantee that the executable in question isn&#8217;t itself going to turn around and execute some other program that is dependent on your <font SIZE="-1">PATH,</font> it makes sure you set the <font SIZE="-1">PATH.</font> </p>
<p> The <font SIZE="-1">PATH</font> isn&#8217;t the only environment variable which can cause problems. Because some shells may use the variables <font SIZE="-1">IFS, CDPATH, ENV,</font> and <font SIZE="-1">BASH_ENV,</font> Perl checks that those are either empty or untainted when starting subprocesses. You may wish to add something like this to your setid and taint-checking scripts. </p>
<pre>
    delete @ENV{qw(IFS CDPATH ENV BASH_ENV)};   # Make %ENV safer
</pre>
<p> It&#8217;s also possible to get into trouble with other operations that don&#8217;t care whether they use tainted values. Make judicious use of the file tests in dealing with any user-supplied filenames. When possible, do opens and such <code>after</code> properly dropping any special user (or group!) privileges. Perl doesn&#8217;t prevent you from opening tainted filenames for reading, so be careful what you print out. The tainting mechanism is intended to prevent stupid mistakes, not to remove the need for thought. </p>
<p> Perl does not call the shell to expand wild cards when you pass <tt>&quot;system&quot;</tt> and <tt>&quot;exec&quot;</tt> explicit parameter lists instead of strings with possible shell wildcards in them. Unfortunately, the <tt>&quot;open&quot;</tt>, <tt>&quot;glob&quot;</tt>, and backtick functions provide no such alternate calling convention, so more subterfuge will be required. </p>
<p> Perl provides a reasonably safe way to open a file or pipe from a setuid or setgid program: just create a child process with reduced privilege who does the dirty work for you. First, fork a child using the special <tt>&quot;open&quot;</tt> syntax that connects the parent and child by a pipe. Now the child resets its <font SIZE="-1">ID</font> set and any other per-process attributes, like environment variables, umasks, current working directories, back to the originals or known safe values. Then the child process, which no longer has any special permissions, does the <tt>&quot;open&quot;</tt> or other system call. Finally, the child passes the data it managed to access back to the parent. Because the file or pipe was opened in the child while running under less privilege than the parent, it&#8217;s not apt to be tricked into doing something it shouldn&#8217;t. </p>
<p> Here&#8217;s a way to do backticks reasonably safely. Notice how the <tt>&quot;exec&quot;</tt> is not called with a string that the shell could expand. This is by far the best way to call something that might be subjected to shell escapes: just never call the shell at all. </p>
<p>use English;<br />
die &#8220;Can&#8217;t fork: $!&#8221; unless defined($pid = open(KID, &#8220;-|&#8221;));<br />
if ($pid) {<br />
#parent while (&lt;KID&gt;){<br />
#do something<br />
    } close KID;<br />
} else {<br />
    my @temp = ($EUID, $EGID);<br />
    my $orig_uid = $UID;<br />
    my $orig_gid = $GID;<br />
    $EUID = $UID;<br />
    $EGID = $GID;<br />
#Drop privileges<br />
    $UID = $orig_uid;<br />
    $GID = $orig_gid;<br />
#Make sure privs are really gone<br />
    ($EUID, $EGID) = @temp;<br />
    die &#8220;Can&#8217;t drop privileges&#8221; unless $UID == $EUID &amp;&amp;$GID eq $EGID;<br />
    $ENV{PATH} = &#8220;/bin:/usr/bin&#8221;;<br />
#Minimal PATH.<br />
#Consider sanitizing the environment even more.<br />
        exec &#8216;myprog&#8217;,<br />
        &#8216;arg1&#8217;, &#8216;arg2&#8217; or die &#8220;can&#8217;t exec myprog: $!&#8221;;<br />
}</p>
<p> A similar strategy would work for wildcard expansion via <tt>&quot;glob&quot;</tt>, although you can use <tt>&quot;readdir&quot;</tt> instead. </p>
<p> Taint checking is most useful when although you trust yourself not to have written a program to give away the farm, you don&#8217;t necessarily trust those who end up using it not to try to trick it into doing something bad. This is the kind of security checking that&#8217;s useful for set-id programs and programs launched on someone else&#8217;s behalf, like <font SIZE="-1">CGI</font> programs. </p>
<p> This is quite different, however, from not even trusting the writer of the code not to try to do something evil. That&#8217;s the kind of trust needed when someone hands you a program you&#8217;ve never seen before and says, &#8220;Here, run this.&#8221; For that kind of safety, you might want to check out the Safe module, included standard in the Perl distribution. This module allows the programmer to set up special compartments in which all system operations are trapped and namespace access is carefully controlled. Safe should not be considered bullet-proof, though: it will not prevent the foreign code to set up infinite loops, allocate gigabytes of memory, or even abusing perl bugs to make the host interpreter crash or behave in unpredictable ways. In any case it&#8217;s better avoided completely if you&#8217;re really concerned about security.</p>
<h3>Shebang Race Condition</h3>
<p> Beyond the obvious problems that stem from giving special privileges to systems as flexible as scripts, on many versions of Unix, set-id scripts are inherently insecure right from the start. The problem is a race condition in the kernel. Between the time the kernel opens the file to see which interpreter to run and when the (now-set-id) interpreter turns around and reopens the file to interpret it, the file in question may have changed, especially if you have symbolic links on your system. </p>
<p> Some Unixes, especially more recent ones, are free of this inherent security bug. On such systems, when the kernel passes the name of the set-id script to open to the interpreter, rather than using a pathname subject to meddling, it instead passes <i>/dev/fd/3</i>. This is a special file already opened on the script, so that there can be no race condition for evil scripts to exploit. On these systems, Perl should be compiled with <tt>&quot;-DSETUID_SCRIPTS_ARE_SECURE_NOW&quot;</tt>. The <i>Configure</i> program that builds Perl tries to figure this out for itself, so you should never have to specify this yourself. Most modern releases of SysVr4 and <font SIZE="-1">BSD 4.4</font> use this approach to avoid the kernel race condition. </p>
<p> If you don&#8217;t have the safe version of set-id scripts, all is not lost. Sometimes this kernel &#8220;feature&#8221; can be disabled, so that the kernel either doesn&#8217;t run set-id scripts with the set-id or doesn&#8217;t run them at all. Either way avoids the exploitability of the race condition, but doesn&#8217;t help in actually running scripts set-id. </p>
<p> If the kernel set-id script feature isn&#8217;t disabled, then any set-id script provides an exploitable vulnerability. Perl can&#8217;t avoid being exploitable, but will point out vulnerable scripts where it can. If Perl detects that it is being applied to a set-id script then it will complain loudly that your set-id script is insecure, and won&#8217;t run it. When Perl complains, you need to remove the set-id bit from the script to eliminate the vulnerability. Refusing to run the script doesn&#8217;t in itself close the vulnerability; it is just Perl&#8217;s way of encouraging you to do this. </p>
<p> To actually run a script set-id, if you don&#8217;t have the safe version of set-id scripts, you&#8217;ll need to put a C wrapper around the script. A C wrapper is just a compiled program that does nothing except call your Perl program. Compiled programs are not subject to the kernel bug that plagues set-id scripts. Here&#8217;s a simple wrapper, written in C: </p>
<pre><code>
#include &lt;errno.h&gt;
#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include &lt;unistd.h&gt;
#define REAL_PATH "/path/to/script"
int main(int argc, char **argv)
{
    execv(REAL_PATH, argv);
    fprintf(stderr, "%s: %s: %s
",
            argv[0], REAL_PATH, strerror(errno));
    return 127;
}
</code></pre>
<p> Compile this wrapper into a binary executable and then make <i>it</i> rather than your script setuid or setgid. Note that this wrapper isn&#8217;t doing anything to sanitise the execution environment other than ensuring that a safe path to the script is used. It only avoids the shebang race condition. It relies on Perl&#8217;s own features, and on the script itself being careful, to make it safe enough to run the script set-id.</p>
<h3>Protecting Your Programs</h3>
<p> There are a number of ways to hide the source to your Perl programs, with varying levels of &#8220;security&#8221;. </p>
<p> First of all, however, you <i>can&#8217;t</i> take away read permission, because the source code has to be readable in order to be compiled and interpreted. (That doesn&#8217;t mean that a <font SIZE="-1">CGI</font> script&#8217;s source is readable by people on the web, though.) So you have to leave the permissions at the socially friendly 0755 level. This lets people on your local system only see your source. </p>
<p> Some people mistakenly regard this as a security problem. If your program does insecure things, and relies on people not knowing how to exploit those insecurities, it is not secure. It is often possible for someone to determine the insecure things and exploit them without viewing the source. Security through obscurity, the name for hiding your bugs instead of fixing them, is little security indeed. </p>
<p> You can try using encryption via source filters (Filter::* from <font SIZE="-1">CPAN,</font> or Filter::Util::Call and Filter::Simple since Perl 5.8). But crackers might be able to decrypt it. You can try using the byte code compiler and interpreter described below, but crackers might be able to de-compile it. You can try using the native-code compiler described below, but crackers might be able to disassemble it. These pose varying degrees of difficulty to people wanting to get at your code, but none can definitively conceal it (this is true of every language, not just Perl). </p>
<p> If you&#8217;re concerned about people profiting from your code, then the bottom line is that nothing but a restrictive license will give you legal security. License your software and pepper it with threatening statements like &#8220;This is unpublished proprietary software of <font SIZE="-1">XYZ</font> Corp. Your access to it does not give you permission to use it blah blah blah.&#8221; You should see a lawyer to be sure your license&#8217;s wording will stand up in court.</p>
<h3>Unicode</h3>
<p> Unicode is a new and complex technology and one may easily overlook certain security pitfalls. See perluniintro for an overview and perlunicode for details, and &#8220;Security Implications of Unicode&#8221; in perlunicode for security implications in particular.</p>
<h3>Algorithmic Complexity Attacks</h3>
<p> Certain internal algorithms used in the implementation of Perl can be attacked by choosing the input carefully to consume large amounts of either time or space or both. This can lead into the so-called <i>Denial of Service</i> (DoS) attacks.</p>
<dl>
<dt>&bull;</p>
<dd> Hash Algorithm &#8211; Hash algorithms like the one used in Perl are well known to be vulnerable to collision attacks on their hash function. Such attacks involve constructing a set of keys which collide into the same bucket producing inefficient behavior. Such attacks often depend on discovering the seed of the hash function used to map the keys to buckets. That seed is then used to brute-force a key set which can be used to mount a denial of service attack. In Perl 5.8.1 changes were introduced to harden Perl to such attacks, and then later in Perl 5.18.0 these features were enhanced and additional protections added. </p>
<p> At the time of this writing, Perl 5.18.0 is considered to be well-hardened against algorithmic complexity attacks on its hash implementation. This is largely owed to the following measures mitigate attacks:</p>
<dl>
<dt>
<dd>
<dl>
<dt>Hash Seed Randomization</p>
<dd> In order to make it impossible to know what seed to generate an attack key set for, this seed is randomly initialized at process start. This may be overridden by using the <font SIZE="-1">PERL_HASH_SEED</font> environment variable, see &#8220;<font SIZE="-1">PERL_HASH_SEED&#8221;</font> in perlrun. This environment variable controls how items are actually stored, not how they are presented via <tt>&quot;keys&quot;</tt>, <tt>&quot;values&quot;</tt> and <tt>&quot;each&quot;</tt>.</p>
<dt>Hash Traversal Randomization</p>
<dd> Independent of which seed is used in the hash function, <tt>&quot;keys&quot;</tt>, <tt>&quot;values&quot;</tt>, and <tt>&quot;each&quot;</tt> return items in a per-hash randomized order. Modifying a hash by insertion will change the iteration order of that hash. This behavior can be overridden by using <tt>&quot;hash_traversal_mask()&quot;</tt> from Hash::Util or by using the <font SIZE="-1">PERL_PERTURB_KEYS</font> environment variable, see &#8220;<font SIZE="-1">PERL_PERTURB_KEYS&#8221;</font> in perlrun. Note that this feature controls the &#8220;visible&#8221; order of the keys, and not the actual order they are stored in.</p>
<dt>Bucket Order Perturbance</p>
<dd> When items collide into a given hash bucket the order they are stored in the chain is no longer predictable in Perl 5.18. This has the intention to make it harder to observe a collision. This behavior can be overridden by using the <font SIZE="-1">PERL_PERTURB_KEYS</font> environment variable, see &#8220;<font SIZE="-1">PERL_PERTURB_KEYS&#8221;</font> in perlrun.</p>
<dt>New Default Hash Function</p>
<dd> The default hash function has been modified with the intention of making it harder to infer the hash seed.</p>
<dt>Alternative Hash Functions</p>
<dd> The source code includes multiple hash algorithms to choose from. While we believe that the default perl hash is robust to attack, we have included the hash function Siphash as a fall-back option. At the time of release of Perl 5.18.0 Siphash is believed to be of cryptographic strength. This is not the default as it is much slower than the default hash.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Without compiling a special Perl, there is no way to get the exact same behavior of any versions prior to Perl 5.18.0. The closest one can get is by setting <font SIZE="-1">PERL_PERTURB_KEYS</font> to 0 and setting the <font SIZE="-1">PERL_HASH_SEED</font> to a known value. We do not advise those settings for production use due to the above security considerations. </p>
<p> <code>Perl has never guaranteed any ordering of the hash keys</code>, and the ordering has already changed several times during the lifetime of Perl 5. Also, the ordering of hash keys has always been, and continues to be, affected by the insertion order and the history of changes made to the hash over its lifetime. </p>
<p> Also note that while the order of the hash elements might be randomized, this &#8220;pseudo-ordering&#8221; should <code>not</code> be used for applications like shuffling a list randomly (use <tt>&quot;List::Util::shuffle()&quot;</tt> for that, see List::Util, a standard core module since Perl 5.8.0; or the <font SIZE="-1">CPAN</font> module <tt>&quot;Algorithm::Numerical::Shuffle&quot;</tt>), or for generating permutations (use e.g. the <font SIZE="-1">CPAN</font> modules <tt>&quot;Algorithm::Permute&quot;</tt> or <tt>&quot;Algorithm::FastPermute&quot;</tt>), or for any cryptographic applications. </p>
<p> Tied hashes may have their own ordering and algorithmic complexity attacks.</dl>
<dt>&bull;</p>
<dd> Regular expressions &#8211; Perl&#8217;s regular expression engine is so called <font SIZE="-1">NFA</font> (Non-deterministic Finite Automaton), which among other things means that it can rather easily consume large amounts of both time and space if the regular expression may match in several ways. Careful crafting of the regular expressions can help but quite often there really isn&#8217;t much one can do (the book &#8220;Mastering Regular Expressions&#8221; is required reading, see perlfaq2). Running out of space manifests itself by Perl running out of memory.</p>
<dt>&bull;</p>
<dd> Sorting &#8211; the quicksort algorithm used in Perls before 5.8.0 to implement the <code>sort()</code> function was very easy to trick into misbehaving so that it consumes a lot of time. Starting from Perl 5.8.0 a different sorting algorithm, mergesort, is used by default. Mergesort cannot misbehave on any input.</dl>
<p> See &lt;<a rel="nofollow" href="https://www.usenix.org/legacy/events/sec03/tech/full_papers/crosby/crosby.pdf">https://www.usenix.org/legacy/events/sec03/tech/full_papers/crosby/crosby.pdf</a>&gt; for more information, and any computer science textbook on algorithmic complexity.</p>
<h3>Using Sudo</h3>
<p> The popular tool <tt>&quot;sudo&quot;</tt> provides a controlled way for users to be able to run programs as other users. It sanitises the execution environment to some extent, and will avoid the shebang race condition. If you don&#8217;t have the safe version of set-id scripts, then <tt>&quot;sudo&quot;</tt> may be a more convenient way of executing a script as another user than writing a C wrapper would be. </p>
<p> However, <tt>&quot;sudo&quot;</tt> sets the real user or group <font SIZE="-1">ID</font> to that of the target identity, not just the effective <font SIZE="-1">ID</font> as set-id bits do. As a result, Perl can&#8217;t detect that it is running under <tt>&quot;sudo&quot;</tt>, and so won&#8217;t automatically take its own security precautions such as turning on taint mode. Where <tt>&quot;sudo&quot;</tt> configuration dictates exactly which command can be run, the approved command may include a <tt>&quot;-T&quot;</tt> option to perl to enable taint mode. </p>
<p> In general, it is necessary to evaluate the suitaility of a script to run under <tt>&quot;sudo&quot;</tt> specifically with that kind of execution environment in mind. It is neither necessary nor sufficient for the same script to be suitable to run in a traditional set-id arrangement, though many of the issues overlap.</p>
<h2>SEE ALSO</h2>
<p> perlrun for its description of cleaning up environment variables. </p>
<h2>Index</h2>
