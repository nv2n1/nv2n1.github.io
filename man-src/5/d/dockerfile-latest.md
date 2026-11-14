---
title: "dockerfile-latest(5)"
name: "dockerfile-latest"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dockerfile-latest/"
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
&nbsp;<wbr>&nbsp;<wbr>The path to the source repository defines where to find the context of the<br />
&nbsp;<wbr>&nbsp;<wbr>build. The build is run by the Docker daemon, not the CLI. The whole<br />
&nbsp;<wbr>&nbsp;<wbr>context must be transferred to the daemon. The Docker CLI reports<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;Sending build context to Docker daemon&quot;&nbsp;<wbr>when the context is sent to the<br />
&nbsp;<wbr>&nbsp;<wbr>daemon. </p>
<dl>
<dd>
<pre> docker build -t repository/tag .</pre>
</dl>
<p> &#8212; specifies a repository and tag at which to save the new image if the build<br />
&nbsp;<wbr>&nbsp;<wbr>succeeds. The Docker daemon runs the steps one-by-one, committing the result<br />
&nbsp;<wbr>&nbsp;<wbr>to a new image if necessary, before finally outputting the ID of the new<br />
&nbsp;<wbr>&nbsp;<wbr>image. The Docker daemon automatically cleans up the context it is given. </p>
<p> Docker re-uses intermediate images whenever possible. This significantly<br />
&nbsp;<wbr>&nbsp;<wbr>accelerates the&nbsp;<wbr><i>docker build</i>&nbsp;<wbr>process.</p>
<h2>Format</h2>
<p>FROM image </p>
<p> FROM image:tag </p>
<p> FROM image [at] digest </p>
<p> &#8212; The <code>FROM</code> instruction sets the base image for subsequent instructions. A<br />
&nbsp;<wbr>&nbsp;<wbr>valid Dockerfile must have&nbsp;<wbr><code>FROM</code>&nbsp;<wbr>as its first instruction. The image can be any<br />
&nbsp;<wbr>&nbsp;<wbr>valid image. It is easy to start by pulling an image from the public<br />
&nbsp;<wbr>&nbsp;<wbr>repositories. </p>
<p> &#8212; <code>FROM</code> must be the first non-comment instruction in Dockerfile. </p>
<p> &#8212; <code>FROM</code> may appear multiple times within a single Dockerfile in order to create<br />
&nbsp;<wbr>&nbsp;<wbr>multiple images. Make a note of the last image ID output by the commit before<br />
&nbsp;<wbr>&nbsp;<wbr>each new&nbsp;<wbr><code>FROM</code>&nbsp;<wbr>command. </p>
<p> &#8212; If no tag is given to the <code>FROM</code> instruction, Docker applies the<br />
&nbsp;<wbr>&nbsp;<wbr>latest tag. If the used tag does not exist, an error is returned. </p>
<p> &#8212; If no digest is given to the <code>FROM</code> instruction, Docker applies the<br />
&nbsp;<wbr>&nbsp;<wbr>latest tag. If the used tag does not exist, an error is returned. </p>
<p> <code>MAINTAINER</code><br />
&nbsp;<wbr>&nbsp;<wbr>&#8212;&nbsp;<wbr><code>MAINTAINER</code>&nbsp;<wbr>sets the Author field for the generated images.<br />
&nbsp;<wbr>&nbsp;<wbr>Useful for providing users with an email or url for support. </p>
<p> <code>RUN</code><br />
&nbsp;<wbr>&nbsp;<wbr>&#8212;&nbsp;<wbr><code>RUN</code>&nbsp;<wbr>has two forms: </p>
<dl>
<dd>
<pre> # the command is run in a shell - /bin/sh -c
 RUN &lt;command&gt;
 # Executable form
 RUN [&quot;executable&quot;, &quot;param1&quot;, &quot;param2&quot;]</pre>
