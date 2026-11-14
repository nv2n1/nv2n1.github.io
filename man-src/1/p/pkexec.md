---
title: "pkexec(1)"
name: "pkexec"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pkexec/"
description: "pkexec – Execute a command as another user"
---

<h2 class="name">NAME</h2>
<p> pkexec &#8211; Execute a command as another user </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pkexec</code> [<code>&#8211;version</code>] [<code>&#8211;disable-internal-agent</code>] [<code>&#8211;help</code>]</p>
<dt> <code>pkexec</code> [<code>&#8211;user</code>&nbsp;<i>username</i>] <i>PROGRAM</i> [<i>ARGUMENTS</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>pkexec</code></p>
<dd>allows an authorized user to execute <i>PROGRAM</i> as another user. If <i>username</i> is not specified, then the program will be executed as the administrative super user, <i>root</i>.</p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, the return value is the return value of <i>PROGRAM</i>. If the calling process is not authorized or an authorization could not be obtained through authentication or an error occured, <code>pkexec</code> exits with a return value of 127. If the authorization could not be obtained because the user dismissed the authentication dialog, <code>pkexec</code> exits with a return value of 126.</p>
<h2>AUTHENTICATION AGENT</h2>
<p> <code>pkexec</code>, like any other PolicyKit application, will use the authentication agent registered for the calling process. However, if no authentication agent is available, then <code>pkexec</code> will register its own textual authentication agent. This behavior can be turned off by passing the <code>&#8211;disable-internal-agent</code> option.</p>
<h2>SECURITY NOTES</h2>
<p> Executing a program as another user is a privileged operation. By default the required authorization (See the section called &#8220;REQUIRED AUTHORIZATIONS&#8221;) requires administrator authentication. In addition, the authentication dialog presented to the user will display the full path to the program to be executed so the user is aware of what will happen: </p>
<dl>
<dt>
<dd> [IMAGE]<font SIZE="-2">[1]</font> </p>
<dl>
<dt>
<dd>
<pre><code>
+----------------------------------------------------------+
|                     Authenticate                     [X] |
+----------------------------------------------------------+
|                                                          |
|  [Icon]  Authentication is needed to run `/bin/bash'     |
|          as the super user                               |
|                                                          |
|          An application is attempting to perform an      |
|          action that requires privileges. Authentication |
|          as the super user is required to perform this   |
|          action.                                         |
|                                                          |
|          Password for root: [_________________________]  |
|                                                          |
| [V] Details:                                             |
|  Command: /bin/bash                                      |
|  Run As:  Super User (root)                              |
|  Action:  org.freedesktop.policykit.exec                 |
|  Vendor:  The PolicyKit Project                          |
|                                                          |
|                                  [Cancel] [Authenticate] |
+----------------------------------------------------------+
</code></pre>
</dl>
</dl>
<p> The environment that <i>PROGRAM</i> will run it, will be set to a minimal known and safe environment in order to avoid injecting code through LD_LIBRARY_PATH or similar mechanisms. In addition the PKEXEC_UID environment variable is set to the user id of the process invoking <code>pkexec</code>. As a result, <code>pkexec</code> will not allow you to run X11 applications as another user since the $DISPLAY and $XAUTHORITY environment variables are not set. These two variables will be retained if the <i>org.freedesktop.policykit.exec.allow_gui</i> annotation on an action is set to a nonempty value; this is discouraged, though, and should only be used for legacy programs.</p>
<h2>REQUIRED AUTHORIZATIONS</h2>
<p> By default, the <i>org.freedesktop.policykit.exec</i> authorization is required unless an action definition file is present for the program in question. To require another authorization, it can be specified using the <i>org.freedesktop.policykit.exec.path</i> annotation on an action (See the section called &#8220;EXAMPLE&#8221; for details).</p>
<h2>EXAMPLE</h2>
<p> To specify what kind of authorization is needed to execute the program /usr/bin/pk-example-frobnicate as another user, simply write an action definition file like this </p>
<dl>
<dt>
<dd>
<pre>
&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;!DOCTYPE policyconfig PUBLIC
 &quot;-//freedesktop//DTD PolicyKit Policy Configuration 1.0//EN&quot;
 &quot;<a rel="nofollow" href="http://www.freedesktop.org/standards/PolicyKit/1/policyconfig.dtd">http://www.freedesktop.org/standards/PolicyKit/1/policyconfig.dtd</a>&quot;&gt;
&lt;policyconfig&gt;
  &lt;vendor&gt;Examples for the PolicyKit Project&lt;/vendor&gt;
  &lt;vendor_url&gt;<a rel="nofollow" href="http://hal.freedesktop.org/docs/PolicyKit/">http://hal.freedesktop.org/docs/PolicyKit/</a>&lt;/vendor_url&gt;
  &lt;action id=&quot;org.freedesktop.policykit.example.pkexec.run-frobnicate&quot;&gt;
    &lt;description&gt;Run the PolicyKit example program Frobnicate&lt;/description&gt;
    &lt;description xml:lang=&quot;da&quot;&gt;Kør PolicyKit eksemplet Frobnicate&lt;/description&gt;
    &lt;message&gt;Authentication is required to run the PolicyKit example program Frobnicate (user=$(user), program=$(program), command_line=$(command_line))&lt;/message&gt;
    &lt;message xml:lang=&quot;da&quot;&gt;Autorisering er påkrævet for at afvikle PolicyKit eksemplet Frobnicate (user=$(user), program=$(program), command_line=$(command_line))&lt;/message&gt;
    &lt;icon_name&gt;audio-x-generic&lt;/icon_name&gt; 
    &lt;defaults&gt;
      &lt;allow_any&gt;no&lt;/allow_any&gt;
      &lt;allow_inactive&gt;no&lt;/allow_inactive&gt;
      &lt;allow_active&gt;auth_self_keep&lt;/allow_active&gt;
    &lt;/defaults&gt;
    &lt;annotate key=&quot;org.freedesktop.policykit.exec.path&quot;&gt;/usr/bin/pk-example-frobnicate&lt;/annotate&gt;
  &lt;/action&gt;
&lt;/policyconfig&gt;
</pre>
</dl>
<p> and drop it in the /usr/share/polkit-1/actions directory under a suitable name (e.g. matching the namespace of the action). Note that in addition to specifying the program, the authentication message, description, icon and defaults can be specified. Note that occurences of the strings $(user), $(program) and $(command_line) in the message will be replaced with respectively the user (of the form &quot;Real Name (username)&quot; or just &quot;username&quot; if there is no real name for the username), the binary to execute (a fully-qualified path, e.g. &quot;/usr/bin/pk-example-frobnicate&quot;) and the command-line, e.g. &quot;pk-example-frobnicate foo bar&quot;. For example, for the action defined above, the following authentication dialog will be shown: </p>
<dl>
<dt>
<dd> [IMAGE]<font SIZE="-2">[2]</font> </p>
<dl>
<dt>
<dd>
+&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-+<br />
|                     Authenticate                     [X] |<br />
+&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-+<br />
|                                                          |<br />
|  [Icon]  Authentication is required to run the PolicyKit |<br />
|          example program Frobnicate                      |<br />
|                                                          |<br />
|          An application is attempting to perform an      |<br />
|          action that requires privileges. Authentication |<br />
|          is required to perform this action.             |<br />
|                                                          |<br />
|          Password: [__________________________________]  |<br />
|                                                          |<br />
| [V] Details:                                             |<br />
|  Command: /usr/bin/pk-example-frobnicate                 |<br />
|  Run As:  Super User (root)                              |<br />
|  Action:  org.fd.pk.example.pkexec.run-frobnicate        |<br />
|  Vendor:  Examples for the PolicyKit Project             |<br />
|                                                          |<br />
|                                  [Cancel] [Authenticate] |<br />
+&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-+
</dl>
</dl>
<p> If the user is using the da_DK locale, the dialog looks like this: </p>
<dl>
<dt>
<dd> [IMAGE]<font SIZE="-2">[3]</font> </p>
<dl>
<dt>
<dd>
<pre><code>
+----------------------------------------------------------+
|                     Autorisering                     [X] |
+----------------------------------------------------------+
|                                                          |
|  [Icon]  Autorisering er påkrævet for at afvikle         |
|          PolicyKit eksemplet Frobnicate                  |
|                                                          |
|          Et program forsøger at udføre en handling der   |
|          kræver privilegier. Autorisering er påkrævet.   |
|                                                          |
|          Kodeord: [___________________________________]  |
|                                                          |
| [V] Detaljer:                                            |
|  Bruger:   Super User (root)                             |
|  Program:  /usr/bin/pk-example-frobnicate                |
|  Handling: org.fd.pk.example.pkexec.run-frobnicate       |
|  Vendor:   Examples for the PolicyKit Project            |
|                                                          |
|                                [Annullér] [Autorisering] |
+----------------------------------------------------------+
</code></pre>
</dl>
</dl>
<p> Note that <code>pkexec</code> does no validation of the <i>ARGUMENTS</i> passed to <i>PROGRAM</i>. In the normal case (where administrator authentication is required every time <code>pkexec</code> is used), this is not a problem since if the user is an administrator he might as well just run <code>pkexec bash</code> to get root. </p>
<p> However, if an action is used for which the user can retain authorization (or if the user is implicitly authorized), such as with pk-example-frobnicate above, this could be a security hole. Therefore, as a rule of thumb, programs for which the default required authorization is changed, should never implicitly trust user input (e.g. like any other well-written <i>suid</i> program).</p>
<h2>AUTHOR</h2>
<p> Written by David Zeuthen &lt;davidz [at] redhat.com&gt; with a lot of help from many others.</p>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution or the polkit-devel mailing list, see the link m[blue]<code><a rel="nofollow" href="http://lists.freedesktop.org/mailman/listinfo/polkit-devel">http://lists.freedesktop.org/mailman/listinfo/polkit-devel</a></code>m[] on how to subscribe.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8), <code><a href="/docs/linux/man/1-pkaction/">pkaction</a></code>(1), <code><a href="/docs/linux/man/1-pkcheck/">pkcheck</a></code>(1), <code><a href="/docs/linux/man/1-pkttyagent/">pkttyagent</a></code>(1)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> /usr/share/gtk-doc/html/polkit-1/pkexec-bash.png</p>
<dt> 2.</p>
<dd> /usr/share/gtk-doc/html/polkit-1/pkexec-frobnicate.png</p>
<dt> 3.</p>
<dd> /usr/share/gtk-doc/html/polkit-1/pkexec-frobnicate-da.png </p>
</dl>
<h2>Index</h2>
