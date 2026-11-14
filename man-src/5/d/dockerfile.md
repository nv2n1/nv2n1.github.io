---
title: "dockerfile(5)"
name: "dockerfile"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dockerfile/"
description: "Dockerfile – automate the steps of creating a Docker image"
---

<p>Dockerfile &#8211; automate the steps of creating a Docker image </p>
<h2>Introduction</h2>
<p>The <code>Dockerfile</code> is a configuration file that automates the steps of creating a Docker image. It is similar to a Makefile. Docker reads instructions from the <code>Dockerfile</code> to automate the steps otherwise performed manually to create an image. To build an image, create a file called <code>Dockerfile</code>. </p>
<p> The <code>Dockerfile</code> describes the steps taken to assemble the image. When the <code>Dockerfile</code> has been created, call the docker build command, using the path of directory that contains <code>Dockerfile</code> as the argument.</p>
<h2>Synopsis</h2>
<p>INSTRUCTION arguments For example: FROM image </p>
<h2>Description</h2>
<p>A Dockerfile is a file that automates the steps of creating a Docker image. A Dockerfile is similar to a Makefile. </p>
<h2>Usage</h2>
<p>docker build . </p>
<p> &#8212; Runs the steps and commits them, building a final image.<br />
&nbsp;<wbr>&nbsp;The path to the source repository defines where to find the context of the<br />
&nbsp;<wbr>&nbsp;build. The build is run by the Docker daemon, not the CLI. The whole<br />
&nbsp;<wbr>&nbsp;context must be transferred to the daemon. The Docker CLI reports<br />
&nbsp;<wbr>&nbsp;&quot;Sending build context to Docker daemon&quot;&nbsp;when the context is sent to the<br />
&nbsp;<wbr>&nbsp;daemon. </p>
<dl>
<dd>
<pre> docker build -t repository/tag .</pre>
</dl>
<p> &#8212; specifies a repository and tag at which to save the new image if the build<br />
&nbsp;<wbr>&nbsp;succeeds. The Docker daemon runs the steps one-by-one, committing the result<br />
&nbsp;<wbr>&nbsp;to a new image if necessary, before finally outputting the ID of the new<br />
&nbsp;<wbr>&nbsp;image. The Docker daemon automatically cleans up the context it is given. </p>
<p> Docker re-uses intermediate images whenever possible. This significantly<br />
&nbsp;<wbr>&nbsp;accelerates the&nbsp;<i>docker build</i>&nbsp;process.</p>
<h2>Format</h2>
<p>FROM image </p>
<p> FROM image:tag </p>
<p> FROM image [at] digest </p>
<p> &#8212; The <code>FROM</code> instruction sets the base image for subsequent instructions. A<br />
&nbsp;<wbr>&nbsp;valid Dockerfile must have&nbsp;<code>FROM</code>&nbsp;as its first instruction. The image can be any<br />
&nbsp;<wbr>&nbsp;valid image. It is easy to start by pulling an image from the public<br />
&nbsp;<wbr>&nbsp;repositories. </p>
<p> &#8212; <code>FROM</code> must be the first non-comment instruction in Dockerfile. </p>
<p> &#8212; <code>FROM</code> may appear multiple times within a single Dockerfile in order to create<br />
&nbsp;<wbr>&nbsp;multiple images. Make a note of the last image ID output by the commit before<br />
&nbsp;<wbr>&nbsp;each new&nbsp;<code>FROM</code>&nbsp;command. </p>
<p> &#8212; If no tag is given to the <code>FROM</code> instruction, Docker applies the<br />
&nbsp;<wbr>&nbsp;latest tag. If the used tag does not exist, an error is returned. </p>
<p> &#8212; If no digest is given to the <code>FROM</code> instruction, Docker applies the<br />
&nbsp;<wbr>&nbsp;latest tag. If the used tag does not exist, an error is returned. </p>
<p> <code>MAINTAINER</code><br />
&nbsp;<wbr>&nbsp;&#8212;&nbsp;<code>MAINTAINER</code>&nbsp;sets the Author field for the generated images.<br />
&nbsp;<wbr>&nbsp;Useful for providing users with an email or url for support. </p>
<p> <code>RUN</code><br />
&nbsp;<wbr>&nbsp;&#8212;&nbsp;<code>RUN</code>&nbsp;has two forms: </p>
<dl>
<dd>
<pre> # the command is run in a shell - /bin/sh -c
 RUN &lt;command&gt;
 # Executable form
 RUN [&quot;executable&quot;, &quot;param1&quot;, &quot;param2&quot;]</pre>