</dl>
<p> &#8212; The <code>RUN</code> instruction executes any commands in a new layer on top of the current<br />
&nbsp;<wbr>&nbsp;<wbr>image and commits the results. The committed image is used for the next step in<br />
&nbsp;<wbr>&nbsp;<wbr>Dockerfile. </p>
<p> &#8212; Layering <code>RUN</code> instructions and generating commits conforms to the core<br />
&nbsp;<wbr>&nbsp;<wbr>concepts of Docker where commits are cheap and containers can be created from<br />
&nbsp;<wbr>&nbsp;<wbr>any point in the history of an image. This is similar to source control.&nbsp;<wbr>&nbsp;<wbr>The<br />
&nbsp;<wbr>&nbsp;<wbr>exec form makes it possible to avoid shell string munging. The exec form makes<br />
&nbsp;<wbr>&nbsp;<wbr>it possible to&nbsp;<wbr><code>RUN</code>&nbsp;<wbr>commands using a base image that does not contain&nbsp;<wbr>/bin/sh. </p>
<p> Note that the exec form is parsed as a JSON array, which means that you must<br />
&nbsp;<wbr>&nbsp;<wbr>use double-quotes&nbsp;<wbr>(&quot;)&nbsp;<wbr>around words not single-quotes&nbsp;<wbr>(&#8216;). </p>
<p> <code>CMD</code><br />
&nbsp;<wbr>&nbsp;<wbr>&#8212;&nbsp;<wbr><code>CMD</code>&nbsp;<wbr>has three forms: </p>
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
&nbsp;<wbr>&nbsp;<wbr>the last&nbsp;<wbr><code>CMD</code>&nbsp;<wbr>takes effect.<br />
&nbsp;<wbr>&nbsp;<wbr>The main purpose of a&nbsp;<wbr><code>CMD</code>&nbsp;<wbr>is to provide defaults for an executing container.<br />
&nbsp;<wbr>&nbsp;<wbr>These defaults may include an executable, or they can omit the executable. If<br />
&nbsp;<wbr>&nbsp;<wbr>they omit the executable, an&nbsp;<wbr><code>ENTRYPOINT</code>&nbsp;<wbr>must be specified.<br />
&nbsp;<wbr>&nbsp;<wbr>When used in the shell or exec formats, the&nbsp;<wbr><code>CMD</code>&nbsp;<wbr>instruction sets the command to<br />
&nbsp;<wbr>&nbsp;<wbr>be executed when running the image.<br />
&nbsp;<wbr>&nbsp;<wbr>If you use the shell form of the&nbsp;<wbr><code>CMD</code>, the&nbsp;<wbr>&lt;command&gt;&nbsp;<wbr>executes in&nbsp;<wbr>/bin/sh -c: </p>
<p> Note that the exec form is parsed as a JSON array, which means that you must<br />
&nbsp;<wbr>&nbsp;<wbr>use double-quotes&nbsp;<wbr>(&quot;)&nbsp;<wbr>around words not single-quotes&nbsp;<wbr>(&#8216;). </p>
<dl>
<dd>
<pre> FROM ubuntu
 CMD echo &quot;This is a test.&quot; | wc -</pre>
</dl>
<p> &#8212; If you run <code>command</code> without a shell, then you must express the command as a<br />
&nbsp;<wbr>&nbsp;<wbr>JSON array and give the full path to the executable. This array form is the<br />
&nbsp;<wbr>&nbsp;<wbr>preferred form of&nbsp;<wbr><code>CMD</code>. All additional parameters must be individually expressed<br />
&nbsp;<wbr>&nbsp;<wbr>as strings in the array: </p>
<dl>
<dd>
<pre> FROM ubuntu
 CMD [&quot;/usr/bin/wc&quot;,&quot;--help&quot;]</pre>
</dl>
<p> &#8212; To make the container run the same executable every time, use <code>ENTRYPOINT</code> in<br />
&nbsp;<wbr>&nbsp;<wbr>combination with&nbsp;<wbr><code>CMD</code>.<br />
&nbsp;<wbr>&nbsp;<wbr>If the user specifies arguments to docker run, the specified commands<br />
&nbsp;<wbr>&nbsp;<wbr>override the default in&nbsp;<wbr><code>CMD</code>.<br />
&nbsp;<wbr>&nbsp;<wbr>Do not confuse&nbsp;<wbr><code>RUN</code>&nbsp;<wbr>with&nbsp;<wbr><code>CMD</code>.&nbsp;<wbr><code>RUN</code>&nbsp;<wbr>runs a command and commits the result.<br />
&nbsp;<wbr>&nbsp;<wbr><code>CMD</code>&nbsp;<wbr>executes nothing at build time, but specifies the intended command for<br />
&nbsp;<wbr>&nbsp;<wbr>the image. </p>
<p> <code>LABEL</code><br />
&nbsp;<wbr>&nbsp;<wbr>&#8212; LABEL&nbsp;<wbr>&lt;key&gt;=&lt;value&gt;&nbsp;<wbr>[&lt;key&gt;=&lt;value&gt;&nbsp;<wbr>&#8230;]or </p>
<dl>
<dd>
<pre> LABEL &lt;key&gt;[ &lt;value&gt;]
 LABEL &lt;key&gt;[ &lt;value&gt;]
 ...</pre>
</dl>
<p> The <code>LABEL</code> instruction adds metadata to an image. A <code>LABEL</code> is a<br />
&nbsp;<wbr>&nbsp;<wbr>key-value pair. To specify a&nbsp;<wbr><code>LABEL</code>&nbsp;<wbr>without a value, simply use an empty<br />
&nbsp;<wbr>&nbsp;<wbr>string. To include spaces within a&nbsp;<wbr><code>LABEL</code>&nbsp;<wbr>value, use quotes and<br />
&nbsp;<wbr>&nbsp;<wbr>backslashes as you would in command-line parsing. </p>
<dl>
<dd>
<pre> LABEL com.example.vendor=&quot;ACME Incorporated&quot;
 LABEL com.example.vendor &quot;ACME Incorporated&quot;
 LABEL com.example.vendor.is-beta &quot;&quot;
 LABEL com.example.vendor.is-beta=
 LABEL com.example.vendor.is-beta=&quot;&quot;</pre>
</dl>
<p> An image can have more than one label. To specify multiple labels, separate<br />
&nbsp;<wbr>&nbsp;<wbr>each key-value pair by a space. </p>
<p> Labels are additive including LABELs in FROM images. As the system<br />
&nbsp;<wbr>&nbsp;<wbr>encounters and then applies a new label, new keys override any previous<br />
&nbsp;<wbr>&nbsp;<wbr>labels with identical keys. </p>
<p> To display an image&#8217;s labels, use the docker inspect command. </p>
<p> <code>EXPOSE</code><br />
&nbsp;<wbr>&nbsp;<wbr>&#8212; EXPOSE&nbsp;<wbr>&lt;port&gt;&nbsp;<wbr>[&lt;port&gt;&#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr>The&nbsp;<wbr><code>EXPOSE</code>&nbsp;<wbr>instruction informs Docker that the container listens on the<br />
&nbsp;<wbr>&nbsp;<wbr>specified network ports at runtime. Docker uses this information to<br />
&nbsp;<wbr>&nbsp;<wbr>interconnect containers using links and to set up port redirection on the host<br />
&nbsp;<wbr>&nbsp;<wbr>system. </p>
<p> <code>ENV</code><br />
&nbsp;<wbr>&nbsp;<wbr>&#8212; ENV&nbsp;<wbr>&lt;key&gt;&nbsp;<wbr>&lt;value&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>The&nbsp;<wbr><code>ENV</code>&nbsp;<wbr>instruction sets the environment variable&nbsp;<wbr>&lt;key&gt;&nbsp;<wbr>to<br />
&nbsp;<wbr>&nbsp;<wbr>the value&nbsp;<wbr>&lt;value&gt;. This value is passed to all future<br />
&nbsp;<wbr>&nbsp;<wbr><code>RUN</code>,&nbsp;<wbr><code>ENTRYPOINT</code>, and&nbsp;<wbr><code>CMD</code>&nbsp;<wbr>instructions. This is<br />
&nbsp;<wbr>&nbsp;<wbr>functionally equivalent to prefixing the command with&nbsp;<wbr>&lt;key&gt;=&lt;value&gt;.&nbsp;<wbr>&nbsp;<wbr>The<br />
&nbsp;<wbr>&nbsp;<wbr>environment variables that are set with&nbsp;<wbr><code>ENV</code>&nbsp;<wbr>persist when a container is run<br />
&nbsp;<wbr>&nbsp;<wbr>from the resulting image. Use docker inspect to inspect these values, and<br />
&nbsp;<wbr>&nbsp;<wbr>change them using docker run &#8211;env&nbsp;<wbr>&lt;key&gt;=&lt;value&gt;. </p>
<p> Note that setting &quot;ENV DEBIAN_FRONTEND noninteractive&quot; may cause<br />
&nbsp;<wbr>&nbsp;<wbr>unintended consequences, because it will persist when the container is run<br />
&nbsp;<wbr>&nbsp;<wbr>interactively, as with the following command: docker run -t -i image bash </p>
<p> <code>ADD</code><br />
&nbsp;<wbr>&nbsp;<wbr>&#8212;&nbsp;<wbr><code>ADD</code>&nbsp;<wbr>has two forms: </p>
<dl>
<dd>
<pre> ADD &lt;src&gt; &lt;dest&gt;
 # Required for paths with whitespace
 ADD [&quot;&lt;src&gt;&quot;,... &quot;&lt;dest&gt;&quot;]</pre>
</dl>
<p> The <code>ADD</code> instruction copies new files, directories<br />
&nbsp;<wbr>&nbsp;<wbr>or remote file URLs to the filesystem of the container at path&nbsp;<wbr>&lt;dest&gt;.<br />
&nbsp;<wbr>&nbsp;<wbr>Multiple&nbsp;<wbr>&lt;src&gt;&nbsp;<wbr>resources may be specified but if they are files or directories<br />
&nbsp;<wbr>&nbsp;<wbr>then they must be relative to the source directory that is being built<br />
&nbsp;<wbr>&nbsp;<wbr>(the context of the build). The&nbsp;<wbr>&lt;dest&gt;&nbsp;<wbr>is the absolute path, or path relative<br />
&nbsp;<wbr>&nbsp;<wbr>to&nbsp;<wbr><code>WORKDIR</code>, into which the source is copied inside the target container.<br />
&nbsp;<wbr>&nbsp;<wbr>If the&nbsp;<wbr>&lt;src&gt;&nbsp;<wbr>argument is a local file in a recognized compression format<br />
&nbsp;<wbr>&nbsp;<wbr>(tar, gzip, bzip2, etc)&nbsp;<wbr>then it is unpacked at the specified&nbsp;<wbr>&lt;dest&gt;&nbsp;<wbr>in the<br />
&nbsp;<wbr>&nbsp;<wbr>container&#8217;s filesystem.&nbsp;<wbr>&nbsp;<wbr>Note that only local compressed files will be unpacked,<br />
&nbsp;<wbr>&nbsp;<wbr>i.e., the URL download and archive unpacking features cannot be used together.<br />
&nbsp;<wbr>&nbsp;<wbr>All new directories are created with mode 0755 and with the uid and gid of&nbsp;<wbr><code>0</code>. </p>
<p> <code>COPY</code><br />
&nbsp;<wbr>&nbsp;<wbr>&#8212;&nbsp;<wbr><code>COPY</code>&nbsp;<wbr>has two forms: </p>
<dl>
<dd>
<pre> COPY &lt;src&gt; &lt;dest&gt;
 # Required for paths with whitespace
 COPY [&quot;&lt;src&gt;&quot;,... &quot;&lt;dest&gt;&quot;]</pre>
</dl>
<p> The <code>COPY</code> instruction copies new files from &lt;src&gt; and<br />
&nbsp;<wbr>&nbsp;<wbr>adds them to the filesystem of the container at path&nbsp;<wbr>&lt;dest&gt;. The&nbsp;<wbr>&lt;src&gt;&nbsp;<wbr>must be<br />
&nbsp;<wbr>&nbsp;<wbr>the path to a file or directory relative to the source directory that is<br />
&nbsp;<wbr>&nbsp;<wbr>being built&nbsp;<wbr>(the context of the build)&nbsp;<wbr>or a remote file URL. The&nbsp;<wbr>&lt;dest&gt;&nbsp;<wbr>is an<br />
&nbsp;<wbr>&nbsp;<wbr>absolute path, or a path relative to&nbsp;<wbr><code>WORKDIR</code>, into which the source will<br />
&nbsp;<wbr>&nbsp;<wbr>be copied inside the target container. If you&nbsp;<wbr><code>COPY</code>&nbsp;<wbr>an archive file it will<br />
&nbsp;<wbr>&nbsp;<wbr>land in the container exactly as it appears in the build context without any<br />
&nbsp;<wbr>&nbsp;<wbr>attempt to unpack it.&nbsp;<wbr>&nbsp;<wbr>All new files and directories are created with mode&nbsp;<wbr><code>0755</code><br />
&nbsp;<wbr>&nbsp;<wbr>and with the uid and gid of&nbsp;<wbr><code>0</code>. </p>
<p> <code>ENTRYPOINT</code><br />
&nbsp;<wbr>&nbsp;<wbr>&#8212;&nbsp;<wbr><code>ENTRYPOINT</code>&nbsp;<wbr>has two forms: </p>
<dl>
<dd>
<pre> # executable form
 ENTRYPOINT [&quot;executable&quot;, &quot;param1&quot;, &quot;param2&quot;]`
 # run command in a shell - /bin/sh -c
 ENTRYPOINT command param1 param2</pre>
</dl>
<p> &#8212; An <code>ENTRYPOINT</code> helps you configure a<br />
&nbsp;<wbr>&nbsp;<wbr>container that can be run as an executable. When you specify an&nbsp;<wbr><code>ENTRYPOINT</code>,<br />
&nbsp;<wbr>&nbsp;<wbr>the whole container runs as if it was only that executable.&nbsp;<wbr>&nbsp;<wbr>The&nbsp;<wbr><code>ENTRYPOINT</code><br />
&nbsp;<wbr>&nbsp;<wbr>instruction adds an entry command that is not overwritten when arguments are<br />
&nbsp;<wbr>&nbsp;<wbr>passed to docker run. This is different from the behavior of&nbsp;<wbr><code>CMD</code>. This allows<br />
&nbsp;<wbr>&nbsp;<wbr>arguments to be passed to the entrypoint, for instance docker run&nbsp;<wbr>&lt;image&gt;&nbsp;<wbr>-d<br />
&nbsp;<wbr>&nbsp;<wbr>passes the -d argument to the&nbsp;<wbr><code>ENTRYPOINT</code>.&nbsp;<wbr>&nbsp;<wbr>Specify parameters either in the<br />
&nbsp;<wbr>&nbsp;<wbr><code>ENTRYPOINT</code>&nbsp;<wbr>JSON array&nbsp;<wbr>(as in the preferred exec form above), or by using a&nbsp;<wbr><code>CMD</code><br />
&nbsp;<wbr>&nbsp;<wbr>statement.&nbsp;<wbr>&nbsp;<wbr>Parameters in the&nbsp;<wbr><code>ENTRYPOINT</code>&nbsp;<wbr>are not overwritten by the docker run<br />
&nbsp;<wbr>&nbsp;<wbr>arguments.&nbsp;<wbr>&nbsp;<wbr>Parameters specified via&nbsp;<wbr><code>CMD</code>&nbsp;<wbr>are overwritten by docker run<br />
&nbsp;<wbr>&nbsp;<wbr>arguments.&nbsp;<wbr>&nbsp;<wbr>Specify a plain string for the&nbsp;<wbr><code>ENTRYPOINT</code>, and it will execute in<br />
&nbsp;<wbr>&nbsp;<wbr>/bin/sh -c, like a&nbsp;<wbr><code>CMD</code>&nbsp;<wbr>instruction: </p>
<dl>
<dd>
<pre> FROM ubuntu
 ENTRYPOINT wc -l -</pre>
</dl>
<p> This means that the Dockerfile&#8217;s image always takes stdin as input (that&#8217;s<br />
&nbsp;<wbr>&nbsp;<wbr>what&nbsp;<wbr>&quot;-&quot;&nbsp;<wbr>means), and prints the number of lines&nbsp;<wbr>(that&#8217;s what&nbsp;<wbr>&quot;-l&quot;&nbsp;<wbr>means). To<br />
&nbsp;<wbr>&nbsp;<wbr>make this optional but default, use a&nbsp;<wbr><code>CMD</code>: </p>
<dl>
<dd>
<pre> FROM ubuntu
 CMD [&quot;-l&quot;, &quot;-&quot;]
 ENTRYPOINT [&quot;/usr/bin/wc&quot;]</pre>
</dl>
<p> <code>VOLUME</code><br />
&nbsp;<wbr>&nbsp;<wbr>&#8212; VOLUME&nbsp;<wbr>[&quot;/data&quot;]<br />
&nbsp;<wbr>&nbsp;<wbr>The&nbsp;<wbr><code>VOLUME</code>&nbsp;<wbr>instruction creates a mount point with the specified name and marks<br />
&nbsp;<wbr>&nbsp;<wbr>it as holding externally-mounted volumes from the native host or from other<br />
&nbsp;<wbr>&nbsp;<wbr>containers. </p>
<p> <code>USER</code><br />
&nbsp;<wbr>&nbsp;<wbr>&#8212; USER daemon<br />
&nbsp;<wbr>&nbsp;<wbr>Sets the username or UID used for running subsequent commands. </p>
<p> The <code>USER</code> instruction can optionally be used to set the group or GID. The<br />
&nbsp;<wbr>&nbsp;<wbr>followings examples are all valid:<br />
&nbsp;<wbr>&nbsp;<wbr>USER&nbsp;<wbr>[user | user:group | uid | uid:gid | user:gid | uid:group&nbsp;<wbr>] </p>
<p> Until the <code>USER</code> instruction is set, instructions will be run as root. The USER<br />
&nbsp;<wbr>&nbsp;<wbr>instruction can be used any number of times in a Dockerfile, and will only affect<br />
&nbsp;<wbr>&nbsp;<wbr>subsequent commands. </p>
<p> <code>WORKDIR</code><br />
&nbsp;<wbr>&nbsp;<wbr>&#8212; WORKDIR&nbsp;<wbr>/path/to/workdir<br />
&nbsp;<wbr>&nbsp;<wbr>The&nbsp;<wbr><code>WORKDIR</code>&nbsp;<wbr>instruction sets the working directory for the&nbsp;<wbr><code>RUN</code>,&nbsp;<wbr><code>CMD</code>,<br />
&nbsp;<wbr>&nbsp;<wbr><code>ENTRYPOINT</code>,&nbsp;<wbr><code>COPY</code>&nbsp;<wbr>and&nbsp;<wbr><code>ADD</code>&nbsp;<wbr>Dockerfile commands that follow it. It can<br />
&nbsp;<wbr>&nbsp;<wbr>be used multiple times in a single Dockerfile. Relative paths are defined<br />
&nbsp;<wbr>&nbsp;<wbr>relative to the path of the previous&nbsp;<wbr><code>WORKDIR</code>&nbsp;<wbr>instruction. For example: </p>
<dl>
<dd>
<pre> WORKDIR /a
 WORKDIR b
 WORKDIR c
 RUN pwd</pre>
</dl>
<p> In the above example, the output of the <code>pwd</code> command is <code>a/b/c</code>. </p>
<p> <code>ARG</code><br />
&#8212; ARG&nbsp;<wbr>&lt;name&gt;[=&lt;default value&gt;] </p>
<p> The ARG instruction defines a variable that users can pass at build-time to<br />
&nbsp;<wbr>&nbsp;<wbr>the builder with the docker build command using the &#8211;build-arg<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;varname&gt;=&lt;value&gt;&nbsp;<wbr>flag. If a user specifies a build argument that was not<br />
&nbsp;<wbr>&nbsp;<wbr>defined in the Dockerfile, the build outputs an error. </p>
<dl>
<dd>
<pre> One or more build-args were not consumed, failing build.</pre>
</dl>
<p> The Dockerfile author can define a single variable by specifying ARG once or many<br />
&nbsp;<wbr>&nbsp;<wbr>variables by specifying ARG more than once. For example, a valid Dockerfile: </p>
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
&nbsp;<wbr>&nbsp;<wbr>builder uses the default. </p>
<p> An ARG variable definition comes into effect from the line on which it is<br />
&nbsp;<wbr>&nbsp;<wbr>defined in the Dockerfile not from the argument&#8217;s use on the command-line or<br />
&nbsp;<wbr>&nbsp;<wbr>elsewhere.&nbsp;<wbr>&nbsp;<wbr>For example, consider this Dockerfile: </p>
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
&nbsp;<wbr>&nbsp;<wbr>subsequent line 3. The USER at line 4 evaluates to what_user as user is<br />
&nbsp;<wbr>&nbsp;<wbr>defined and the what_user value was passed on the command line. Prior to its definition by an<br />
&nbsp;<wbr>&nbsp;<wbr>ARG instruction, any use of a variable results in an empty string. </p>
<dl>
<dd><code>Warning:</code> It is not recommended to use build-time variables for<br />
&nbsp;<wbr>passing secrets like github keys, user credentials etc. Build-time variable<br />
&nbsp;<wbr>values are visible to any user of the image with the docker history command.</dl>
<p> You can use an ARG or an ENV instruction to specify variables that are<br />
&nbsp;<wbr>&nbsp;<wbr>available to the RUN instruction. Environment variables defined using the<br />
&nbsp;<wbr>&nbsp;<wbr>ENV instruction always override an ARG instruction of the same name. Consider<br />
&nbsp;<wbr>&nbsp;<wbr>this Dockerfile with an ENV and ARG instruction. </p>
<dl>
<dd>
<pre> 1 FROM ubuntu
 2 ARG CONT_IMG_VER
 3 ENV CONT_IMG_VER v1.0.0
 4 RUN echo $CONT_IMG_VER</pre>
</dl>
<p> Then, assume this image is built with this command: </p>
<dl>
<dd>
<pre> $ docker build --build-arg CONT_IMG_VER=v2.0.1 Dockerfile</pre>
</dl>
<p> In this case, the RUN instruction uses v1.0.0 instead of the ARG setting<br />
&nbsp;<wbr>&nbsp;<wbr>passed by the user:v2.0.1 This behavior is similar to a shell<br />
&nbsp;<wbr>&nbsp;<wbr>script where a locally scoped variable overrides the variables passed as<br />
&nbsp;<wbr>&nbsp;<wbr>arguments or inherited from environment, from its point of definition. </p>
<p> Using the example above but a different ENV specification you can create more<br />
&nbsp;<wbr>&nbsp;<wbr>useful interactions between ARG and ENV instructions: </p>
<dl>
<dd>
<pre> 1 FROM ubuntu
 2 ARG CONT_IMG_VER
 3 ENV CONT_IMG_VER ${CONT_IMG_VER:-v1.0.0}
 4 RUN echo $CONT_IMG_VER</pre>
</dl>
<p> Unlike an ARG instruction, ENV values are always persisted in the built<br />
&nbsp;<wbr>&nbsp;<wbr>image. Consider a docker build without the &#8211;build-arg flag: </p>
<dl>
<dd>
<pre> $ docker build Dockerfile</pre>
</dl>
<p> Using this Dockerfile example, CONT_IMG_VER is still persisted in the image but<br />
&nbsp;<wbr>&nbsp;<wbr>its value would be v1.0.0 as it is the default set in line 3 by the ENV instruction. </p>
<p> The variable expansion technique in this example allows you to pass arguments<br />
&nbsp;<wbr>&nbsp;<wbr>from the command line and persist them in the final image by leveraging the<br />
&nbsp;<wbr>&nbsp;<wbr>ENV instruction. Variable expansion is only supported for&nbsp;<wbr> &lt;#environment-replacement&gt; </p>
<p> Docker has a set of predefined ARG variables that you can use without a<br />
&nbsp;<wbr>&nbsp;<wbr>corresponding ARG instruction in the Dockerfile.</p>
<dl>
<dt>step]</p>
<dd>item HTTP_PROXY item http_proxy item HTTPS_PROXY item https_proxy item FTP_PROXY item ftp_proxy item NO_PROXY item no_proxy</dl>
<p> To use these, simply pass them on the command line using the &#8211;build-arg<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;varname&gt;=&lt;value&gt;&nbsp;<wbr>flag. </p>
<p> <code>ONBUILD</code><br />
&nbsp;<wbr>&nbsp;<wbr>&#8212; ONBUILD&nbsp;<wbr>[INSTRUCTION]<br />
&nbsp;<wbr>&nbsp;<wbr>The&nbsp;<wbr><code>ONBUILD</code>&nbsp;<wbr>instruction adds a trigger instruction to an image. The<br />
&nbsp;<wbr>&nbsp;<wbr>trigger is executed at a later time, when the image is used as the base for<br />
&nbsp;<wbr>&nbsp;<wbr>another build. Docker executes the trigger in the context of the downstream<br />
&nbsp;<wbr>&nbsp;<wbr>build, as if the trigger existed immediately after the&nbsp;<wbr><code>FROM</code>&nbsp;<wbr>instruction in<br />
&nbsp;<wbr>&nbsp;<wbr>the downstream Dockerfile. </p>
<p> You can register any build instruction as a trigger. A trigger is useful if<br />
&nbsp;<wbr>&nbsp;<wbr>you are defining an image to use as a base for building other images. For<br />
&nbsp;<wbr>&nbsp;<wbr>example, if you are defining an application build environment or a daemon that<br />
&nbsp;<wbr>&nbsp;<wbr>is customized with a user-specific configuration. </p>
<p> Consider an image intended as a reusable python application builder. It must<br />
&nbsp;<wbr>&nbsp;<wbr>add application source code to a particular directory, and might need a build<br />
&nbsp;<wbr>&nbsp;<wbr>script called after that. You can&#8217;t just call&nbsp;<wbr><code>ADD</code>&nbsp;<wbr>and&nbsp;<wbr><code>RUN</code>&nbsp;<wbr>now, because<br />
&nbsp;<wbr>&nbsp;<wbr>you don&#8217;t yet have access to the application source code, and it is different<br />
&nbsp;<wbr>&nbsp;<wbr>for each application build. </p>
<p> &#8212; Providing application developers with a boilerplate Dockerfile to copy-paste<br />
&nbsp;<wbr>&nbsp;<wbr>into their application is inefficient, error-prone, and<br />
&nbsp;<wbr>&nbsp;<wbr>difficult to update because it mixes with application-specific code.<br />
&nbsp;<wbr>&nbsp;<wbr>The solution is to use&nbsp;<wbr><code>ONBUILD</code>&nbsp;<wbr>to register instructions in advance, to<br />
&nbsp;<wbr>&nbsp;<wbr>run later, during the next build stage.</p>
<h2>History</h2>
<p>*May 2014, Compiled by Zac Dover (zdover at redhat dot com) based on docker.com Dockerfile documentation. *Feb 2015, updated by Brian Goff (cpuguy83 [at] gmail.com) for readability *Sept 2015, updated by Sally O&#8217;Malley (somalley [at] redhat.com)</p>
