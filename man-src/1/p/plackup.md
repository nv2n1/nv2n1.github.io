---
title: "plackup(1)"
name: "plackup"
section: "1"
letter: "p"
url: "/docs/linux/man/1-plackup/"
---

<h2 class="name">NAME</h2>
 

 plackup - Run PSGI application with Plack servers 

<h2>SYNOPSIS</h2>

 <pre><code>
#read your app from app.psgi file
plackup
#choose.psgi file from ARGV[0](or with - a option)
        plackup hello.psgi
#switch server implementation with-- server(or -s)
            plackup-- server HTTP::Server::Simple-- port 9090 --host 127.0.0.1 test.psgi
#use UNIX socket to run FCGI daemon
                plackup -
    s FCGI-- listen / tmp / fcgi.sock myapp.psgi
#launch FCGI external server on port 9090
                                plackup -
    s FCGI-- port 9090
</code></pre>

<h2>DESCRIPTION</h2>

 plackup is a command line utility to run <font SIZE="-1">PSGI</font> applications from the command line. 

 plackup automatically figures out the environment it is run in, and runs your application in that environment. FastCGI, <font SIZE="-1">CGI,</font> AnyEvent and others can all be detected. See Plack::Loader for the authoritative list. 

 <tt>&quot;plackup&quot;</tt> assumes you have an <tt>&quot;app.psgi&quot;</tt> script in your current directory. The last statement of <tt>&quot;app.psgi&quot;</tt> should be a code reference that is a <font SIZE="-1">PSGI</font> application: 

 
#!/ usr / bin / perl
use MyApp;
my $application = MyApp-&gt;new;
my $app = sub
{
    $application-&gt;run_psgi(@_)
};


<h2>ARGUMENTS</h2>

<dl>
<dt>.psgi
<dd> <pre>
  plackup --host 127.0.0.1 --port 9090 /path/to/app.psgi
</pre> 

 The first non-option argument is used as a <tt>&quot;.psgi&quot;</tt> file path. You can also set this path with <tt>&quot;-a&quot;</tt> or <tt>&quot;--app&quot;</tt>. If omitted, the default file path is <tt>&quot;app.psgi&quot;</tt> in the current directory.</dl>

<h2>OPTIONS</h2>

<dl>
<dt>-a, --app
<dd> Specifies the full path to a <tt>&quot;.psgi&quot;</tt> script. You may alternately provide this path as the first argument to <tt>&quot;plackup&quot;</tt>.
<dt>-e
<dd> Evaluates the given perl code as a <font SIZE="-1">PSGI</font> app, much like perl's <tt>&quot;-e&quot;</tt> option: 

 
plackup - e 'sub { my $env = shift; return [ ... ] }'
 

 It is also handy when you want to run a custom application like Plack::App::*. 

 <pre>
  plackup -MPlack::App::File -e 'Plack::App::File-&gt;new(...)-&gt;to_app'
</pre> 

 You can also specify <tt>&quot;-e&quot;</tt> option with <tt>&quot;.psgi&quot;</tt> file path to wrap the application with middleware configuration from the command line. You can also use Plack::Builder <font SIZE="-1">DSL</font> syntax inside <tt>&quot;-e&quot;</tt> code. For example: 

 <pre>
  plackup -e 'enable &quot;Auth::Basic&quot;, authenticator =&gt; ...;' myapp.psgi
</pre> 

 is equivalent to the <font SIZE="-1">PSGI</font> application: 

 <pre><code>
use Plack::Builder;
use Plack::Util;

builder
{
    enable "Auth::Basic", authenticator = &gt; ...;
    Plack::Util::load_psgi("myapp.psgi");
};
</code></pre> 

 Note that when you use <tt>&quot;-e&quot;</tt> option to enable middleware, plackup doesn't assume the implicit <tt>&quot;app.psgi&quot;</tt> path. You must either pass the path to your <tt>&quot;.psgi&quot;</tt> file in the command line arguments or load the application inside <tt>&quot;-e&quot;</tt> after the <tt>&quot;enable&quot;</tt>. 

 <pre>
  plackup                                # Runs app.psgi
  plackup -e 'enable &quot;Foo&quot;'              # Doesn't work!
  plackup -e 'enable &quot;Foo&quot;' app.psgi     # Works
  plackup -e 'enable &quot;Foo&quot;; sub { ... }' # Works
</pre>
<dt>-o, --host
<dd> Binds to a <font SIZE="-1">TCP</font> interface. Defaults to undef, which lets most server backends bind to the any (*) interface. This option is only valid for servers which support <font SIZE="-1">TCP</font> sockets.
<dt>-p, --port
<dd> Binds to a <font SIZE="-1">TCP</font> port. Defaults to 5000. This option is only valid for servers which support <font SIZE="-1">TCP</font> sockets.
<dt>-s, --server, the &quot;PLACK_SERVER&quot; environment variable
<dd> Selects a specific server implementation to run on. When provided, the <tt>&quot;-s&quot;</tt> or <tt>&quot;--server&quot;</tt> flag will be preferred over the environment variable. 

 If no option is given, plackup will try to detect the <i>best</i> server implementation based on the environment variables as well as modules loaded by your application in <tt>%INC</tt>. See Plack::Loader for details.
