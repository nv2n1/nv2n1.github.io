---

title: "asciinema(1)"
name: "asciinema"
section: "1"
letter: "a"
url: "/docs/linux/man/1-asciinema/"
description: "asciinema – terminal session recorder"
---

<h2>NAME</h2>
<p> asciinema &#8211; terminal session recorder</p>
<p> <code>asciinema</code> <i>[-h] [&#8211;version] command [&lt;args&gt;]</i></p>
<p> Terminal session recorder and the best companion of asciinema.org service. </p>
<p> asciinema is composed of multiple commands, similar to git, apt-get or brew. </p>
<p> When you run asciinema with no arguments help messages is displayed, listing all available commands with their options.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-h, &#8211;help</dt>
<dd> Display help message</dd>
<dt>&#8211;version</dt>
<dd> Display version information</dd></dl>
<h2>COMMANDS</h2>
<p> <code>rec [&lt;filename&gt;]</code></p>
<dl>
<dt>
</dt><dd> Record terminal session. </dd>
<p> This is the single most important command in asciinema, since it is how you utilize this tool&#8217;s main job. </p>
<p> By running <code>asciinema rec</code> <i>[filename]</i> you start a new recording session. The command (process) that is recorded can be specified with <i>-c</i> option (see below), and defaults to <code>$SHELL</code> which is what you want in most cases. </p>
<p> Recording finishes when you exit the shell (hit <code>Ctrl+D</code> or type <i>exit</i>). If the recorded process is not a shell than recording finishes when the process exits. </p>
<p> If the <i>filename</i> argument is given then the resulting recording is saved to a local file. It can later be replayed with <code>asciinema play</code> <i>&lt;filename&gt;</i> and/or uploaded to asciinema.org with <code>asciinema upload</code> <i>&lt;filename&gt;</i>. If the <i>filename</i> argument is omitted then (after asking for confirmation) the resulting asciicast is uploaded to asciinema.org for further playback in a web browser. </p>
<p> <code>ASCIINEMA_REC=1</code> is added to recorded process environment variables. This can be used by your shell&#8217;s config file (<i>.bashrc</i>, <i>.zshrc</i>) to alter the prompt or play a sound when shell is being recorded.</p>
<dl>
<dt>Available options:</dt>
<dd>
</dd><dl>
<dl>
<dt>-c, &#8211;command</dt>
<dd> specify command to record, defaults to $SHELL</dd>
<dt>-t</dt>
<dd> specify the title of the asciicast</dd>
<dt>-w, &#8211;max-wait</dt>
<dd> reduce recorded terminal inactivity to max &lt;sec&gt; seconds</dd>
<dt>-y, &#8211;yes</dt>
<dd> answer &quot;yes&quot; to all prompts (e.g. upload confirmation)</dd>
<dt>-q, &#8211;quiet</dt>
<dd> be quiet, suppress all notices/warnings (implies -y)</dd></dl>
</dl>
</dl>
</dl>
<p> <code>play &lt;filename&gt;</code></p>
<dl>
<dt>
</dt><dd> Replay recorded asciicast in a terminal. </dd>
<p> This command replays given asciicast (as recorded by <i>rec</i> command) directly in your terminal. </p>
<p> When &quot;-&quot; is passed as a filename the asciicast is read from stdin. </p>
<p> NOTE: it is recommended to run it in a terminal of dimensions not smaller than the one used for recording as there&#8217;s no &quot;transcoding&quot; of control sequences for new terminal size.</p>
<dl>
<dt>Available options:</dt>
<dd>
</dd><dl>
<dl>
<dt>-w, &#8211;max-wait</dt>
<dd> reduce replayed terminal inactivity to max <i>sec</i> seconds</dd></dl>
</dl>
</dl>
</dl>
<p> <code>upload &lt;filename&gt;</code></p>
<dl>
<dt>
</dt><dd> Upload recorded asciicast to asciinema.org site. </dd>
<p> This command uploads given asciicast (as recorded by <i>rec</i> command) to asciinema.org for further playback in a web browser. </p>
<p> <code>asciinema rec</code> <i>demo.json</i> + <code>asciinema play</code> <i>demo.json</i> + <code>asciinema upload</code> <i>demo.json</i> is a nice combo for when you want to review an asciicast before publishing it on asciinema.org.</dl>
<p> <code>auth</code></p>
<dl>
<dt>
</dt><dd> Assign local API token to asciinema.org account. </dd>
<p> On every machine you install asciinema recorder, you get a new, unique API token. This command connects this local token with your asciinema.org account, and links all asciicasts recorded on this machine with the account. </p>
<p> This command displays the URL you should open in your web browser. If you never logged in to asciinema.org then your account will be created when opening the URL. </p>
<p> NOTE: it is <code>necessary</code> to do this if you want to edit or delete your recordings on asciinema.org. </p>
<p> You can synchronize your config file (which keeps the API token) across the machines but that&#8217;s not necessary. You can assign new tokens to your account from as many machines as you want.</dl>
<h2>CONTRIBUTING</h2>
<p> If you want to contribute to this project check out Contributing page: <i><a rel="nofollow" href="https://asciinema.org/contributing">https://asciinema.org/contributing</a></i></p>
<h2>BUGS</h2>
<p> All your bug reports and feature ideas are highly appreciated as they help to improve the quality and functionality of asciinema for everyone. </p>
<p> As the service is built of several parts there are separate bug trackers:</p>
<dl>
<dt><a rel="nofollow" href="https://github.com/asciinema/asciinema/issues">https://github.com/asciinema/asciinema/issues</a></dt>
<dd> issues and ideas for the command line recorder</dd>
<dt><a rel="nofollow" href="https://github.com/asciinema/asciinema.org/issues">https://github.com/asciinema/asciinema.org/issues</a></dt>
<dd> issues and ideas for the website</dd>
<dt><a rel="nofollow" href="https://github.com/asciinema/asciinema-player/issues">https://github.com/asciinema/asciinema-player/issues</a></dt>
<dd> issues and ideas for the javascript player</dd></dl>
<h2>AUTHORS</h2>
<p> Developed with passion by <code>Marcin Kulik</code> and great open source contributors. </p>