</dl>
<p> &#8212; The <code>RUN</code> instruction executes any commands in a new layer on top of the current<br />
&nbsp;<wbr>&nbsp;image and commits the results. The committed image is used for the next step in<br />
&nbsp;<wbr>&nbsp;Dockerfile. </p>
<p> &#8212; Layering <code>RUN</code> instructions and generating commits conforms to the core<br />
&nbsp;<wbr>&nbsp;concepts of Docker where commits are cheap and containers can be created from<br />
&nbsp;<wbr>&nbsp;any point in the history of an image. This is similar to source control.&nbsp;<wbr>&nbsp;The<br />
&nbsp;<wbr>&nbsp;exec form makes it possible to avoid shell string munging. The exec form makes<br />
&nbsp;<wbr>&nbsp;it possible to&nbsp;<code>RUN</code>&nbsp;commands using a base image that does not contain&nbsp;/bin/sh. </p>
<p> Note that the exec form is parsed as a JSON array, which means that you must<br />
&nbsp;<wbr>&nbsp;use double-quotes&nbsp;(&quot;)&nbsp;around words not single-quotes&nbsp;(&#8216;). </p>
<p> <code>CMD</code><br />
&nbsp;<wbr>&nbsp;&#8212;&nbsp;<code>CMD</code>&nbsp;has three forms: </p>
<dl>
<dd>
<pre> # Executable form
 CMD [&quot;executable&quot;, &quot;param1&quot;, &quot;param2&quot;]`
 # Provide default arguments to ENTRYPOINT
 CMD [&quot;param1&quot;, &quot;param2&quot;]`
 # the command is run in a shell - /bin/sh -c
 CMD command param1 param2</pre>
</dl>
<p> &#8212; There should be only one <code>CMD</code> in a Dockerfile. If more than one <code>CMD</code> is listed, only<br />
&nbsp;<wbr>&nbsp;the last&nbsp;<code>CMD</code>&nbsp;takes effect.<br />
&nbsp;<wbr>&nbsp;The main purpose of a&nbsp;<code>CMD</code>&nbsp;is to provide defaults for an executing container.<br />
&nbsp;<wbr>&nbsp;These defaults may include an executable, or they can omit the executable. If<br />
&nbsp;<wbr>&nbsp;they omit the executable, an&nbsp;<code>ENTRYPOINT</code>&nbsp;must be specified.<br />
&nbsp;<wbr>&nbsp;When used in the shell or exec formats, the&nbsp;<code>CMD</code>&nbsp;instruction sets the command to<br />
&nbsp;<wbr>&nbsp;be executed when running the image.<br />
&nbsp;<wbr>&nbsp;If you use the shell form of the&nbsp;<code>CMD</code>, the&nbsp;&lt;command&gt;&nbsp;executes in&nbsp;/bin/sh -c: </p>
<p> Note that the exec form is parsed as a JSON array, which means that you must<br />
&nbsp;<wbr>&nbsp;use double-quotes&nbsp;(&quot;)&nbsp;around words not single-quotes&nbsp;(&#8216;). </p>
<dl>
<dd>
<pre> FROM ubuntu
 CMD echo &quot;This is a test.&quot; | wc -</pre>
</dl>
<p> &#8212; If you run <code>command</code> without a shell, then you must express the command as a<br />
&nbsp;<wbr>&nbsp;JSON array and give the full path to the executable. This array form is the<br />
&nbsp;<wbr>&nbsp;preferred form of&nbsp;<code>CMD</code>. All additional parameters must be individually expressed<br />
&nbsp;<wbr>&nbsp;as strings in the array: </p>
<dl>
<dd>
<pre> FROM ubuntu
 CMD [&quot;/usr/bin/wc&quot;,&quot;--help&quot;]</pre>
</dl>
<p> &#8212; To make the container run the same executable every time, use <code>ENTRYPOINT</code> in<br />
&nbsp;<wbr>&nbsp;combination with&nbsp;<code>CMD</code>.<br />
&nbsp;<wbr>&nbsp;If the user specifies arguments to docker run, the specified commands<br />
&nbsp;<wbr>&nbsp;override the default in&nbsp;<code>CMD</code>.<br />
&nbsp;<wbr>&nbsp;Do not confuse&nbsp;<code>RUN</code>&nbsp;with&nbsp;<code>CMD</code>.&nbsp;<code>RUN</code>&nbsp;runs a command and commits the result.<br />
&nbsp;<wbr>&nbsp;<code>CMD</code>&nbsp;executes nothing at build time, but specifies the intended command for<br />
&nbsp;<wbr>&nbsp;the image. </p>
<p> <code>LABEL</code><br />
&nbsp;<wbr>&nbsp;&#8212; LABEL&nbsp;&lt;key&gt;=&lt;value&gt;&nbsp;[&lt;key&gt;=&lt;value&gt;&nbsp;&#8230;]or </p>
<dl>
<dd>
<pre> LABEL &lt;key&gt;[ &lt;value&gt;]
 LABEL &lt;key&gt;[ &lt;value&gt;]
 ...</pre>
</dl>
<p> The <code>LABEL</code> instruction adds metadata to an image. A <code>LABEL</code> is a<br />
&nbsp;<wbr>&nbsp;key-value pair. To specify a&nbsp;<code>LABEL</code>&nbsp;without a value, simply use an empty<br />
&nbsp;<wbr>&nbsp;string. To include spaces within a&nbsp;<code>LABEL</code>&nbsp;value, use quotes and<br />
&nbsp;<wbr>&nbsp;backslashes as you would in command-line parsing. </p>
<dl>
<dd>
<pre> LABEL com.example.vendor=&quot;ACME Incorporated&quot;
 LABEL com.example.vendor &quot;ACME Incorporated&quot;
 LABEL com.example.vendor.is-beta &quot;&quot;
 LABEL com.example.vendor.is-beta=
 LABEL com.example.vendor.is-beta=&quot;&quot;</pre>
</dl>
<p> An image can have more than one label. To specify multiple labels, separate<br />
&nbsp;<wbr>&nbsp;each key-value pair by a space. </p>
<p> Labels are additive including LABELs in FROM images. As the system<br />
&nbsp;<wbr>&nbsp;encounters and then applies a new label, new keys override any previous<br />
&nbsp;<wbr>&nbsp;labels with identical keys. </p>
<p> To display an image&#8217;s labels, use the docker inspect command. </p>
<p> <code>STOPSIGNAL</code> </p>
<p> &#8212; STOPSIGNAL &lt;signal&gt;<br />
&nbsp;<wbr>&nbsp;The&nbsp;<code>STOPSIGNAL</code>&nbsp;instruction sets the system call signal that will be sent<br />
&nbsp;<wbr>&nbsp;to the container to exit. This signal can be a signal name in the format<br />
&nbsp;<wbr>&nbsp;<code>SIG</code>, for instance&nbsp;<code>SIGKILL</code>, or an unsigned number that matches a<br />
&nbsp;<wbr>&nbsp;position in the kernel&#8217;s syscall table, for instance&nbsp;<code>9</code>. The default is<br />
&nbsp;<wbr>&nbsp;<code>SIGTERM</code>&nbsp;if not defined. </p>
<p> The image&#8217;s default stopsignal can be overridden per container, using the<br />
&nbsp;<wbr>&nbsp;<code>&#8211;stop-signal</code>&nbsp;flag on&nbsp;<code><a href="/docs/linux/man/1-docker-run/">docker-run</a>(1)</code>&nbsp;and&nbsp;<code><a href="/docs/linux/man/1-docker-create/">docker-create</a>(1)</code>. </p>
<p> <code>EXPOSE</code><br />
&nbsp;<wbr>&nbsp;&#8212; EXPOSE&nbsp;&lt;port&gt;&nbsp;[&lt;port&gt;&#8230;]<br />
&nbsp;<wbr>&nbsp;The&nbsp;<code>EXPOSE</code>&nbsp;instruction informs Docker that the container listens on the<br />
&nbsp;<wbr>&nbsp;specified network ports at runtime. Docker uses this information to<br />
&nbsp;<wbr>&nbsp;interconnect containers using links and to set up port redirection on the host<br />
&nbsp;<wbr>&nbsp;system. </p>
<p> <code>ENV</code><br />
&nbsp;<wbr>&nbsp;&#8212; ENV&nbsp;&lt;key&gt;&nbsp;&lt;value&gt;<br />
&nbsp;<wbr>&nbsp;The&nbsp;<code>ENV</code>&nbsp;instruction sets the environment variable&nbsp;<wbr>&nbsp;to<br />
&nbsp;<wbr>&nbsp;the value&nbsp;&lt;value&gt;. This value is passed to all future<br />
&nbsp;<wbr>&nbsp;<code>RUN</code>,&nbsp;<code>ENTRYPOINT</code>, and&nbsp;<code>CMD</code>&nbsp;instructions. This is<br />
&nbsp;<wbr>&nbsp;functionally equivalent to prefixing the command with&nbsp;&lt;key&gt;=&lt;value&gt;.&nbsp;<wbr>&nbsp;The<br />
&nbsp;<wbr>&nbsp;environment variables that are set with&nbsp;<code>ENV</code>&nbsp;persist when a container is run<br />
&nbsp;<wbr>&nbsp;from the resulting image. Use docker inspect to inspect these values, and<br />
&nbsp;<wbr>&nbsp;change them using docker run &#8211;env&nbsp;&lt;key&gt;=&lt;value&gt;. </p>
<p> Note that setting &quot;ENV DEBIAN_FRONTEND=noninteractive&quot; may cause<br />
&nbsp;<wbr>&nbsp;unintended consequences, because it will persist when the container is run<br />
&nbsp;<wbr>&nbsp;interactively, as with the following command: docker run -t -i image bash </p>
<p> <code>ADD</code><br />
&nbsp;<wbr>&nbsp;&#8212;&nbsp;<code>ADD</code>&nbsp;has two forms: </p>
<dl>
<dd>
<pre> ADD &lt;src&gt; &lt;dest&gt;
 # Required for paths with whitespace
 ADD [&quot;&lt;src&gt;&quot;,... &quot;&lt;dest&gt;&quot;]</pre>
</dl>
<p> The <code>ADD</code> instruction copies new files, directories<br />
&nbsp;<wbr>&nbsp;or remote file URLs to the filesystem of the container at path&nbsp;&lt;dest&gt;.<br />
&nbsp;<wbr>&nbsp;Multiple&nbsp;&lt;src&gt;&nbsp;resources may be specified but if they are files or directories<br />
&nbsp;<wbr>&nbsp;then they must be relative to the source directory that is being built<br />
&nbsp;<wbr>&nbsp;(the context of the build). The&nbsp;&lt;dest&gt;&nbsp;is the absolute path, or path relative<br />
&nbsp;<wbr>&nbsp;to&nbsp;<code>WORKDIR</code>, into which the source is copied inside the target container.<br />
&nbsp;<wbr>&nbsp;If the&nbsp;&lt;src&gt;&nbsp;argument is a local file in a recognized compression format<br />
&nbsp;<wbr>&nbsp;(tar, gzip, bzip2, etc)&nbsp;then it is unpacked at the specified&nbsp;&lt;dest&gt;&nbsp;in the<br />
&nbsp;<wbr>&nbsp;container&#8217;s filesystem.&nbsp;<wbr>&nbsp;Note that only local compressed files will be unpacked,<br />
&nbsp;<wbr>&nbsp;i.e., the URL download and archive unpacking features cannot be used together.<br />
&nbsp;<wbr>&nbsp;All new directories are created with mode 0755 and with the uid and gid of&nbsp;<code>0</code>. </p>
<p> <code>COPY</code><br />
&nbsp;<wbr>&nbsp;&#8212;&nbsp;<code>COPY</code>&nbsp;has two forms: </p>
<dl>
<dd>
<pre> COPY &lt;src&gt; &lt;dest&gt;
 # Required for paths with whitespace
 COPY [&quot;&lt;src&gt;&quot;,... &quot;&lt;dest&gt;&quot;]</pre>
</dl>
<p> The <code>COPY</code> instruction copies new files from &lt;src&gt; and<br />
&nbsp;<wbr>&nbsp;adds them to the filesystem of the container at path . The&nbsp;&lt;src&gt;&nbsp;must be<br />
&nbsp;<wbr>&nbsp;the path to a file or directory relative to the source directory that is<br />
&nbsp;<wbr>&nbsp;being built&nbsp;(the context of the build)&nbsp;or a remote file URL. The&nbsp;&lt;dest&gt;&nbsp;is an<br />
&nbsp;<wbr>&nbsp;absolute path, or a path relative to&nbsp;<code>WORKDIR</code>, into which the source will<br />
&nbsp;<wbr>&nbsp;be copied inside the target container. If you&nbsp;<code>COPY</code>&nbsp;an archive file it will<br />
&nbsp;<wbr>&nbsp;land in the container exactly as it appears in the build context without any<br />
&nbsp;<wbr>&nbsp;attempt to unpack it.&nbsp;<wbr>&nbsp;All new files and directories are created with mode&nbsp;<code>0755</code><br />
&nbsp;<wbr>&nbsp;and with the uid and gid of&nbsp;<code>0</code>. </p>
<p> <code>ENTRYPOINT</code><br />
&nbsp;<wbr>&nbsp;&#8212;&nbsp;<code>ENTRYPOINT</code>&nbsp;has two forms: </p>
<dl>
<dd>
<pre> # executable form
 ENTRYPOINT [&quot;executable&quot;, &quot;param1&quot;, &quot;param2&quot;]`
 # run command in a shell - /bin/sh -c
 ENTRYPOINT command param1 param2</pre>
</dl>
<p> &#8212; An <code>ENTRYPOINT</code> helps you configure a<br />
&nbsp;<wbr>&nbsp;container that can be run as an executable. When you specify an&nbsp;<code>ENTRYPOINT</code>,<br />
&nbsp;<wbr>&nbsp;the whole container runs as if it was only that executable.&nbsp;<wbr>&nbsp;The&nbsp;<code>ENTRYPOINT</code><br />
&nbsp;<wbr>&nbsp;instruction adds an entry command that is not overwritten when arguments are<br />
&nbsp;<wbr>&nbsp;passed to docker run. This is different from the behavior of&nbsp;<code>CMD</code>. This allows<br />
&nbsp;<wbr>&nbsp;arguments to be passed to the entrypoint, for instance docker run&nbsp;&lt;image&gt;&nbsp;-d<br />
&nbsp;<wbr>&nbsp;passes the -d argument to the&nbsp;<code>ENTRYPOINT</code>.&nbsp;<wbr>&nbsp;Specify parameters either in the<br />
&nbsp;<wbr>&nbsp;<code>ENTRYPOINT</code>&nbsp;JSON array&nbsp;(as in the preferred exec form above), or by using a&nbsp;<code>CMD</code><br />
&nbsp;<wbr>&nbsp;statement.&nbsp;<wbr>&nbsp;Parameters in the&nbsp;<code>ENTRYPOINT</code>&nbsp;are not overwritten by the docker run<br />
&nbsp;<wbr>&nbsp;arguments.&nbsp;<wbr>&nbsp;Parameters specified via&nbsp;<code>CMD</code>&nbsp;are overwritten by docker run<br />
&nbsp;<wbr>&nbsp;arguments.&nbsp;<wbr>&nbsp;Specify a plain string for the&nbsp;<code>ENTRYPOINT</code>, and it will execute in<br />
&nbsp;<wbr>&nbsp;/bin/sh -c, like a&nbsp;<code>CMD</code>&nbsp;instruction: </p>
<dl>
<dd>
<pre> FROM ubuntu
 ENTRYPOINT wc -l -</pre>
</dl>
<p> This means that the Dockerfile&#8217;s image always takes stdin as input (that&#8217;s<br />
&nbsp;<wbr>&nbsp;what&nbsp;&quot;-&quot;&nbsp;means), and prints the number of lines&nbsp;(that&#8217;s what&nbsp;&quot;-l&quot;&nbsp;means). To<br />
&nbsp;<wbr>&nbsp;make this optional but default, use a&nbsp;<code>CMD</code>: </p>
<dl>
<dd>
<pre> FROM ubuntu
 CMD [&quot;-l&quot;, &quot;-&quot;]
 ENTRYPOINT [&quot;/usr/bin/wc&quot;]</pre>
</dl>
<p> <code>VOLUME</code><br />
&nbsp;<wbr>&nbsp;&#8212; VOLUME&nbsp;[&quot;/data&quot;]<br />
&nbsp;<wbr>&nbsp;The&nbsp;<code>VOLUME</code>&nbsp;instruction creates a mount point with the specified name and marks<br />
&nbsp;<wbr>&nbsp;it as holding externally-mounted volumes from the native host or from other<br />
&nbsp;<wbr>&nbsp;containers. </p>
<p> <code>USER</code><br />
&nbsp;<wbr>&nbsp;&#8212; USER daemon<br />
&nbsp;<wbr>&nbsp;Sets the username or UID used for running subsequent commands. </p>
<p> The <code>USER</code> instruction can optionally be used to set the group or GID. The<br />
&nbsp;<wbr>&nbsp;followings examples are all valid:<br />
&nbsp;<wbr>&nbsp;USER&nbsp;[user | user:group | uid | uid:gid | user:gid | uid:group&nbsp;] </p>
<p> Until the <code>USER</code> instruction is set, instructions will be run as root. The USER<br />
&nbsp;<wbr>&nbsp;instruction can be used any number of times in a Dockerfile, and will only affect<br />
&nbsp;<wbr>&nbsp;subsequent commands. </p>
<p> <code>WORKDIR</code><br />
&nbsp;<wbr>&nbsp;&#8212; WORKDIR&nbsp;/path/to/workdir<br />
&nbsp;<wbr>&nbsp;The&nbsp;<code>WORKDIR</code>&nbsp;instruction sets the working directory for the&nbsp;<code>RUN</code>,&nbsp;<code>CMD</code>,<br />
&nbsp;<wbr>&nbsp;<code>ENTRYPOINT</code>,&nbsp;<code>COPY</code>&nbsp;and&nbsp;<code>ADD</code>&nbsp;Dockerfile commands that follow it. It can<br />
&nbsp;<wbr>&nbsp;be used multiple times in a single Dockerfile. Relative paths are defined<br />
&nbsp;<wbr>&nbsp;relative to the path of the previous&nbsp;<code>WORKDIR</code>&nbsp;instruction. For example: </p>
<dl>
<dd>
<pre> WORKDIR /a
 WORKDIR b
 WORKDIR c
 RUN pwd</pre>
</dl>
<p> In the above example, the output of the <code>pwd</code> command is <code>a/b/c</code>. </p>
<p> <code>ARG</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8212; ARG&nbsp;[=] </p>
<p> The ARG instruction defines a variable that users can pass at build-time to<br />
&nbsp;<wbr>&nbsp;the builder with the docker build command using the &#8211;build-arg<br />
&nbsp;<wbr>&nbsp;&lt;varname&gt;=&lt;value&gt;&nbsp;flag. If a user specifies a build argument that was not<br />
&nbsp;<wbr>&nbsp;defined in the Dockerfile, the build outputs a warning. </p>
<dl>
<dd>
<pre> [Warning] One or more build-args [foo] were not consumed</pre>
</dl>
<p> The Dockerfile author can define a single variable by specifying ARG once or many<br />
&nbsp;<wbr>&nbsp;variables by specifying ARG more than once. For example, a valid Dockerfile: </p>
<dl>
<dd>
<pre> FROM busybox
 ARG user1
 ARG buildno
 ...</pre>
</dl>
<p> A Dockerfile author may optionally specify a default value for an ARG instruction: </p>
<dl>
<dd>
<pre> FROM busybox
 ARG user1=someuser
 ARG buildno=1
 ...</pre>
</dl>
<p> If an ARG value has a default and if there is no value passed at build-time, the<br />
&nbsp;<wbr>&nbsp;builder uses the default. </p>
<p> An ARG variable definition comes into effect from the line on which it is<br />
&nbsp;<wbr>&nbsp;defined in the Dockerfile not from the argument&#8217;s use on the command-line or<br />
&nbsp;<wbr>&nbsp;elsewhere.&nbsp;<wbr>&nbsp;For example, consider this Dockerfile: </p>
<dl>
<dd>
<pre> 1 FROM busybox
 2 USER ${user:-some_user}
 3 ARG user
 4 USER $user
 ...</pre>
</dl>
<p> A user builds this file by calling: </p>
<dl>
<dd>
<pre> $ docker build --build-arg user=what_user Dockerfile</pre>
</dl>
<p> The USER at line 2 evaluates to some_user as the user variable is defined on the<br />
&nbsp;<wbr>&nbsp;subsequent line 3. The USER at line 4 evaluates to what_user as user is<br />
&nbsp;<wbr>&nbsp;defined and the what_user value was passed on the command line. Prior to its definition by an<br />
&nbsp;<wbr>&nbsp;ARG instruction, any use of a variable results in an empty string. </p>
<dl>
<dd><code>Warning:</code> It is not recommended to use build-time variables for<br />
&nbsp;passing secrets like github keys, user credentials etc. Build-time variable<br />
&nbsp;values are visible to any user of the image with the docker history command. </p>
</dl>
<p> You can use an ARG or an ENV instruction to specify variables that are<br />
&nbsp;<wbr>&nbsp;available to the RUN instruction. Environment variables defined using the<br />
&nbsp;<wbr>&nbsp;ENV instruction always override an ARG instruction of the same name. Consider<br />
&nbsp;<wbr>&nbsp;this Dockerfile with an ENV and ARG instruction. </p>
<dl>
<dd>
<pre> 1 FROM ubuntu
 2 ARG CONT_IMG_VER
 3 ENV CONT_IMG_VER=v1.0.0
 4 RUN echo $CONT_IMG_VER</pre>
</dl>
<p> Then, assume this image is built with this command: </p>
<dl>
<dd>
<pre> $ docker build --build-arg CONT_IMG_VER=v2.0.1 Dockerfile</pre>
</dl>
<p> In this case, the RUN instruction uses v1.0.0 instead of the ARG setting<br />
&nbsp;<wbr>&nbsp;passed by the user:v2.0.1 This behavior is similar to a shell<br />
&nbsp;<wbr>&nbsp;script where a locally scoped variable overrides the variables passed as<br />
&nbsp;<wbr>&nbsp;arguments or inherited from environment, from its point of definition. </p>
<p> Using the example above but a different ENV specification you can create more<br />
&nbsp;<wbr>&nbsp;useful interactions between ARG and ENV instructions: </p>
<dl>
<dd>
<pre> 1 FROM ubuntu
 2 ARG CONT_IMG_VER
 3 ENV CONT_IMG_VER=${CONT_IMG_VER:-v1.0.0}
 4 RUN echo $CONT_IMG_VER</pre>
</dl>
<p> Unlike an ARG instruction, ENV values are always persisted in the built<br />
&nbsp;<wbr>&nbsp;image. Consider a docker build without the &#8211;build-arg flag: </p>
<dl>
<dd>
<pre> $ docker build Dockerfile</pre>
</dl>
<p> Using this Dockerfile example, CONT_IMG_VER is still persisted in the image but<br />
&nbsp;<wbr>&nbsp;its value would be v1.0.0 as it is the default set in line 3 by the ENV instruction. </p>
<p> The variable expansion technique in this example allows you to pass arguments<br />
&nbsp;<wbr>&nbsp;from the command line and persist them in the final image by leveraging the<br />
&nbsp;<wbr>&nbsp;ENV instruction. Variable expansion is only supported for a limited set of<br />
&nbsp;<wbr>&nbsp;Dockerfile instructions. &lt;#environment-replacement&gt; </p>
<p> Docker has a set of predefined ARG variables that you can use without a<br />
&nbsp;<wbr>&nbsp;corresponding ARG instruction in the Dockerfile. </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>HTTP_PROXY</p>
<dt>&bull;</p>
<dd>http_proxy</p>
<dt>&bull;</p>
<dd>HTTPS_PROXY</p>
<dt>&bull;</p>
<dd>https_proxy</p>
<dt>&bull;</p>
<dd>FTP_PROXY</p>
<dt>&bull;</p>
<dd>ftp_proxy</p>
<dt>&bull;</p>
<dd>NO_PROXY</p>
<dt>&bull;</p>
<dd>no_proxy </p>
</dl>
</dl>
<p> To use these, pass them on the command line using &#8211;build-arg flag, for<br />
&nbsp;<wbr>&nbsp;example: </p>
<dl>
<dd>
<pre> $ docker build --build-arg HTTPS_PROXY=<a rel="nofollow" href="https://my-proxy.example.com">https://my-proxy.example.com</a> .</pre>
</dl>
<p> <code>ONBUILD</code><br />
&nbsp;<wbr>&nbsp;&#8212; ONBUILD&nbsp;[INSTRUCTION]<br />
&nbsp;<wbr>&nbsp;The&nbsp;<code>ONBUILD</code>&nbsp;instruction adds a trigger instruction to an image. The<br />
&nbsp;<wbr>&nbsp;trigger is executed at a later time, when the image is used as the base for<br />
&nbsp;<wbr>&nbsp;another build. Docker executes the trigger in the context of the downstream<br />
&nbsp;<wbr>&nbsp;build, as if the trigger existed immediately after the&nbsp;<code>FROM</code>&nbsp;instruction in<br />
&nbsp;<wbr>&nbsp;the downstream Dockerfile. </p>
<p> You can register any build instruction as a trigger. A trigger is useful if<br />
&nbsp;<wbr>&nbsp;you are defining an image to use as a base for building other images. For<br />
&nbsp;<wbr>&nbsp;example, if you are defining an application build environment or a daemon that<br />
&nbsp;<wbr>&nbsp;is customized with a user-specific configuration. </p>
<p> Consider an image intended as a reusable python application builder. It must<br />
&nbsp;<wbr>&nbsp;add application source code to a particular directory, and might need a build<br />
&nbsp;<wbr>&nbsp;script called after that. You can&#8217;t just call&nbsp;<code>ADD</code>&nbsp;and&nbsp;<code>RUN</code>&nbsp;now, because<br />
&nbsp;<wbr>&nbsp;you don&#8217;t yet have access to the application source code, and it is different<br />
&nbsp;<wbr>&nbsp;for each application build. </p>
<p> &#8212; Providing application developers with a boilerplate Dockerfile to copy-paste<br />
&nbsp;<wbr>&nbsp;into their application is inefficient, error-prone, and<br />
&nbsp;<wbr>&nbsp;difficult to update because it mixes with application-specific code.<br />
&nbsp;<wbr>&nbsp;The solution is to use&nbsp;<code>ONBUILD</code>&nbsp;to register instructions in advance, to<br />
&nbsp;<wbr>&nbsp;run later, during the next build stage.</p>
<h2>History</h2>
<p>*May 2014, Compiled by Zac Dover (zdover at redhat dot com) based on docker.com Dockerfile documentation. *Feb 2015, updated by Brian Goff (cpuguy83 [at] gmail.com) for readability *Sept 2015, updated by Sally O&#8217;Malley (somalley [at] redhat.com) *Oct 2016, updated by Addam Hardy (addam.hardy [at] gmail.com)</p>
