---
title: "modifyrepo_c(8)"
name: "modifyrepo_c"
section: "8"
letter: "m"
url: "/docs/linux/man/8-modifyrepo_c/"
---

modifyrepo_c - Modify a repomd.xml of rpm-md format repository

<h2>Synopsis</h2>

modifyrepo_c [options] &lt;input metadata&gt; &lt;output repodata&gt; 

 modifyrepo_c --remove &lt;metadata type&gt; &lt;output repodata&gt; 

 modifyrepo_c [options] --batchfile &lt;batch file&gt; &lt;output repodata&gt;

<h2>Options</h2>

<h3>--version</h3>

Show program's version number and exit.

<h3>--mdtype MDTYPE</h3>

Specific datatype of the metadata, will be derived from the filename if not specified.

<h3>--remove</h3>

Remove specified file from repodata.

<h3>--compress</h3>

Compress the new repodata before adding it to the repo. (default)

<h3>--no-compress</h3>

Do not compress the new repodata before adding it to the repo.

<h3>--compress-type COMPRESS_TYPE</h3>

Compression format to use.

<h3>-s --checksum SUMTYPE</h3>

Specify the checksum type to use. (default: sha256)

<h3>--unique-md-filenames</h3>

Include the file's checksum in the filename, helps with proxies. (default)

<h3>--simple-md-filenames</h3>

Do not include the file's checksum in the filename.

<h3>--verbose</h3>

Verbose output.

<h3>-f --batchfile BATCHFILE</h3>

Batch file.

<h3>--new-name NEWFILENAME</h3>

New filename for the file
