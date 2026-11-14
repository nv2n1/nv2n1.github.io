---
title: "pkcon(1)"
name: "pkcon"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pkcon/"
description: "pkcon – PackageKit console client"
---

<h2 class="name">NAME</h2>
<p> pkcon &#8211; PackageKit console client </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pkcon</code> [<code>OPTION</code>&#8230;] [<code>COMMAND</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>This manual page documents briefly the <code>pkcon</code> command. </p>
<p> <code>pkcon</code> is the command line client for PackageKit.</p>
<h2>COMMANDS</h2>
<p> pkcon knows about the following commands. Depending on the backend in use, not all of them may be available. </p>
<p> backend-details</p>
<dl>
<dt>
<dd> Print information about the PackageKit backend in use.</dl>
<p> get-roles</p>
<dl>
<dt>
<dd> List the roles that a transaction can have.</dl>
<p> get-groups</p>
<dl>
<dt>
<dd> List the available package groups.</dl>
<p> get-filters</p>
<dl>
<dt>
<dd> List the available filters.</dl>
<p> get-transactions</p>
<dl>
<dt>
<dd> List known transactions.</dl>
<p> get-time <i>ROLE</i></p>
<dl>
<dt>
<dd> Print the time that has passed since the last transaction with the given role.</dl>
<p> search [name|details|group|file] <i>DATA</i></p>
<dl>
<dt>
<dd> Search for a package matching the given data. The search is performed in the package information that is indicated by the first argument: name, details, group or files.</dl>
<p> install <i>PACKAGES</i></p>
<dl>
<dt>
<dd> Install the given packages from repositories.</dl>
<p> install-local <i>FILES</i></p>
<dl>
<dt>
<dd> Install the given packages from the local filesystem.</dl>
<p> download <i>DIRECTORY</i> <i>PACKAGES</i></p>
<dl>
<dt>
<dd> Download the given packages from repositories, and store them in the given directory.</dl>
<p> install-sig <i>TYPE</i> <i>KEY_ID</i> <i>PACKAGE</i></p>
<dl>
<dt>
<dd> Install a package signature. Only GPG signatures are supported at this time.</dl>
<p> remove <i>PACKAGE</i></p>
<dl>
<dt>
<dd> Remove the given package.</dl>
<p> update [<i>PACKAGES</i>]</p>
<dl>
<dt>
<dd> Update the system by installing available updates. If a list of packages is specified, only install updates for these packages.</dl>
<p> refresh [force]</p>
<dl>
<dt>
<dd> Refresh the cached information about available updates.</dl>
<p> resolve <i>PACKAGE</i></p>
<dl>
<dt>
<dd> Resolve the given package name and print information about installed or available packages and updates.</dl>
<p> upgrade-system <i>DISTRIBUTION</i> [minimal|default|complete]</p>
<dl>
<dt>
<dd> Upgrade the system to the given distribution.</dl>
<p> get-updates</p>
<dl>
<dt>
<dd> List available updates.</dl>
<p> get-distro-upgrades</p>
<dl>
<dt>
<dd> List available distribution upgrades.</dl>
<p> depends-on <i>PACKAGE</i></p>
<dl>
<dt>
<dd> List dependencies fo the given package.</dl>
<p> required-by <i>PACKAGE</i></p>
<dl>
<dt>
<dd> List packages that require the given package.</dl>
<p> get-details <i>PACKAGE</i></p>
<dl>
<dt>
<dd> Print details about the available or installed package with the given name.</dl>
<p> get-details-local <i>FILE</i></p>
<dl>
<dt>
<dd> Print details about the local package.</dl>
<p> get-files <i>PACKAGE</i></p>
<dl>
<dt>
<dd> List the files contained in the given package.</dl>
<p> get-files-local <i>FILE</i></p>
<dl>
<dt>
<dd> List the files contained in the local package.</dl>
<p> get-update-detail <i>PACKAGE</i></p>
<dl>
<dt>
<dd> Print the package changelog for the given package.</dl>
<p> get-packages</p>
<dl>
<dt>
<dd> List all available and installed packages.</dl>
<p> repo-list</p>
<dl>
<dt>
<dd> List all configured package repositories.</dl>
<p> repo-enable <i>REPOSITORY</i></p>
<dl>
<dt>
<dd> Enable the given repository.</dl>
<p> repo-disable <i>REPOSITORY</i></p>
<dl>
<dt>
<dd> Disable the given repository.</dl>
<p> repo-set-data <i>REPOSITORY</i> <i>PARAMETER</i> <i>DATA</i></p>
<dl>
<dt>
<dd> Set the given parameter to the given value for the repository.</dl>
<p> repo-remove <i>REPOSITORY</i> <i>PARAMETER</i></p>
<dl>
<dt>
<dd> Removes the repository and optionally any packages installed from it.</dl>
<p> what-provides <i>STRING</i></p>
<dl>
<dt>
<dd> List packages that provide the given string.</dl>
<p> accept-eula <i>EULA_ID</i></p>
<dl>
<dt>
<dd> Accept the EULA with the given id.</dl>
<p> get-categories</p>
<dl>
<dt>
<dd> List available categories.</dl>
<p> repair</p>
<dl>
<dt>
<dd> Attempt to repair the system package database.</dl>
<p> offline-get-prepared</p>
<dl>
<dt>
<dd> Print information about the prepared offline update. If no offline update is prepared, exit with an exit code of 1.</dl>
<p> offline-trigger</p>
<dl>
<dt>
<dd> Trigger an offline update.</dl>
<p> offline-status</p>
<dl>
<dt>
<dd> Print information about the result of the last offline update.</dl>
<h2>OPTIONS</h2>
<p> The following options can be used to influence the behavior of <code>pkcon</code>. </p>
<p> &#8211;version</p>
<dl>
<dt>
<dd> Print the program version and exit.</dl>
<p> -h, &#8211;help</p>
<dl>
<dt>
<dd> Show help options.</dl>
<p> &#8211;help-all</p>
<dl>
<dt>
<dd> Show all help options.</dl>
<p> &#8211;filter <i>FILTER</i></p>
<dl>
<dt>
<dd> Set the filter to use.</dl>
<p> -y, &#8211;noninteractive</p>
<dl>
<dt>
<dd> Install packages without asking for confirmation.</dl>
<p> &#8211;only-download</p>
<dl>
<dt>
<dd> Prepare the transaction by downloading packages only.</dl>
<p> -n, &#8211;background</p>
<dl>
<dt>
<dd> Run the command using idle network bandwidth and also using less power.</dl>
<p> -p, &#8211;plain</p>
<dl>
<dt>
<dd> Print to screen a machine-readable output, rather than using animated widgets.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Show debugging information.</dl>
<p> -c, &#8211;cache-age <i>AGE</i></p>
<dl>
<dt>
<dd> Set the maximum acceptable age for cached metadata, in seconds. Use -1 for &#8216;never&#8217;.</dl>
<p> &#8211;allow-untrusted</p>
<dl>
<dt>
<dd> Allow untrusted packages to be installed.</dl>
<p> &#8211;allow-downgrade</p>
<dl>
<dt>
<dd> Allow packages to be downgraded during transaction.</dl>
<p> &#8211;allow-reinstall</p>
<dl>
<dt>
<dd> Allow packages to be reinstalled during transaction.</dl>
<h2>RETURN VALUES</h2>
<p> <code>0</code></p>
<dl>
<dt>
<dd> Success</dl>
<p> <code>1</code></p>
<dl>
<dt>
<dd> Failed with miscellaneous internal error.</dl>
<p> <code>3</code></p>
<dl>
<dt>
<dd> Failed with syntax error, or failed to parse command.</dl>
<p> <code>4</code></p>
<dl>
<dt>
<dd> Failed as a file or directory was not found.</dl>
<p> <code>5</code></p>
<dl>
<dt>
<dd> Nothing useful was done.</dl>
<p> <code>6</code></p>
<dl>
<dt>
<dd> The initial setup failed, e.g. setting the network proxy.</dl>
<p> <code>7</code></p>
<dl>
<dt>
<dd> The transaction failed, see the detailed error for more information.</dl>
<h2>SEE ALSO</h2>
<p> pkmon (1). </p>
<p> The programs are documented fully on <a rel="nofollow" href="http://www.packagekit.org.">http://www.packagekit.org.</a></p>
<h2>AUTHOR</h2>
<p> This manual page was written by Richard Hughes &lt;richard [at] hughsie.com&gt;.</p>
<h2>AUTHOR</h2>
<p> <code>Richard Hughes</code></p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2007 &#8211; 2013 Richard Hughes </p>
<h2>Index</h2>