<dt>-S, --socket
<dd> Listens on a <font SIZE="-1">UNIX</font> domain socket path. Defaults to undef. This option is only valid for servers which support <font SIZE="-1">UNIX</font> sockets.
<dt>-l, --listen
<dd> Listens on one or more addresses, whether ``<font SIZE="-1">HOST:PORT'', ``:PORT'',</font> or ``<font SIZE="-1">PATH'' </font>(without colons). You may use this option multiple times to listen on multiple addresses, but the server will decide whether it supports multiple interfaces.
<dt>-D, --daemonize
<dd> Makes the process run in the background. It's up to the backend server/handler implementation whether this option is respected or not.
<dt>-I
<dd> Specifies Perl library include paths, like <tt>&quot;perl&quot;</tt>'s -I option. You may add multiple paths by using this option multiple times.
<dt>-M
<dd> Loads the named modules before loading the app's code. You may load multiple modules by using this option multiple times.
<dt>-E, --env, the &quot;PLACK_ENV&quot; environment variable.
<dd> Specifies the environment option. Setting this value with <tt>&quot;-E&quot;</tt> or <tt>&quot;--env&quot;</tt> also writes to the <tt>&quot;PLACK_ENV&quot;</tt> environment variable. This allows applications or frameworks to tell which environment setting the application is running on. 

 <pre>
  # These two are the same
  plackup -E deployment
  env PLACK_ENV=deployment plackup
</pre> 

 Common values are <tt>&quot;development&quot;</tt>, <tt>&quot;deployment&quot;</tt>, and <tt>&quot;test&quot;</tt>. The default value is <tt>&quot;development&quot;</tt>, which causes <tt>&quot;plackup&quot;</tt> to load the middleware components: <i>AccessLog</i>, <i>StackTrace</i>, and <i>Lint</i> unless <tt>&quot;--no-default-middleware&quot;</tt> is set.
<dt>--no-default-middleware
<dd> This prevents loading the default middleware stack even when Plack environment (i.e. <tt>&quot;-E&quot;</tt> or <tt>&quot;PLACK_ENV&quot;</tt>) is set to <tt>&quot;development&quot;</tt>.
<dt>-r, --reload
<dd> Makes plackup restart the server whenever a file in your development directory changes. This option by default watches the <tt>&quot;lib&quot;</tt> directory and the base directory where <i>.psgi</i> file is located. Use <tt>&quot;-R&quot;</tt> to watch other directories. 

 Reloading will delay the compilation of your application. Automatic server detection (see <tt>&quot;-s&quot;</tt> above) may not behave as you expect, if plackup needs to scan your application for the modules it uses. Avoid problems by specifying <tt>&quot;-s&quot;</tt> explicitly when using <tt>&quot;-r&quot;</tt> or <tt>&quot;-R&quot;</tt>.
<dt>-R, --Reload
<dd> Makes plackup restart the server whenever a file in any of the given directories changes. <tt>&quot;-R&quot;</tt> and <tt>&quot;--Reload&quot;</tt> take a comma-separated list of paths: 

 <pre>
  plackup -R /path/to/project/lib,/path/to/project/templates
</pre>
<dt>-L, --loader
<dd> Specifies the server loading subclass that implements how to run the server. Available options are <i>Plack::Loader</i> (default), <i>Restarter</i> (automatically set when <tt>&quot;-r&quot;</tt> or <tt>&quot;-R&quot;</tt> is used), <i>Delayed</i>, and <i>Shotgun</i>. 

 See Plack::Loader::Delayed and Plack::Loader::Shotgun for more details.
<dt>--access-log
<dd> Specifies the pathname of a file where the access log should be written. By default, in the development environment access logs will go to <font SIZE="-1">STDERR.</font>
<dt>--path
<dd> Specify the root path of your app (<tt>&quot;SCRIPT_NAME&quot;</tt> in <font SIZE="-1">PSGI</font> env) to run. The following two commands are roughly the same. 

 <pre>
  plackup --path /foo app.psgi
  plackup -e 'mount &quot;/foo&quot; =&gt; Plack::Util::load_psgi(&quot;app.psgi&quot;)'
</pre></dl>
 

 Other options that starts with <tt>&quot;--&quot;</tt> are passed through to the backend server. See each Plack::Handler backend's documentation for more details on their available options.

<h2>SEE ALSO</h2>

 Plack::Runner Plack::Loader 

<h2>Index</h2>


