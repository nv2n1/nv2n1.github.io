---
title: "createrepo_c(8)"
name: "createrepo_c"
section: "8"
letter: "c"
url: "/docs/linux/man/8-createrepo_c/"
---

createrepo_c - Create rpm-md format (xml-rpm-metadata) repository

<h2>Synopsis</h2>

createrepo_c [options] &lt;directory&gt;

<h2>Options</h2>

<h3>-V --version</h3>

Show program's version number and exit.

<h3>-q --quiet</h3>

Run quietly.

<h3>-v --verbose</h3>

Run verbosely.

<h3>-x --excludes &lt;packages&gt;</h3>

File globs to exclude, can be specified multiple times.

<h3>--basedir &lt;basedir&gt;</h3>

Basedir for path to directories.

<h3>-u --baseurl &lt;URL&gt;</h3>

Optional base URL location for all files.

<h3>-g --groupfile GROUPFILE</h3>

Path to groupfile to include in metadata.

<h3>-s --checksum &lt;checksum_type&gt;</h3>

Choose the checksum type used in repomd.xml and for packages in the metadata. The default is now sha256.

<h3>-p --pretty</h3>

Make sure all xml generated is formatted (default)

<h3>-d --database</h3>

Generate sqlite databases for use with yum.

<h3>--no-database</h3>

Do not generate sqlite databases in the repository.

<h3>--update</h3>

If metadata already exists in the outputdir and an rpm is unchanged (based on file size and mtime) since the metadata was generated, reuse the existing metadata rather than recalculating it. In the case of a large repository with only a few new or modified rpms this can significantly reduce I/O and processing time.

<h3>--update-md-path</h3>

Use the existing repodata for --update from this path.

<h3>--skip-stat</h3>

Skip the stat() call on a --update, assumes if the filename is the same then the file is still the same (only use this if you're fairly trusting or gullible).

<h3>-i --pkglist &lt;filename&gt;</h3>

Specify a text file which contains the complete list of files to include in the repository from the set found in the directory. File format is one package per line, no wildcards or globs.

<h3>-n --includepkg &lt;packages&gt;</h3>

Specify pkgs to include on the command line. Takes urls as well as local paths.

<h3>-o --outputdir &lt;URL&gt;</h3>

Optional output directory.

<h3>-S --skip-symlinks</h3>

Ignore symlinks of packages.

<h3>--changelog-limit &lt;number&gt;</h3>

Only import the last N changelog entries, from each rpm, into the metadata.

<h3>--unique-md-filenames</h3>

Include the file's checksum in the metadata filename, helps HTTP caching (default).

<h3>--simple-md-filenames</h3>

Do not include the file's checksum in the metadata filename.

<h3>--retain-old-md &lt;N&gt;</h3>

Keep around the latest (by timestamp) N copies of the old repodata.

<h3>--distro DISTRO</h3>

Distro tag and optional cpeid: --distro'cpeid,textname'.

<h3>--content CONTENT_TAGS</h3>

Tags for the content in the repository.

<h3>--repo REPO_TAGS</h3>

Tags to describe the repository itself.

<h3>--revision REVISION</h3>

User-specified revision for this repository.

<h3>--read-pkgs-list READ_PKGS_LIST</h3>

Output the paths to the pkgs actually read useful with --update.

<h3>--workers</h3>

Number of workers to spawn to read rpms.

<h3>--xz</h3>

Use xz for repodata compression.

<h3>--compress-type &lt;compress_type&gt;</h3>

Which compression type to use.

<h3>--keep-all-metadata</h3>

Keep groupfile and updateinfo from source repo during update.

<h3>--compatibility</h3>

Enforce maximal compatibility with classical createrepo.

<h3>--retain-old-md-by-age AGE</h3>

During --update, remove all files in repodata/ which are older then the specified period of time. (e.g. '2h', '30d', ...). Available units (m - minutes, h - hours, d - days)

<h3>-c --cachedir CACHEDIR.</h3>

Set path to cache dir

<h3>--deltas</h3>

Tells createrepo to generate deltarpms and the delta metadata.

<h3>--oldpackagedirs PATH</h3>

Paths to look for older pkgs to delta against. Can be specified multiple times.

<h3>--num-deltas INT</h3>

The number of older versions to make deltas against. Defaults to 1.

<h3>--max-delta-rpm-size MAX_DELTA_RPM_SIZE</h3>

Max size of an rpm that to run deltarpm against (in bytes).

<h3>--local-sqlite</h3>

Gen sqlite DBs locally (into a directory for temporary files). Sometimes, sqlite has a trouble to gen DBs on a NFS mount, use this option in such cases. This option could lead to a higher memory consumption if TMPDIR is set to /tmp or not set at all, because then the /tmp is used and /tmp dir is often a ramdisk.

<h3>--cut-dirs NUM</h3>

Ignore NUM of directory components in location_href during repodata generation

<h3>--location-prefix PREFIX</h3>

Append this prefix before location_href in output repodata

<h3>--ignore-lock</h3>

Expert (risky) option: Ignore an existing .repodata/. (Remove the existing .repodata/ and create an empty new one to serve as a lock for other createrepo intances. For the repodata generation, a different temporary dir with the name in format .repodata.time.microseconds.pid/ will be used). NOTE: Use this option on your own risk! If two createrepos run simultaneously, then the state of the generated metadata is not guaranted - it can be inconsistent and wrong.
