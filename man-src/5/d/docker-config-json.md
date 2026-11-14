---
title: "docker-config-json(5)"
name: "docker-config-json"
section: "5"
letter: "d"
url: "/docs/linux/man/5-docker-config-json/"
description: "HOME/.docker/config.json – Default Docker configuration file"
---

<p>HOME/.docker/config.json &#8211; Default Docker configuration file </p>
<h2>Introduction</h2>
<p>By default, the Docker command line stores its configuration files in a directory called .docker within your $HOME directory. Docker manages most of the files in the configuration directory and you should not modify them. However, you <i>can modify</i> the config.json file to control certain aspects of how the docker command behaves. </p>
<p> Currently, you can modify the docker command behavior using environment variables or command-line options. You can also use options within config.json to modify some of the same behavior. When using these mechanisms, you must keep in mind the order of precedence among them. Command line options override environment variables and environment variables override properties you specify in a config.json file. </p>
<p> The config.json file stores a JSON encoding of several properties: </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>The HttpHeaders property specifies a set of headers to include in all messages sent from the Docker client to the daemon. Docker does not try to interpret or understand these header; it simply puts them into the messages. Docker does not allow these headers to change any headers it sets for itself.</p>
<dt>&bull;</p>
<dd>The psFormat property specifies the default format for docker ps output. When the &#8211;format flag is not provided with the docker ps command, Docker&#8217;s client uses this property. If this property is not set, the client falls back to the default table format. For a list of supported formatting directives, see <code><a href="/docs/linux/man/1-docker-ps/">docker-ps</a>(1)</code>.</p>
<dt>&bull;</p>
<dd>The detachKeys property specifies the default key sequence which detaches the container. When the &#8211;detach-keys flag is not provide with the docker attach, docker exec, docker run or docker start, Docker&#8217;s client uses this property. If this property is not set, the client falls back to the default sequence ctrl-p,ctrl-q.</p>
<dt>&bull;</p>
<dd>The imagesFormat property specifies the default format for docker images output. When the &#8211;format flag is not provided with the docker images command, Docker&#8217;s client uses this property. If this property is not set, the client falls back to the default table format. For a list of supported formatting directives, see <code><a href="/docs/linux/man/1-docker-images/">docker-images</a>(1)</code>. </p>
</dl>
</dl>
<p> You can specify a different location for the configuration files via the DOCKER_CONFIG environment variable or the &#8211;config command line option. If both are specified, then the &#8211;config option overrides the DOCKER_CONFIG environment variable: </p>
<dl>
<dd>
<pre>docker --config ~/testconfigs/ ps</pre>
</dl>
<p> This command instructs Docker to use the configuration files in the ~/testconfigs/ directory when running the ps command.</p>
<h2>Examples</h2>
<p>Following is a sample config.json file: </p>
<pre><code>
{
    &quot;HttpHeaders&quot;: {
        &quot;MyHeader&quot;: &quot;MyValue&quot;
    },
    &quot;psFormat&quot;: &quot;table &#123;&#123;.ID}}\t&#123;&#123;.Image}}\t&#123;&#123;.Command}}\t&#123;&#123;.Labels}}&quot;,
    &quot;imagesFormat&quot;: &quot;table &#123;&#123;.ID}}\t&#123;&#123;.Repository}}\t&#123;&#123;.Tag}}\t&#123;&#123;.CreatedAt}}&quot;,
    &quot;detachKeys&quot;: &quot;ctrl-e,e&quot;
}

</code></pre>
<h2>History</h2>
<p>January 2016, created by Moxiegirl mary [at] docker.com &lt;mailto:mary [at] docker.com&gt;</p>
