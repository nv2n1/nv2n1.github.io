---
title: "django-admin(1)"
name: "django-admin"
section: "1"
letter: "d"
url: "/docs/linux/man/1-django-admin/"
description: "django-admin – Utility script for the Django Web framework"
---

<h2>NAME</h2>
<p> django-admin &#8211; Utility script for the Django Web framework </p>
<p> <code>django-admin</code> is Django&#8217;s command-line utility for administrative tasks. This document outlines all it can do. </p>
<p> Prior to Django 1.7, <code>django-admin</code> was only installed as <code>django-admin.py</code>. </p>
<p> In addition, <code>manage.py</code> is automatically created in each Django project. <code>manage.py</code> is a thin wrapper around <code>django-admin</code> that takes care of several things for you before delegating to <code>django-admin</code>:</p>
<dl>
<dt>&bull;</p>
<dd> It puts your project&#8217;s package on <code>sys.path</code>.</p>
<dt>&bull;</p>
<dd> It sets the <code>DJANGO_SETTINGS_MODULE</code> environment variable so that it points to your project&#8217;s <code>settings.py</code> file.</p>
<dt>&bull;</p>
<dd> It calls <code>django.setup()</code> to initialize various internals of Django. </p>
<p> <code>django.setup()</code> didn&#8217;t exist in previous versions of Django. </p>
<p> The <code>django-admin</code> script should be on your system path if you installed Django via its <code>setup.py</code> utility. If it&#8217;s not on your path, you can find it in <code>site-packages/django/bin</code> within your Python installation. Consider symlinking it from some place on your path, such as <code>/usr/local/bin</code>. </p>
<p> For Windows users, who do not have symlinking functionality available, you can copy <code>django-admin.exe</code> to a location on your existing path or edit the <code>PATH</code> settings (under <code>Settings &#8211; Control Panel &#8211; System &#8211; Advanced &#8211; Environment&#8230;</code>) to point to its installed location. </p>
<p> Generally, when working on a single Django project, it&#8217;s easier to use <code>manage.py</code> than <code>django-admin</code>. If you need to switch between multiple Django settings files, use <code>django-admin</code> with <code>DJANGO_SETTINGS_MODULE</code> or the <i>&#8211;settings</i> command line option. </p>
<p> The command-line examples throughout this document use <code>django-admin</code> to be consistent, but any example can use <code>manage.py</code> just as well.</dl>
<h2>USAGE</h2>
<pre><code>
$ django - admin&lt;command&gt;[options] $ manage.py&lt;command&gt;[options]
</code></pre>
<p> <code>command</code> should be one of the commands listed in this document. <code>options</code>, which is optional, should be zero or more of the options available for the given command.</p>
<h3>Getting runtime help</h3>
<dl>
<dt><code>django-admin help</code></p>
<dd>
<p> Run <code>django-admin help</code> to display usage information and a list of the commands provided by each application. </p>
<p> Run <code>django-admin help &#8211;commands</code> to display a list of all available commands. </p>
<p> Run <code>django-admin help &lt;command&gt;</code> to display a description of the given command and a list of its available options.</dl>
<h3>App names</h3>
<p> Many commands take a list of &quot;app names.&quot; An &quot;app name&quot; is the basename of the package containing your models. For example, if your <code>INSTALLED_APPS</code> contains the string <code>&#8216;mysite.blog&#8217;</code>, the app name is <code>blog</code>.</p>
<h3>Determining the version</h3>
<dl>
<dt><code>django-admin version</code></p>
<dd>
<p> Run <code>django-admin version</code> to display the current Django version. </p>
<p> The output follows the schema described in <i>PEP 386</i>: </p>
<pre>
1.4.dev17026
1.4a1
1.4
</pre>
</dl>
<h3>Displaying debug output</h3>
<p> Use <i>&#8211;verbosity</i> to specify the amount of notification and debug information that <code>django-admin</code> should print to the console. For more details, see the documentation for the <i>&#8211;verbosity</i> option.</p>
<h2>AVAILABLE COMMANDS</h2>
<h3>check &lt;appname appname &#8230;&gt;</h3>
<dl>
<dt><code>django-admin check</code></p>
<dd>
<p> Uses the <code>system check framework</code> to inspect the entire Django project for common problems. </p>
<p> The system check framework will confirm that there aren&#8217;t any problems with your installed models or your admin registrations. It will also provide warnings of common compatibility problems introduced by upgrading Django to a new version. Custom checks may be introduced by other libraries and applications. </p>
<p> By default, all apps will be checked. You can check a subset of apps by providing a list of app labels as arguments: </p>
<pre>
python manage.py check auth admin myapp
</pre>
<p> If you do not specify any app, all apps will be checked.</p>
<dt><code>&#8211;tag &lt;tagname&gt;</code></p>
<dd>
<p> The <code>system check framework</code> performs many different types of checks. These check types are categorized with tags. You can use these tags to restrict the checks performed to just those in a particular category. For example, to perform only security and compatibility checks, you would run: </p>
<pre>
python manage.py check --tag security --tag compatibility
</pre>
<dt><code>&#8211;list-tags</code></p>
<dd>
<p> List all available tags.</p>
<dt><code>&#8211;deploy</code></p>
<dd>
<p> The <code>&#8211;deploy</code> option activates some additional checks that are only relevant in a deployment setting. </p>
<p> You can use this option in your local development environment, but since your local development settings module may not have many of your production settings, you will probably want to point the <code>check</code> command at a different settings module, either by setting the <code>DJANGO_SETTINGS_MODULE</code> environment variable, or by passing the <code>&#8211;settings</code> option: </p>
<pre>
python manage.py check --deploy --settings=production_settings
</pre>
<p> Or you could run it directly on a production or staging deployment to verify that the correct settings are in use (omitting <code>&#8211;settings</code>). You could even make it part of your integration test suite.</dl>
<h3>compilemessages</h3>
<dl>
<dt><code>django-admin compilemessages</code></p>
<dd>
<p> Compiles .po files created by <i>makemessages</i> to .mo files for use with the builtin gettext support. See <code>/topics/i18n/index</code>. </p>
<p> Use the <i>&#8211;locale</i> option (or its shorter version <code>-l</code>) to specify the locale(s) to process. If not provided, all locales are processed. </p>
<p> Use the <i>&#8211;exclude</i> option (or its shorter version <code>-x</code>) to specify the locale(s) to exclude from processing. If not provided, no locales are excluded. </p>
<p> You can pass <code>&#8211;use-fuzzy</code> option (or <code>-f</code>) to include fuzzy translations into compiled files. </p>
<p> Added <code>&#8211;exclude</code> and <code>&#8211;use-fuzzy</code> options. </p>
<p> Example usage: </p>
<p>django &#8211; admin compilemessages&#8211; locale = pt_BR<br />
                                              django &#8211;<br />
                                          admin compilemessages&#8211; locale = pt_BR&#8211; locale = fr &#8211; f django &#8211; admin compilemessages &#8211; l pt_BR django &#8211; admin compilemessages &#8211; l pt_BR &#8211; l fr&#8211; use &#8211; fuzzy django &#8211; admin compilemessages&#8211; exclude = pt_BR<br />
                                                                                                                                                                                                                                                         django &#8211;<br />
                                                                                                                                                                                                                                                     admin compilemessages&#8211; exclude = pt_BR&#8211; exclude = fr<br />
                                                                                                                                                                                                                                                                                                             django &#8211;<br />
                                                                                                                                                                                                                                                                                                         admin compilemessages &#8211; x pt_BR django &#8211; admin compilemessages &#8211; x pt_BR &#8211; x fr
</dl>
<h3>createcachetable</h3>
<dl>
<dt><code>django-admin createcachetable</code></p>
<dd>
<p> Creates the cache tables for use with the database cache backend. See <code>/topics/cache</code> for more information. </p>
<p> The <i>&#8211;database</i> option can be used to specify the database onto which the cachetable will be installed. </p>
<p> It is no longer necessary to provide the cache table name or the <i>&#8211;database</i> option. Django takes this information from your settings file. If you have configured multiple caches or multiple databases, all cache tables are created. </p>
</dl>
<h3>dbshell</h3>
<dl>
<dt><code>django-admin dbshell</code></p>
<dd>
<p> Runs the command-line client for the database engine specified in your <code>ENGINE</code> setting, with the connection parameters specified in your <code>USER</code>, <code>PASSWORD</code>, etc., settings.</p>
<dt>&bull;</p>
<dd> For PostgreSQL, this runs the <code>psql</code> command-line client.</p>
<dt>&bull;</p>
<dd> For MySQL, this runs the <code>mysql</code> command-line client.</p>
<dt>&bull;</p>
<dd> For SQLite, this runs the <code>sqlite3</code> command-line client. </p>
<p> This command assumes the programs are on your <code>PATH</code> so that a simple call to the program name (<code>psql</code>, <code>mysql</code>, <code>sqlite3</code>) will find the program in the right place. There&#8217;s no way to specify the location of the program manually. </p>
<p> The <i>&#8211;database</i> option can be used to specify the database onto which to open a shell.</dl>
<h3>diffsettings</h3>
<dl>
<dt><code>django-admin diffsettings</code></p>
<dd>
<p> Displays differences between the current settings file and Django&#8217;s default settings. </p>
<p> Settings that don&#8217;t appear in the defaults are followed by <code>&quot;###&quot;</code>. For example, the default settings don&#8217;t define <code>ROOT_URLCONF</code>, so <code>ROOT_URLCONF</code> is followed by <code>&quot;###&quot;</code> in the output of <code>diffsettings</code>. </p>
<p> The <i>&#8211;all</i> option may be provided to display all settings, even if they have Django&#8217;s default value. Such settings are prefixed by <code>&quot;###&quot;</code>.</dl>
<h3>dumpdata &lt;app_label app_label app_label.Model &#8230;&gt;</h3>
<dl>
<dt><code>django-admin dumpdata</code></p>
<dd>
<p> Outputs to standard output all data in the database associated with the named application(s). </p>
<p> If no application name is provided, all installed applications will be dumped. </p>
<p> The output of <code>dumpdata</code> can be used as input for <i>loaddata</i>. </p>
<p> Note that <code>dumpdata</code> uses the default manager on the model for selecting the records to dump. If you&#8217;re using a <i>custom manager</i> as the default manager and it filters some of the available records, not all of the objects will be dumped. </p>
<p> The <i>&#8211;all</i> option may be provided to specify that <code>dumpdata</code> should use Django&#8217;s base manager, dumping records which might otherwise be filtered or modified by a custom manager.</p>
<dt><code>&#8211;format &lt;fmt&gt;</code></p>
<dd>
<p> By default, <code>dumpdata</code> will format its output in JSON, but you can use the <code>&#8211;format</code> option to specify another format. Currently supported formats are listed in <i>serialization-formats</i>.</p>
<dt><code>&#8211;indent &lt;num&gt;</code></p>
<dd>
<p> By default, <code>dumpdata</code> will output all data on a single line. This isn&#8217;t easy for humans to read, so you can use the <code>&#8211;indent</code> option to pretty-print the output with a number of indentation spaces. </p>
<p> The <i>&#8211;exclude</i> option may be provided to prevent specific applications or models (specified as in the form of <code>app_label.ModelName</code>) from being dumped. If you specify a model name to <code>dumpdata</code>, the dumped output will be restricted to that model, rather than the entire application. You can also mix application names and model names. </p>
<p> The <i>&#8211;database</i> option can be used to specify the database from which data will be dumped.</p>
<dt><code>&#8211;natural-foreign</code></p>
<dd>
<p> When this option is specified, Django will use the <code>natural_key()</code> model method to serialize any foreign key and many-to-many relationship to objects of the type that defines the method. If you are dumping <code>contrib.auth</code> <code>Permission</code> objects or <code>contrib.contenttypes</code> <code>ContentType</code> objects, you should probably be using this flag. See the <i>natural keys</i> documentation for more details on this and the next option.</p>
<dt><code>&#8211;natural-primary</code></p>
<dd>
<p> When this option is specified, Django will not provide the primary key in the serialized data of this object since it can be calculated during deserialization.</p>
<dt><code>&#8211;natural</code></p>
<dd>
<p> Deprecated since version 1.7: Equivalent to the <i>&#8211;natural-foreign</i> option; use that instead. </p>
<p> Use <i>natural keys</i> to represent any foreign key and many-to-many relationship with a model that provides a natural key definition.</p>
<dt><code>&#8211;pks</code></p>
<dd>
<p> By default, <code>dumpdata</code> will output all the records of the model, but you can use the <code>&#8211;pks</code> option to specify a comma separated list of primary keys on which to filter. This is only available when dumping one model.</p>
<dt><code>&#8211;output</code></p>
<dd>
<p> By default <code>dumpdata</code> will output all the serialized data to standard output. This options allows to specify the file to which the data is to be written.</dl>
<h3>flush</h3>
<dl>
<dt><code>django-admin flush</code></p>
<dd>
<p> Removes all data from the database, re-executes any post-synchronization handlers, and reinstalls any initial data fixtures. </p>
<p> The <i>&#8211;noinput</i> option may be provided to suppress all user prompts. </p>
<p> The <i>&#8211;database</i> option may be used to specify the database to flush.</dl>
<h3><code>&#8211;no-initial-data</code></h3>
<p> Use <code>&#8211;no-initial-data</code> to avoid loading the initial_data fixture.</p>
<h3>inspectdb</h3>
<dl>
<dt><code>django-admin inspectdb</code></p>
<dd>
<p> Introspects the database tables and views in the database pointed-to by the <code>NAME</code> setting and outputs a Django model module (a <code>models.py</code> file) to standard output. </p>
<p> Use this if you have a legacy database with which you&#8217;d like to use Django. The script will inspect the database and create a model for each table or view within it. </p>
<p> As you might expect, the created models will have an attribute for every field in the table or view. Note that <code>inspectdb</code> has a few special cases in its field-name output:</p>
<dt>&bull;</p>
<dd> If <code>inspectdb</code> cannot map a column&#8217;s type to a model field type, it&#8217;ll use <code>TextField</code> and will insert the Python comment <code>&#8216;This field type is a guess.&#8217;</code> next to the field in the generated model.</p>
<dt>&bull;</p>
<dd> If the database column name is a Python reserved word (such as <code>&#8216;pass&#8217;</code>, <code>&#8216;class&#8217;</code> or <code>&#8216;for&#8217;</code>), <code>inspectdb</code> will append <code>&#8216;_field&#8217;</code> to the attribute name. For example, if a table has a column <code>&#8216;for&#8217;</code>, the generated model will have a field <code>&#8216;for_field&#8217;</code>, with the <code>db_column</code> attribute set to <code>&#8216;for&#8217;</code>. <code>inspectdb</code> will insert the Python comment <code>&#8216;Field renamed because it was a Python reserved word.&#8217;</code> next to the field. </p>
<p> This feature is meant as a shortcut, not as definitive model generation. After you run it, you&#8217;ll want to look over the generated models yourself to make customizations. In particular, you&#8217;ll need to rearrange models&#8217; order, so that models that refer to other models are ordered properly. </p>
<p> Primary keys are automatically introspected for PostgreSQL, MySQL and SQLite, in which case Django puts in the <code>primary_key=True</code> where needed. </p>
<p> <code>inspectdb</code> works with PostgreSQL, MySQL and SQLite. Foreign-key detection only works in PostgreSQL and with certain types of MySQL tables. </p>
<p> Django doesn&#8217;t create database defaults when a <code>default</code> is specified on a model field. Similarly, database defaults aren&#8217;t translated to model field defaults or detected in any fashion by <code>inspectdb</code>. </p>
<p> By default, <code>inspectdb</code> creates unmanaged models. That is, <code>managed = False</code> in the model&#8217;s <code>Meta</code> class tells Django not to manage each table&#8217;s creation, modification, and deletion. If you do want to allow Django to manage the table&#8217;s lifecycle, you&#8217;ll need to change the <code>managed</code> option to <code>True</code> (or simply remove it because <code>True</code> is its default value). </p>
<p> The <i>&#8211;database</i> option may be used to specify the database to introspect. </p>
<p> A feature to inspect database views was added. In previous versions, only tables (not views) were inspected. </p>
</dl>
<h3>loaddata &lt;fixture fixture &#8230;&gt;</h3>
<dl>
<dt><code>django-admin loaddata</code></p>
<dd>
<p> Searches for and loads the contents of the named fixture into the database. </p>
<p> The <i>&#8211;database</i> option can be used to specify the database onto which the data will be loaded.</p>
<dt><code>&#8211;ignorenonexistent</code></p>
<dd>
<p> The <i>&#8211;ignorenonexistent</i> option can be used to ignore fields and models that may have been removed since the fixture was originally generated.</p>
<dt><code>&#8211;app</code></p>
<dd>
<p> The <i>&#8211;app</i> option can be used to specify a single app to look for fixtures in rather than looking through all apps. </p>
<p> <code>&#8211;app</code> was added. </p>
<p> <code>&#8211;ignorenonexistent</code> also ignores non-existent models. </p>
</dl>
<h3>What&#8217;s a fixture?</h3>
<p> A <i>fixture</i> is a collection of files that contain the serialized contents of the database. Each fixture has a unique name, and the files that comprise the fixture can be distributed over multiple directories, in multiple applications. </p>
<p> Django will search in three locations for fixtures:</p>
<dl>
<dt>1.</p>
<dd> In the <code>fixtures</code> directory of every installed application</p>
<dt>2.</p>
<dd> In any directory named in the <code>FIXTURE_DIRS</code> setting</p>
<dt>3.</p>
<dd> In the literal path named by the fixture </p>
<p> Django will load any and all fixtures it finds in these locations that match the provided fixture names. </p>
<p> If the named fixture has a file extension, only fixtures of that type will be loaded. For example: </p>
<pre>
django-admin loaddata mydata.json
</pre>
<p> would only load JSON fixtures called <code>mydata</code>. The fixture extension must correspond to the registered name of a <i>serializer</i> (e.g., <code>json</code> or <code>xml</code>). </p>
<p> If you omit the extensions, Django will search all available fixture types for a matching fixture. For example: </p>
<pre>
django-admin loaddata mydata
</pre>
<p> would look for any fixture of any fixture type called <code>mydata</code>. If a fixture directory contained <code>mydata.json</code>, that fixture would be loaded as a JSON fixture. </p>
<p> The fixtures that are named can include directory components. These directories will be included in the search path. For example: </p>
<pre>
django-admin loaddata foo/bar/mydata.json
</pre>
<p> would search <code>&lt;app_label&gt;/fixtures/foo/bar/mydata.json</code> for each installed application, <code>&lt;dirname&gt;/foo/bar/mydata.json</code> for each directory in <code>FIXTURE_DIRS</code>, and the literal path <code>foo/bar/mydata.json</code>. </p>
<p> When fixture files are processed, the data is saved to the database as is. Model defined <code>save()</code> methods are not called, and any <code>pre_save</code> or <code>post_save</code> signals will be called with <code>raw=True</code> since the instance only contains attributes that are local to the model. You may, for example, want to disable handlers that access related fields that aren&#8217;t present during fixture loading and would otherwise raise an exception: </p>
<p>from django.db.models.signals import post_save<br />
    from.models import MyModel<br />
        def my_handler(**kwargs)<br />
    :<br />
#disable the handler during fixture loading<br />
      if kwargs[&#8216;raw&#8217;] : return &#8230; post_save.connect(my_handler, sender = MyModel)</p>
<p> You could also write a simple decorator to encapsulate this logic: </p>
<p>from functools import wraps<br />
    def<br />
    disable_for_loaddata(signal_handler)<br />
    : &#8220;&#8221;<br />
      &#8221;<br />
      Decorator that turns off signal handlers when loading fixture data.&#8221;&#8221;<br />
                                                                         &#8221;<br />
      @wraps(signal_handler)<br />
          def wrapper(*args, **kwargs)<br />
    : if kwargs[&#8216;raw&#8217;] : return signal_handler(*args, **kwargs) return wrapper<br />
                         @disable_for_loaddata def my_handler(**kwargs)<br />
    : &#8230;</p>
<p> Just be aware that this logic will disable the signals whenever fixtures are deserialized, not just during <code>loaddata</code>. </p>
<p> Note that the order in which fixture files are processed is undefined. However, all fixture data is installed as a single transaction, so data in one fixture can reference data in another fixture. If the database backend supports row-level constraints, these constraints will be checked at the end of the transaction. </p>
<p> The <i>dumpdata</i> command can be used to generate input for <code>loaddata</code>.</dl>
<h3>Compressed fixtures</h3>
<p> Fixtures may be compressed in <code>zip</code>, <code>gz</code>, or <code>bz2</code> format. For example: </p>
<pre>
django-admin loaddata mydata.json
</pre>
<p> would look for any of <code>mydata.json</code>, <code>mydata.json.zip</code>, <code>mydata.json.gz</code>, or <code>mydata.json.bz2</code>. The first file contained within a zip-compressed archive is used. </p>
<p> Note that if two fixtures with the same name but different fixture type are discovered (for example, if <code>mydata.json</code> and <code>mydata.xml.gz</code> were found in the same fixture directory), fixture installation will be aborted, and any data installed in the call to <code>loaddata</code> will be removed from the database.</p>
<dl>
<dt>MySQL with MyISAM and fixtures</p>
<dd>
<p> The MyISAM storage engine of MySQL doesn&#8217;t support transactions or constraints, so if you use MyISAM, you won&#8217;t get validation of fixture data, or a rollback if multiple transaction files are found.</dl>
<h3>Database-specific fixtures</h3>
<p> If you&#8217;re in a multi-database setup, you might have fixture data that you want to load onto one database, but not onto another. In this situation, you can add database identifier into the names of your fixtures. </p>
<p> For example, if your <code>DATABASES</code> setting has a &#8216;master&#8217; database defined, name the fixture <code>mydata.master.json</code> or <code>mydata.master.json.gz</code> and the fixture will only be loaded when you specify you want to load data into the <code>master</code> database.</p>
<h3>makemessages</h3>
<dl>
<dt><code>django-admin makemessages</code></p>
<dd>
<p> Runs over the entire source tree of the current directory and pulls out all strings marked for translation. It creates (or updates) a message file in the conf/locale (in the Django tree) or locale (for project and application) directory. After making changes to the messages files you need to compile them with <i>compilemessages</i> for use with the builtin gettext support. See the <i>i18n documentation</i> for details.</p>
<dt><code>&#8211;all</code></p>
<dd>
<p> Use the <code>&#8211;all</code> or <code>-a</code> option to update the message files for all available languages. </p>
<p> Example usage: </p>
<pre>
django-admin makemessages --all
</pre>
<dt><code>&#8211;extension</code></p>
<dd>
<p> Use the <code>&#8211;extension</code> or <code>-e</code> option to specify a list of file extensions to examine (default: &quot;.html&quot;, &quot;.txt&quot;). </p>
<p> Example usage: </p>
<pre>
django-admin makemessages --locale=de --extension xhtml
</pre>
<p> Separate multiple extensions with commas or use -e or &#8211;extension multiple times: </p>
<pre>
django-admin makemessages --locale=de --extension=html,txt --extension xml
</pre>
<p> Use the <i>&#8211;locale</i> option (or its shorter version <code>-l</code>) to specify the locale(s) to process. </p>
<p> Use the <i>&#8211;exclude</i> option (or its shorter version <code>-x</code>) to specify the locale(s) to exclude from processing. If not provided, no locales are excluded. </p>
<p> Example usage: </p>
<pre><code>
django - admin makemessages-- locale = pt_BR
                                           django -
                                       admin makemessages-- locale = pt_BR-- locale = fr
                                                                                          django -
                                                                                      admin makemessages - l pt_BR django - admin makemessages - l pt_BR - l fr django - admin makemessages-- exclude = pt_BR
                                                                                                                                                                                                            django -
                                                                                                                                                                                                        admin makemessages-- exclude = pt_BR-- exclude = fr
                                                                                                                                                                                                                                                             django -
                                                                                                                                                                                                                                                         admin makemessages - x pt_BR django - admin makemessages - x pt_BR - x fr
</code></pre>
<p> Added the <code>&#8211;previous</code> option to the <code>msgmerge</code> command when merging with existing po files. </p>
<dt><code>&#8211;domain</code></p>
<dd>
<p> Use the <code>&#8211;domain</code> or <code>-d</code> option to change the domain of the messages files. Currently supported:</p>
<dt>&bull;</p>
<dd> <code>django</code> for all <code>*.py</code>, <code>*.html</code> and <code>*.txt</code> files (default)</p>
<dt>&bull;</p>
<dd> <code>djangojs</code> for <code>*.js</code> files</p>
<dt><code>&#8211;symlinks</code></p>
<dd>
<p> Use the <code>&#8211;symlinks</code> or <code>-s</code> option to follow symlinks to directories when looking for new translation strings. </p>
<p> Example usage: </p>
<pre>
django-admin makemessages --locale=de --symlinks
</pre>
<dt><code>&#8211;ignore</code></p>
<dd>
<p> Use the <code>&#8211;ignore</code> or <code>-i</code> option to ignore files or directories matching the given <i>glob</i>-style pattern. Use multiple times to ignore more. </p>
<p> These patterns are used by default: <code>&#8216;CVS&#8217;</code>, <code>&#8216;.*&#8217;</code>, <code>&#8216;*~&#8217;</code>, <code>&#8216;*.pyc&#8217;</code> </p>
<p> Example usage: </p>
<pre>
django-admin makemessages --locale=en_US --ignore=apps/* --ignore=secret/*.html
</pre>
<dt><code>&#8211;no-default-ignore</code></p>
<dd>
<p> Use the <code>&#8211;no-default-ignore</code> option to disable the default values of <i>&#8211;ignore</i>.</p>
<dt><code>&#8211;no-wrap</code></p>
<dd>
<p> Use the <code>&#8211;no-wrap</code> option to disable breaking long message lines into several lines in language files.</p>
<dt><code>&#8211;no-location</code></p>
<dd>
<p> Use the <code>&#8211;no-location</code> option to not write &#8216;<code>#: filename:line</code>’ comment lines in language files. Note that using this option makes it harder for technically skilled translators to understand each message&#8217;s context.</p>
<dt><code>&#8211;keep-pot</code></p>
<dd>
<p> Use the <code>&#8211;keep-pot</code> option to prevent Django from deleting the temporary debugging errors which may prevent the final language files from being created. </p>
<p> <code>SEE ALSO:</code> See <i>customizing-makemessages</i> for instructions on how to customize the keywords that <i>makemessages</i> passes to <code>xgettext</code>.</dl>
<h3>makemigrations [&lt;app_label&gt;]</h3>
<dl>
<dt><code>django-admin makemigrations</code></p>
<dd>
<p> Creates new migrations based on the changes detected to your models. Migrations, their relationship with apps and more are covered in depth in <code>the migrations documentation</code>. </p>
<p> Providing one or more app names as arguments will limit the migrations created to the app(s) specified and any dependencies needed (the table at the other end of a <code>ForeignKey</code>, for example).</p>
<dt><code>&#8211;empty</code></p>
<dd>
<p> The <code>&#8211;empty</code> option will cause <code>makemigrations</code> to output an empty migration for the specified apps, for manual editing. This option is only for advanced users and should not be used unless you are familiar with the migration format, migration operations, and the dependencies between your migrations.</p>
<dt><code>&#8211;dry-run</code></p>
<dd>
<p> The <code>&#8211;dry-run</code> option shows what migrations would be made without actually writing any migrations files to disk. Using this option along with <code>&#8211;verbosity 3</code> will also show the complete migrations files that would be written.</p>
<dt><code>&#8211;merge</code></p>
<dd>
<p> The <code>&#8211;merge</code> option enables fixing of migration conflicts. The <i>&#8211;noinput</i> option may be provided to suppress user prompts during a merge.</p>
<dt><code>&#8211;name, -n</code></p>
<dd>
<p> The <code>&#8211;name</code> option allows you to give the migration(s) a custom name instead of a generated one.</p>
<dt><code>&#8211;exit, -e</code></p>
<dd>
<p> The <code>&#8211;exit</code> option will cause <code>makemigrations</code> to exit with error code 1 when no migration are created (or would have been created, if combined with <code>&#8211;dry-run</code>).</dl>
<h3>migrate [&lt;app_label&gt; [&lt;migrationname&gt;]]</h3>
<dl>
<dt><code>django-admin migrate</code></p>
<dd>
<p> Synchronizes the database state with the current set of models and migrations. Migrations, their relationship with apps and more are covered in depth in <code>the migrations documentation</code>. </p>
<p> The behavior of this command changes depending on the arguments provided:</p>
<dt>&bull;</p>
<dd> No arguments: All migrated apps have all of their migrations run, and all unmigrated apps are synchronized with the database,</p>
<dt>&bull;</p>
<dd> <code>&lt;app_label&gt;</code>: The specified app has its migrations run, up to the most recent migration. This may involve running other apps&#8217; migrations too, due to dependencies.</p>
<dt>&bull;</p>
<dd> <code>&lt;app_label&gt; &lt;migrationname&gt;</code>: Brings the database schema to a state where the named migration is applied, but no later migrations in the same app are applied. This may involve unapplying migrations if you have previously migrated past the named migration. Use the name <code>zero</code> to unapply all migrations for an app. </p>
<p> Unlike <code>syncdb</code>, this command does not prompt you to create a superuser if one doesn&#8217;t exist (assuming you are using <code>django.contrib.auth</code>). Use <i>createsuperuser</i> to do that if you wish. </p>
<p> The <i>&#8211;database</i> option can be used to specify the database to migrate.</p>
<dt><code>&#8211;fake</code></p>
<dd>
<p> The <code>&#8211;fake</code> option tells Django to mark the migrations as having been applied or unapplied, but without actually running the SQL to change your database schema. </p>
<p> This is intended for advanced users to manipulate the current migration state directly if they&#8217;re manually applying changes; be warned that using <code>&#8211;fake</code> runs the risk of putting the migration state table into a state where manual recovery will be needed to make migrations run correctly. </p>
<dt><code>&#8211;fake-initial</code></p>
<dd>
<p> The <code>&#8211;fake-initial</code> option can be used to allow Django to skip an app&#8217;s initial migration if all database tables with the names of all models created by all <code>CreateModel</code> operations in that migration already exist. This option is intended for use when first running migrations against a database that preexisted the use of migrations. This option does not, however, check for matching database schema beyond matching table names and so is only safe to use if you are confident that your existing schema matches what is recorded in your initial migration. </p>
<p> Deprecated since version 1.8: The <code>&#8211;list</code> option has been moved to the <i>showmigrations</i> command. </p>
</dl>
<h3>runfcgi [options]</h3>
<dl>
<dt><code>django-admin runfcgi</code></p>
<dd>
<p> Deprecated since version 1.7: FastCGI support is deprecated and will be removed in Django 1.9. </p>
<p> Starts a set of FastCGI processes suitable for use with any Web server that supports the FastCGI protocol. See the <code>FastCGI deployment documentation</code> for details. Requires the Python FastCGI module from <i>flup</i>. </p>
<p> Internally, this wraps the WSGI application object specified by the <code>WSGI_APPLICATION</code> setting. </p>
<p> The options accepted by this command are passed to the FastCGI library and don&#8217;t use the <code>&#8216;&#8211;&#8216;</code> prefix as is usual for other Django management commands.</p>
<dt><code>protocol</code></p>
<dd>
<p> <code>protocol=PROTOCOL</code> </p>
<p> Protocol to use. <i>PROTOCOL</i> can be <code>fcgi</code>, <code>scgi</code>, <code>ajp</code>, etc. (default is <code>fcgi</code>)</p>
<dt><code>host</code></p>
<dd>
<p> <code>host=HOSTNAME</code> </p>
<p> Hostname to listen on.</p>
<dt><code>port</code></p>
<dd>
<p> <code>port=PORTNUM</code> </p>
<p> Port to listen on.</p>
<dt><code>socket</code></p>
<dd>
<p> <code>socket=FILE</code> </p>
<p> UNIX socket to listen on.</p>
<dt><code>method</code></p>
<dd>
<p> <code>method=IMPL</code> </p>
<p> Possible values: <code>prefork</code> or <code>threaded</code> (default <code>prefork</code>)</p>
<dt><code>maxrequests</code></p>
<dd>
<p> <code>maxrequests=NUMBER</code> </p>
<p> Number of requests a child handles before it is killed and a new child is forked (0 means no limit).</p>
<dt><code>maxspare</code></p>
<dd>
<p> <code>maxspare=NUMBER</code> </p>
<p> Max number of spare processes / threads.</p>
<dt><code>minspare</code></p>
<dd>
<p> <code>minspare=NUMBER</code> </p>
<p> Min number of spare processes / threads.</p>
<dt><code>maxchildren</code></p>
<dd>
<p> <code>maxchildren=NUMBER</code> </p>
<p> Hard limit number of processes / threads.</p>
<dt><code>daemonize</code></p>
<dd>
<p> <code>daemonize=BOOL</code> </p>
<p> Whether to detach from terminal.</p>
<dt><code>pidfile</code></p>
<dd>
<p> <code>pidfile=FILE</code> </p>
<p> Write the spawned process-id to file <i>FILE</i>.</p>
<dt><code>workdir</code></p>
<dd>
<p> <code>workdir=DIRECTORY</code> </p>
<p> Change to directory <i>DIRECTORY</i> when daemonizing.</p>
<dt><code>debug</code></p>
<dd>
<p> <code>debug=BOOL</code> </p>
<p> Set to true to enable flup tracebacks.</p>
<dt><code>outlog</code></p>
<dd>
<p> <code>outlog=FILE</code> </p>
<p> Write stdout to the <i>FILE</i> file.</p>
<dt><code>errlog</code></p>
<dd>
<p> <code>errlog=FILE</code> </p>
<p> Write stderr to the <i>FILE</i> file.</p>
<dt><code>umask</code></p>
<dd>
<p> <code>umask=UMASK</code> </p>
<p> Umask to use when daemonizing. The value is interpreted as an octal number (default value is <code>0o22</code>). </p>
<p> Example usage: </p>
<pre>
django-admin runfcgi socket=/tmp/fcgi.sock method=prefork daemonize=true \
    pidfile=/var/run/django-fcgi.pid
</pre>
<p> Run a FastCGI server as a daemon and write the spawned PID in a file.</dl>
<h3>runserver [port or address:port]</h3>
<dl>
<dt><code>django-admin runserver</code></p>
<dd>
<p> Starts a lightweight development Web server on the local machine. By default, the server runs on port 8000 on the IP address <code>127.0.0.1</code>. You can pass in an IP address and port number explicitly. </p>
<p> If you run this script as a user with normal privileges (recommended), you might not have access to start a port on a low port number. Low port numbers are reserved for the superuser (root). </p>
<p> This server uses the WSGI application object specified by the <code>WSGI_APPLICATION</code> setting. </p>
<p> DO NOT USE THIS SERVER IN A PRODUCTION SETTING. It has not gone through security audits or performance tests. (And that&#8217;s how it&#8217;s gonna stay. We&#8217;re in the business of making Web frameworks, not Web servers, so improving this server to be able to handle a production environment is outside the scope of Django.) </p>
<p> The development server automatically reloads Python code for each request, as needed. You don&#8217;t need to restart the server for code changes to take effect. However, some actions like adding files don&#8217;t trigger a restart, so you&#8217;ll have to restart the server in these cases. </p>
<p> Compiling translation files now also restarts the development server. </p>
<p> If you are using Linux and install <i>pyinotify</i>, kernel signals will be used to autoreload the server (rather than polling file modification timestamps each second). This offers better scaling to large projects, reduction in response time to code modification, more robust change detection, and battery usage reduction. </p>
<p> <code>pyinotify</code> support was added. </p>
<p> When you start the server, and each time you change Python code while the server is running, the server will check your entire Django project for errors (see the <i>check</i> command). If any errors are found, they will be printed to standard output, but it won&#8217;t stop the server. </p>
<p> You can run as many servers as you want, as long as they&#8217;re on separate ports. Just execute <code>django-admin runserver</code> more than once. </p>
<p> Note that the default IP address, <code>127.0.0.1</code>, is not accessible from other machines on your network. To make your development server viewable to other machines on the network, use its own IP address (e.g. <code>192.168.2.1</code>) or <code>0.0.0.0</code> or <code>::</code> (with IPv6 enabled). </p>
<p> You can provide an IPv6 address surrounded by brackets (e.g. <code>[200a::1]:8000</code>). This will automatically enable IPv6 support. </p>
<p> A hostname containing ASCII-only characters can also be used. </p>
<p> If the <code>staticfiles</code> contrib app is enabled (default in new projects) the <i>runserver</i> command will be overridden with its own <i>runserver</i> command. </p>
<p> If <i>migrate</i> was not previously executed, the table that stores the history of migrations is created at first run of <code>runserver</code>.</p>
<dt><code>&#8211;noreload</code></p>
<dd>
<p> Use the <code>&#8211;noreload</code> option to disable the use of the auto-reloader. This means any Python code changes you make while the server is running will <i>not</i> take effect if the particular Python modules have already been loaded into memory. </p>
<p> Example usage: </p>
<pre>
django-admin runserver --noreload
</pre>
<dt><code>&#8211;nothreading</code></p>
<dd>
<p> The development server is multithreaded by default. Use the <code>&#8211;nothreading</code> option to disable the use of threading in the development server.</p>
<dt><code>&#8211;ipv6, -6</code></p>
<dd>
<p> Use the <code>&#8211;ipv6</code> (or shorter <code>-6</code>) option to tell Django to use IPv6 for the development server. This changes the default IP address from <code>127.0.0.1</code> to <code>::1</code>. </p>
<p> Example usage: </p>
<pre>
django-admin runserver --ipv6
</pre>
</dl>
<h3>Examples of using different ports and addresses</h3>
<p> Port 8000 on IP address <code>127.0.0.1</code>: </p>
<pre>
django-admin runserver
</pre>
<p> Port 8000 on IP address <code>1.2.3.4</code>: </p>
<pre>
django-admin runserver 1.2.3.4:8000
</pre>
<p> Port 7000 on IP address <code>127.0.0.1</code>: </p>
<pre>
django-admin runserver 7000
</pre>
<p> Port 7000 on IP address <code>1.2.3.4</code>: </p>
<pre>
django-admin runserver 1.2.3.4:7000
</pre>
<p> Port 8000 on IPv6 address <code>::1</code>: </p>
<pre>
django-admin runserver -6
</pre>
<p> Port 7000 on IPv6 address <code>::1</code>: </p>
<pre>
django-admin runserver -6 7000
</pre>
<p> Port 7000 on IPv6 address <code>2001:0db8:1234:5678::9</code>: </p>
<pre>
django-admin runserver [2001:0db8:1234:5678::9]:7000
</pre>
<p> Port 8000 on IPv4 address of host <code>localhost</code>: </p>
<pre>
django-admin runserver localhost:8000
</pre>
<p> Port 8000 on IPv6 address of host <code>localhost</code>: </p>
<pre>
django-admin runserver -6 localhost:8000
</pre>
<h3>Serving static files with the development server</h3>
<p> By default, the development server doesn&#8217;t serve any static files for your site (such as CSS files, images, things under <code>MEDIA_URL</code> and so forth). If you want to configure Django to serve static media, read <code>/howto/static-files/index</code>.</p>
<h3>shell</h3>
<dl>
<dt><code>django-admin shell</code></p>
<dd>
<p> Starts the Python interactive interpreter. </p>
<p> Django will use <i>IPython</i> or <i>bpython</i> if either is installed. If you have a rich shell installed but want to force use of the &quot;plain&quot; Python interpreter, use the <code>&#8211;plain</code> option, like so: </p>
<pre>
django-admin shell --plain
</pre>
<p> If you would like to specify either IPython or bpython as your interpreter if you have both installed you can specify an alternative interpreter interface with the <code>-i</code> or <code>&#8211;interface</code> options like so: </p>
<p> IPython: </p>
<pre>
django-admin shell -i ipython
django-admin shell --interface ipython
</pre>
<p> bpython: </p>
<pre>
django-admin shell -i bpython
django-admin shell --interface bpython
</pre>
<p> When the &quot;plain&quot; Python interactive interpreter starts (be it because <code>&#8211;plain</code> was specified or because no other interactive interface is available) it reads the script pointed to by the <i>PYTHONSTARTUP</i> environment variable and the <code>~/.pythonrc.py</code> script. If you don&#8217;t wish this behavior you can use the <code>&#8211;no-startup</code> option. e.g.: </p>
<pre>
django-admin shell --plain --no-startup
</pre>
</dl>
<h3>showmigrations [&lt;app_label&gt; [&lt;app_label&gt;]]</h3>
<dl>
<dt><code>django-admin showmigrations</code></p>
<dd>
<p> Shows all migrations in a project.</p>
<dt><code>&#8211;list, -l</code></p>
<dd>
<p> The <code>&#8211;list</code> option lists all of the apps Django knows about, the migrations available for each app, and whether or not each migrations is applied (marked by an <code>[X]</code> next to the migration name). </p>
<p> Apps without migrations are also listed, but have <code>(no migrations)</code> printed under them.</p>
<dt><code>&#8211;plan, -p</code></p>
<dd>
<p> The <code>&#8211;plan</code> option shows the migration plan Django will follow to apply migrations. Any supplied app labels are ignored because the plan might go beyond those apps. Same as <code>&#8211;list</code>, applied migrations are marked by an <code>[X]</code>. For a verbosity of 2 and above, all dependencies of a migration will also be shown.</dl>
<h3>sql &lt;app_label app_label &#8230;&gt;</h3>
<dl>
<dt><code>django-admin sql</code></p>
<dd>
<p> Prints the CREATE TABLE SQL statements for the given app name(s). </p>
<p> The <i>&#8211;database</i> option can be used to specify the database for which to print the SQL.</dl>
<h3>sqlall &lt;app_label app_label &#8230;&gt;</h3>
<dl>
<dt><code>django-admin sqlall</code></p>
<dd>
<p> Prints the CREATE TABLE and initial-data SQL statements for the given app name(s). </p>
<p> Refer to the description of <i>sqlcustom</i> for an explanation of how to specify initial data. </p>
<p> The <i>&#8211;database</i> option can be used to specify the database for which to print the SQL. </p>
<p> The <code>sql*</code> management commands now respect the <code>allow_migrate()</code> method of <code>DATABASE_ROUTERS</code>. If you have models synced to non-default databases, use the <i>&#8211;database</i> flag to get SQL for those models (previously they would always be included in the output). </p>
</dl>
<h3>sqlclear &lt;app_label app_label &#8230;&gt;</h3>
<dl>
<dt><code>django-admin sqlclear</code></p>
<dd>
<p> Prints the DROP TABLE SQL statements for the given app name(s). </p>
<p> The <i>&#8211;database</i> option can be used to specify the database for which to print the SQL.</dl>
<h3>sqlcustom &lt;app_label app_label &#8230;&gt;</h3>
<dl>
<dt><code>django-admin sqlcustom</code></p>
<dd>
<p> Prints the custom SQL statements for the given app name(s). </p>
<p> For each model in each specified app, this command looks for the file <code>&lt;app_label&gt;/sql/&lt;modelname&gt;.sql</code>, where <code>&lt;app_label&gt;</code> is the given app name and <code>&lt;modelname&gt;</code> is the model&#8217;s name in lowercase. For example, if you have an app <code>news</code> that includes a <code>Story</code> model, <code>sqlcustom</code> will attempt to read a file <code>news/sql/story.sql</code> and append it to the output of this command. </p>
<p> Each of the SQL files, if given, is expected to contain valid SQL. The SQL files are piped directly into the database after all of the models&#8217; table-creation statements have been executed. Use this SQL hook to make any table modifications, or insert any SQL functions into the database. </p>
<p> Note that the order in which the SQL files are processed is undefined. </p>
<p> The <i>&#8211;database</i> option can be used to specify the database for which to print the SQL.</dl>
<h3>sqldropindexes &lt;app_label app_label &#8230;&gt;</h3>
<dl>
<dt><code>django-admin sqldropindexes</code></p>
<dd>
<p> Prints the DROP INDEX SQL statements for the given app name(s). </p>
<p> The <i>&#8211;database</i> option can be used to specify the database for which to print the SQL.</dl>
<h3>sqlflush</h3>
<dl>
<dt><code>django-admin sqlflush</code></p>
<dd>
<p> Prints the SQL statements that would be executed for the <i>flush</i> command. </p>
<p> The <i>&#8211;database</i> option can be used to specify the database for which to print the SQL.</dl>
<h3>sqlindexes &lt;app_label app_label &#8230;&gt;</h3>
<dl>
<dt><code>django-admin sqlindexes</code></p>
<dd>
<p> Prints the CREATE INDEX SQL statements for the given app name(s). </p>
<p> The <i>&#8211;database</i> option can be used to specify the database for which to print the SQL.</dl>
<h3>sqlmigrate &lt;app_label&gt; &lt;migrationname&gt;</h3>
<dl>
<dt><code>django-admin sqlmigrate</code></p>
<dd>
<p> Prints the SQL for the named migration. This requires an active database connection, which it will use to resolve constraint names; this means you must generate the SQL against a copy of the database you wish to later apply it on. </p>
<p> Note that <code>sqlmigrate</code> doesn&#8217;t colorize its output. </p>
<p> The <i>&#8211;database</i> option can be used to specify the database for which to generate the SQL.</p>
<dt><code>&#8211;backwards</code></p>
<dd>
<p> By default, the SQL created is for running the migration in the forwards direction. Pass <code>&#8211;backwards</code> to generate the SQL for unapplying the migration instead.</dl>
<h3>sqlsequencereset &lt;app_label app_label &#8230;&gt;</h3>
<dl>
<dt><code>django-admin sqlsequencereset</code></p>
<dd>
<p> Prints the SQL statements for resetting sequences for the given app name(s). </p>
<p> Sequences are indexes used by some database engines to track the next available number for automatically incremented fields. </p>
<p> Use this command to generate SQL which will fix cases where a sequence is out of sync with its automatically incremented field data. </p>
<p> The <i>&#8211;database</i> option can be used to specify the database for which to print the SQL.</dl>
<h3>squashmigrations &lt;app_label&gt; &lt;migration_name&gt;</h3>
<dl>
<dt><code>django-admin squashmigrations</code></p>
<dd>
<p> Squashes the migrations for <code>app_label</code> up to and including <code>migration_name</code> down into fewer migrations, if possible. The resulting squashed migrations can live alongside the unsquashed ones safely. For more information, please read <i>migration-squashing</i>.</p>
<dt><code>&#8211;no-optimize</code></p>
<dd>
<p> By default, Django will try to optimize the operations in your migrations to reduce the size of the resulting file. Pass <code>&#8211;no-optimize</code> if this process is failing for you or creating incorrect migrations, though please also file a Django bug report about the behavior, as optimization is meant to be safe.</dl>
<h3>startapp &lt;app_label&gt; [destination]</h3>
<dl>
<dt><code>django-admin startapp</code></p>
<dd>
<p> Creates a Django app directory structure for the given app name in the current directory or the given destination. </p>
<p> By default the directory created contains a <code>models.py</code> file and other app template files. (See the <i>source</i> for more details.) If only the app name is given, the app directory will be created in the current working directory. </p>
<p> If the optional destination is provided, Django will use that existing directory rather than creating a new one. You can use &#8216;.&#8217; to denote the current working directory. </p>
<p> For example: </p>
<pre>
django-admin startapp myapp /Users/jezdez/Code/myapp
</pre>
<dt><code>&#8211;template</code></p>
<dd>
<p> With the <code>&#8211;template</code> option, you can use a custom app template by providing either the path to a directory with the app template file, or a path to a compressed file (<code>.tar.gz</code>, <code>.tar.bz2</code>, <code>.tgz</code>, <code>.tbz</code>, <code>.zip</code>) containing the app template files. </p>
<p> For example, this would look for an app template in the given directory when creating the <code>myapp</code> app: </p>
<pre>
django-admin startapp --template=/Users/jezdez/Code/my_app_template myapp
</pre>
<p> Django will also accept URLs (<code>http</code>, <code>https</code>, <code>ftp</code>) to compressed archives with the app template files, downloading and extracting them on the fly. </p>
<p> For example, taking advantage of Github&#8217;s feature to expose repositories as zip files, you can use a URL like: </p>
<pre>
django-admin startapp --template=<a rel="nofollow" href="https://github.com/githubuser/django-app-template/archive/master.zip">https://github.com/githubuser/django-app-template/archive/master.zip</a> myapp
</pre>
<p> When Django copies the app template files, it also renders certain files through the template engine: the files whose extensions match the <code>&#8211;extension</code> option (<code>py</code> by default) and the files whose names are passed with the <code>&#8211;name</code> option. The <code>template context</code> used is:</p>
<dt>&bull;</p>
<dd> Any option passed to the <code>startapp</code> command (among the command&#8217;s supported options)</p>
<dt>&bull;</p>
<dd> <code>app_name</code> &#8212; the app name as passed to the command</p>
<dt>&bull;</p>
<dd> <code>app_directory</code> &#8212; the full path of the newly created app</p>
<dt>&bull;</p>
<dd> <code>docs_version</code> &#8212; the version of the documentation: <code>&#8216;dev&#8217;</code> or <code>&#8216;1.x&#8217;</code> </p>
<p> <code>WARNING:</code> When the app template files are rendered with the Django template engine (by default all <code>*.py</code> files), Django will also replace all stray template variables contained. For example, if one of the Python files contains a docstring explaining a particular feature related to template rendering, it might result in an incorrect example. </p>
<p> To work around this problem, you can use the <code>templatetag</code> templatetag to &quot;escape&quot; the various parts of the template syntax.</dl>
<h3>startproject &lt;projectname&gt; [destination]</h3>
<dl>
<dt><code>django-admin startproject</code></p>
<dd>
<p> Creates a Django project directory structure for the given project name in the current directory or the given destination. </p>
<p> By default, the new directory contains <code>manage.py</code> and a project package (containing a <code>settings.py</code> and other files). See the <i>template source</i> for details. </p>
<p> If only the project name is given, both the project directory and project package will be named <code>&lt;projectname&gt;</code> and the project directory will be created in the current working directory. </p>
<p> If the optional destination is provided, Django will use that existing directory as the project directory, and create <code>manage.py</code> and the project package within it. Use &#8216;.&#8217; to denote the current working directory. </p>
<p> For example: </p>
<pre>
django-admin startproject myproject /Users/jezdez/Code/myproject_repo
</pre>
<p> As with the <i>startapp</i> command, the <code>&#8211;template</code> option lets you specify a directory, file path or URL of a custom project template. See the <i>startapp</i> documentation for details of supported project template formats. </p>
<p> For example, this would look for a project template in the given directory when creating the <code>myproject</code> project: </p>
<pre>
django-admin startproject --template=/Users/jezdez/Code/my_project_template myproject
</pre>
<p> Django will also accept URLs (<code>http</code>, <code>https</code>, <code>ftp</code>) to compressed archives with the project template files, downloading and extracting them on the fly. </p>
<p> For example, taking advantage of Github&#8217;s feature to expose repositories as zip files, you can use a URL like: </p>
<pre>
django-admin startproject --template=<a rel="nofollow" href="https://github.com/githubuser/django-project-template/archive/master.zip">https://github.com/githubuser/django-project-template/archive/master.zip</a> myproject
</pre>
<p> When Django copies the project template files, it also renders certain files through the template engine: the files whose extensions match the <code>&#8211;extension</code> option (<code>py</code> by default) and the files whose names are passed with the <code>&#8211;name</code> option. The <code>template context</code> used is:</p>
<dt>&bull;</p>
<dd> Any option passed to the <code>startproject</code> command (among the command&#8217;s supported options)</p>
<dt>&bull;</p>
<dd> <code>project_name</code> &#8212; the project name as passed to the command</p>
<dt>&bull;</p>
<dd> <code>project_directory</code> &#8212; the full path of the newly created project</p>
<dt>&bull;</p>
<dd> <code>secret_key</code> &#8212; a random key for the <code>SECRET_KEY</code> setting</p>
<dt>&bull;</p>
<dd> <code>docs_version</code> &#8212; the version of the documentation: <code>&#8216;dev&#8217;</code> or <code>&#8216;1.x&#8217;</code> </p>
<p> Please also see the <i>rendering warning</i> as mentioned for <i>startapp</i>.</dl>
<h3>syncdb</h3>
<dl>
<dt><code>django-admin syncdb</code></p>
<dd>
<p> Deprecated since version 1.7: This command has been deprecated in favor of the <i>migrate</i> command, which performs both the old behavior as well as executing migrations. It is now just an alias to that command. </p>
<p> Alias for <i>migrate</i>.</dl>
<h3>test &lt;app or test identifier&gt;</h3>
<dl>
<dt><code>django-admin test</code></p>
<dd>
<p> Runs tests for all installed models. See <code>/topics/testing/index</code> for more information.</p>
<dt><code>&#8211;failfast</code></p>
<dd>
<p> The <code>&#8211;failfast</code> option can be used to stop running tests and report the failure immediately after a test fails.</p>
<dt><code>&#8211;testrunner</code></p>
<dd>
<p> The <code>&#8211;testrunner</code> option can be used to control the test runner class that is used to execute tests. If this value is provided, it overrides the value provided by the <code>TEST_RUNNER</code> setting.</p>
<dt><code>&#8211;liveserver</code></p>
<dd>
<p> The <code>&#8211;liveserver</code> option can be used to override the default address where the live server (used with <code>LiveServerTestCase</code>) is expected to run from. The default value is <code>localhost:8081</code>.</p>
<dt><code>&#8211;keepdb</code></p>
<dd>
<p> The <code>&#8211;keepdb</code> option can be used to preserve the test database between test runs. This has the advantage of skipping both the create and destroy actions which greatly decreases the time to run tests, especially those in a large test suite. If the test database does not exist, it will be created on the first run and then preserved for each subsequent run. Any unapplied migrations will also be applied to the test database before running the test suite.</p>
<dt><code>&#8211;reverse</code></p>
<dd>
<p> The <code>&#8211;reverse</code> option can be used to sort test cases in the opposite order. This may help in debugging tests that aren&#8217;t properly isolated and have side effects. <i>Grouping by test class</i> is preserved when using this option.</p>
<dt><code>&#8211;debug-sql</code></p>
<dd>
<p> The <code>&#8211;debug-sql</code> option can be used to enable <i>SQL logging</i> for failing tests. If <i>&#8211;verbosity</i> is <code>2</code>, then queries in passing tests are also output.</dl>
<h3>testserver &lt;fixture fixture &#8230;&gt;</h3>
<dl>
<dt><code>django-admin testserver</code></p>
<dd>
<p> Runs a Django development server (as in <i>runserver</i>) using data from the given fixture(s). </p>
<p> For example, this command: </p>
<pre>
django-admin testserver mydata.json
</pre>
<p> &#8230;would perform the following steps:</p>
<dt>1.</p>
<dd> Create a test database, as described in <i>the-test-database</i>.</p>
<dt>2.</p>
<dd> Populate the test database with fixture data from the given fixtures. (For more on fixtures, see the documentation for <i>loaddata</i> above.)</p>
<dt>3.</p>
<dd> Runs the Django development server (as in <i>runserver</i>), pointed at this newly created test database instead of your production database. </p>
<p> This is useful in a number of ways:</p>
<dt>&bull;</p>
<dd> When you&#8217;re writing <code>unit tests</code> of how your views act with certain fixture data, you can use <code>testserver</code> to interact with the views in a Web browser, manually.</p>
<dt>&bull;</p>
<dd> Let&#8217;s say you&#8217;re developing your Django application and have a &quot;pristine&quot; copy of a database that you&#8217;d like to interact with. You can dump your database to a fixture (using the <i>dumpdata</i> command, explained above), then use <code>testserver</code> to run your Web application with that data. With this arrangement, you have the flexibility of messing up your data in any way, knowing that whatever data changes you&#8217;re making are only being made to a test database. </p>
<p> Note that this server does <i>not</i> automatically detect changes to your Python source code (as <i>runserver</i> does). It does, however, detect changes to templates.</p>
<dt><code>&#8211;addrport [port number or ipaddr:port]</code></p>
<dd>
<p> Use <code>&#8211;addrport</code> to specify a different port, or IP address and port, from the default of <code>127.0.0.1:8000</code>. This value follows exactly the same format and serves exactly the same function as the argument to the <i>runserver</i> command. </p>
<p> Examples: </p>
<p> To run the test server on port 7000 with <code>fixture1</code> and <code>fixture2</code>: </p>
<pre>
django-admin testserver --addrport 7000 fixture1 fixture2
django-admin testserver fixture1 fixture2 --addrport 7000
</pre>
<p> (The above statements are equivalent. We include both of them to demonstrate that it doesn&#8217;t matter whether the options come before or after the fixture arguments.) </p>
<p> To run on 1.2.3.4:7000 with a <code>test</code> fixture: </p>
<pre>
django-admin testserver --addrport 1.2.3.4:7000 test
</pre>
<p> The <i>&#8211;noinput</i> option may be provided to suppress all user prompts.</dl>
<h3>validate</h3>
<dl>
<dt><code>django-admin validate</code></p>
<dd>
<p> Deprecated since version 1.7: Replaced by the <i>check</i> command. </p>
<p> Validates all installed models (according to the <code>INSTALLED_APPS</code> setting) and prints validation errors to standard output.</dl>
<h2>COMMANDS PROVIDED BY APPLICATIONS</h2>
<p> Some commands are only available when the <code>django.contrib</code> application that <code>implements</code> them has been <code>enabled</code>. This section describes them grouped by their application.</p>
<h3><code>django.contrib.auth</code></h3>
<h3>changepassword</h3>
<dl>
<dt><code>django-admin changepassword</code></p>
<dd>
<p> This command is only available if Django&#8217;s <code>authentication system</code> (<code>django.contrib.auth</code>) is installed. </p>
<p> Allows changing a user&#8217;s password. It prompts you to enter twice the password of the user given as parameter. If they both match, the new password will be changed immediately. If you do not supply a user, the command will attempt to change the password whose username matches the current user. </p>
<p> Use the <code>&#8211;database</code> option to specify the database to query for the user. If it&#8217;s not supplied, Django will use the <code>default</code> database. </p>
<p> Example usage: </p>
<pre>
django-admin changepassword ringo
</pre>
</dl>
<h3>createsuperuser</h3>
<dl>
<dt><code>django-admin createsuperuser</code></p>
<dd>
<p> This command is only available if Django&#8217;s <code>authentication system</code> (<code>django.contrib.auth</code>) is installed. </p>
<p> Creates a superuser account (a user who has all permissions). This is useful if you need to create an initial superuser account or if you need to programmatically generate superuser accounts for your site(s). </p>
<p> When run interactively, this command will prompt for a password for the new superuser account. When run non-interactively, no password will be set, and the superuser account will not be able to log in until a password has been manually set for it.</p>
<dt><code>&#8211;username</code></p>
<dd>
<dt><code>&#8211;email</code></p>
<dd>
<p> The username and email address for the new account can be supplied by using the <code>&#8211;username</code> and <code>&#8211;email</code> arguments on the command line. If either of those is not supplied, <code>createsuperuser</code> will prompt for it when running interactively. </p>
<p> Use the <code>&#8211;database</code> option to specify the database into which the superuser object will be saved. </p>
<p> You can subclass the management command and override <code>get_input_data()</code> if you want to customize data input and validation. Consult the source code for details on the existing implementation and the method&#8217;s parameters. For example, it could be useful if you have a <code>ForeignKey</code> in <code>REQUIRED_FIELDS</code> and want to allow creating an instance instead of entering the primary key of an existing instance.</dl>
<h3><code>django.contrib.gis</code></h3>
<h3>ogrinspect</h3>
<p> This command is only available if <code>GeoDjango</code> (<code>django.contrib.gis</code>) is installed. </p>
<p> Please refer to its <code>description</code> in the GeoDjango documentation.</p>
<h3><code>django.contrib.sessions</code></h3>
<h3>clearsessions</h3>
<dl>
<dt><code>django-admin clearsessions</code></p>
<dd>
<p> Can be run as a cron job or directly to clean out expired sessions.</dl>
<h3><code>django.contrib.sitemaps</code></h3>
<h3>ping_google</h3>
<p> This command is only available if the <code>Sitemaps framework</code> (<code>django.contrib.sitemaps</code>) is installed. </p>
<p> Please refer to its <code>description</code> in the Sitemaps documentation.</p>
<h3><code>django.contrib.staticfiles</code></h3>
<h3>collectstatic</h3>
<p> This command is only available if the <code>static files application</code> (<code>django.contrib.staticfiles</code>) is installed. </p>
<p> Please refer to its <code>description</code> in the <code>staticfiles</code> documentation.</p>
<h3>findstatic</h3>
<p> This command is only available if the <code>static files application</code> (<code>django.contrib.staticfiles</code>) is installed. </p>
<p> Please refer to its <code>description</code> in the <code>staticfiles</code> documentation.</p>
<h2>DEFAULT OPTIONS</h2>
<p> Although some commands may allow their own custom options, every command allows for the following options:</p>
<dl>
<dt><code>&#8211;pythonpath</code></p>
<dd>
<p> Example usage: </p>
<pre>
django-admin migrate --pythonpath='/home/djangoprojects/myproject'
</pre>
<p> Adds the given filesystem path to the Python <i>import search path</i>. If this isn&#8217;t provided, <code>django-admin</code> will use the <code>PYTHONPATH</code> environment variable. </p>
<p> Note that this option is unnecessary in <code>manage.py</code>, because it takes care of setting the Python path for you.</p>
<dt><code>&#8211;settings</code></p>
<dd>
<p> Example usage: </p>
<pre>
django-admin migrate --settings=mysite.settings
</pre>
<p> Explicitly specifies the settings module to use. The settings module should be in Python package syntax, e.g. <code>mysite.settings</code>. If this isn&#8217;t provided, <code>django-admin</code> will use the <code>DJANGO_SETTINGS_MODULE</code> environment variable. </p>
<p> Note that this option is unnecessary in <code>manage.py</code>, because it uses <code>settings.py</code> from the current project by default.</p>
<dt><code>&#8211;traceback</code></p>
<dd>
<p> Example usage: </p>
<pre>
django-admin migrate --traceback
</pre>
<p> By default, <code>django-admin</code> will show a simple error message whenever an <code>CommandError</code> occurs, but a full stack trace for any other exception. If you specify <code>&#8211;traceback</code>, <code>django-admin</code> will also output a full stack trace when a <code>CommandError</code> is raised.</p>
<dt><code>&#8211;verbosity</code></p>
<dd>
<p> Example usage: </p>
<pre>
django-admin migrate --verbosity 2
</pre>
<p> Use <code>&#8211;verbosity</code> to specify the amount of notification and debug information that <code>django-admin</code> should print to the console.</p>
<dt>&bull;</p>
<dd> <code>0</code> means no output.</p>
<dt>&bull;</p>
<dd> <code>1</code> means normal output (default).</p>
<dt>&bull;</p>
<dd> <code>2</code> means verbose output.</p>
<dt>&bull;</p>
<dd> <code>3</code> means <i>very</i> verbose output.</p>
<dt><code>&#8211;no-color</code></p>
<dd>
<p> Example usage: </p>
<pre>
django-admin sqlall --no-color
</pre>
<p> By default, <code>django-admin</code> will format the output to be colorized. For example, errors will be printed to the console in red and SQL statements will be syntax highlighted. To prevent this and have a plain text output, pass the <code>&#8211;no-color</code> option when running your command.</dl>
<h2>COMMON OPTIONS</h2>
<p> The following options are not available on every command, but they are common to a number of commands.</p>
<dl>
<dt><code>&#8211;database</code></p>
<dd>
<p> Used to specify the database on which a command will operate. If not specified, this option will default to an alias of <code>default</code>. </p>
<p> For example, to dump data from the database with the alias <code>master</code>: </p>
<pre>
django-admin dumpdata --database=master
</pre>
<dt><code>&#8211;exclude</code></p>
<dd>
<p> Exclude a specific application from the applications whose contents is output. For example, to specifically exclude the <code>auth</code> application from the output of dumpdata, you would call: </p>
<pre>
django-admin dumpdata --exclude=auth
</pre>
<p> If you want to exclude multiple applications, use multiple <code>&#8211;exclude</code> directives: </p>
<pre>
django-admin dumpdata --exclude=auth --exclude=contenttypes
</pre>
<dt><code>&#8211;locale</code></p>
<dd>
<p> Use the <code>&#8211;locale</code> or <code>-l</code> option to specify the locale to process. If not provided all locales are processed.</p>
<dt><code>&#8211;noinput</code></p>
<dd>
<p> Use the <code>&#8211;noinput</code> option to suppress all user prompting, such as &quot;Are you sure?&quot; confirmation messages. This is useful if <code>django-admin</code> is being executed as an unattended, automated script.</dl>
<h2>EXTRA NICETIES</h2>
<h3>Syntax coloring</h3>
<p> The <code>django-admin</code> / <code>manage.py</code> commands will use pretty color-coded output if your terminal supports ANSI-colored output. It won&#8217;t use the color codes if you&#8217;re piping the command&#8217;s output to another program. </p>
<p> Under Windows, the native console doesn&#8217;t support ANSI escape sequences so by default there is no color output. But you can install the <i>ANSICON</i> third-party tool, the Django commands will detect its presence and will make use of its services to color output just like on Unix-based platforms. </p>
<p> The colors used for syntax highlighting can be customized. Django ships with three color palettes:</p>
<dl>
<dt>&bull;</p>
<dd> <code>dark</code>, suited to terminals that show white text on a black background. This is the default palette.</p>
<dt>&bull;</p>
<dd> <code>light</code>, suited to terminals that show black text on a white background.</p>
<dt>&bull;</p>
<dd> <code>nocolor</code>, which disables syntax highlighting. </p>
<p> You select a palette by setting a <code>DJANGO_COLORS</code> environment variable to specify the palette you want to use. For example, to specify the <code>light</code> palette under a Unix or OS/X BASH shell, you would run the following at a command prompt: </p>
<pre>
export DJANGO_COLORS=&quot;light&quot;
</pre>
<p> You can also customize the colors that are used. Django specifies a number of roles in which color is used:</p>
<dt>&bull;</p>
<dd> <code>error</code> &#8211; A major error.</p>
<dt>&bull;</p>
<dd> <code>notice</code> &#8211; A minor error.</p>
<dt>&bull;</p>
<dd> <code>sql_field</code> &#8211; The name of a model field in SQL.</p>
<dt>&bull;</p>
<dd> <code>sql_coltype</code> &#8211; The type of a model field in SQL.</p>
<dt>&bull;</p>
<dd> <code>sql_keyword</code> &#8211; An SQL keyword.</p>
<dt>&bull;</p>
<dd> <code>sql_table</code> &#8211; The name of a model in SQL.</p>
<dt>&bull;</p>
<dd> <code>http_info</code> &#8211; A 1XX HTTP Informational server response.</p>
<dt>&bull;</p>
<dd> <code>http_success</code> &#8211; A 2XX HTTP Success server response.</p>
<dt>&bull;</p>
<dd> <code>http_not_modified</code> &#8211; A 304 HTTP Not Modified server response.</p>
<dt>&bull;</p>
<dd> <code>http_redirect</code> &#8211; A 3XX HTTP Redirect server response other than 304.</p>
<dt>&bull;</p>
<dd> <code>http_not_found</code> &#8211; A 404 HTTP Not Found server response.</p>
<dt>&bull;</p>
<dd> <code>http_bad_request</code> &#8211; A 4XX HTTP Bad Request server response other than 404.</p>
<dt>&bull;</p>
<dd> <code>http_server_error</code> &#8211; A 5XX HTTP Server Error response. </p>
<p> Each of these roles can be assigned a specific foreground and background color, from the following list:</p>
<dt>&bull;</p>
<dd> <code>black</code></p>
<dt>&bull;</p>
<dd> <code>red</code></p>
<dt>&bull;</p>
<dd> <code>green</code></p>
<dt>&bull;</p>
<dd> <code>yellow</code></p>
<dt>&bull;</p>
<dd> <code>blue</code></p>
<dt>&bull;</p>
<dd> <code>magenta</code></p>
<dt>&bull;</p>
<dd> <code>cyan</code></p>
<dt>&bull;</p>
<dd> <code>white</code> </p>
<p> Each of these colors can then be modified by using the following display options:</p>
<dt>&bull;</p>
<dd> <code>bold</code></p>
<dt>&bull;</p>
<dd> <code>underscore</code></p>
<dt>&bull;</p>
<dd> <code>blink</code></p>
<dt>&bull;</p>
<dd> <code>reverse</code></p>
<dt>&bull;</p>
<dd> <code>conceal</code> </p>
<p> A color specification follows one of the following patterns:</p>
<dt>&bull;</p>
<dd> <code>role=fg</code></p>
<dt>&bull;</p>
<dd> <code>role=fg/bg</code></p>
<dt>&bull;</p>
<dd> <code>role=fg,option,option</code></p>
<dt>&bull;</p>
<dd> <code>role=fg/bg,option,option</code> </p>
<p> where <code>role</code> is the name of a valid color role, <code>fg</code> is the foreground color, <code>bg</code> is the background color and each <code>option</code> is one of the color modifying options. Multiple color specifications are then separated by semicolon. For example: </p>
<pre>
export DJANGO_COLORS=&quot;error=yellow/blue,blink;notice=magenta&quot;
</pre>
<p> would specify that errors be displayed using blinking yellow on blue, and notices displayed using magenta. All other color roles would be left uncolored. </p>
<p> Colors can also be specified by extending a base palette. If you put a palette name in a color specification, all the colors implied by that palette will be loaded. So: </p>
<pre>
export DJANGO_COLORS=&quot;light;error=yellow/blue,blink;notice=magenta&quot;
</pre>
<p> would specify the use of all the colors in the light color palette, <i>except</i> for the colors for errors and notices which would be overridden as specified. </p>
<p> Support for color-coded output from <code>django-admin</code> / <code>manage.py</code> utilities on Windows by relying on the ANSICON application was added in Django 1.7.</dl>
<h3>Bash completion</h3>
<p> If you use the Bash shell, consider installing the Django bash completion script, which lives in <code>extras/django_bash_completion</code> in the Django distribution. It enables tab-completion of <code>django-admin</code> and <code>manage.py</code> commands, so you can, for instance&#8230;</p>
<dl>
<dt>&bull;</p>
<dd> Type <code>django-admin</code>.</p>
<dt>&bull;</p>
<dd> Press [TAB] to see all available options.</p>
<dt>&bull;</p>
<dd> Type <code>sql</code>, then [TAB], to see all available options whose names start with <code>sql</code>. </p>
<p> See <code>/howto/custom-management-commands</code> for how to add customized actions.</p>
<dt><code>django.core.management.call_command(name, *args, **options)</code></p>
<dd>
<p> To call a management command from code use <code>call_command</code>.</p>
<dt><code>name</code></p>
<dd> the name of the command to call.</p>
<dt><code>*args</code></p>
<dd> a list of arguments accepted by the command.</p>
<dt><code>**options</code></p>
<dd> named options accepted on the command-line. </p>
<p> Examples: </p>
<pre>
from django.core import management
management.call_command('flush', verbosity=0, interactive=False)
management.call_command('loaddata', 'test_data', verbosity=0)
</pre>
<p> Note that command options that take no arguments are passed as keywords with <code>True</code> or <code>False</code>, as you can see with the <code>interactive</code> option above. </p>
<p> Named arguments can be passed by using either one of the following syntaxes: </p>
<pre>
# Similar to the command line
management.call_command('dumpdata', '--natural-foreign')
# Named argument similar to the command line minus the initial dashes and
# with internal dashes replaced by underscores
management.call_command('dumpdata', natural_foreign=True)
# `use_natural_foreign_keys` is the option destination variable
management.call_command('dumpdata', use_natural_foreign_keys=True)
</pre>
<p> The first syntax is now supported thanks to management commands using the <i>argparse</i> module. For the second syntax, Django previously passed the option name as-is to the command, now it is always using the <code>dest</code> variable name (which may or may not be the same as the option name). </p>
<p> Command options which take multiple options are passed a list: </p>
<pre>
management.call_command('dumpdata', exclude=['contenttypes', 'auth'])
</pre>
</dl>
<h2>OUTPUT REDIRECTION</h2>
<p> Note that you can redirect standard output and error streams as all commands support the <code>stdout</code> and <code>stderr</code> options. For example, you could write: </p>
<pre>
with open('/path/to/command_output') as f:
    management.call_command('dumpdata', stdout=f)
</pre>
<h2>AUTHOR</h2>
<p> Django Software Foundation</p>
<h2>COPYRIGHT</h2>
<p> Django Software Foundation and contributors </p>
<h2>Index</h2>
<dt><a href="#lbBU">COMMANDS PROVIDED BY APPLICATIONS</a></p>
<dd>
<dt><a href="#lbCH">DEFAULT OPTIONS</a></p>
<dd>
<dt><a href="#lbCI">COMMON OPTIONS</a></p>
<dd>
<dt><a href="#lbCJ">EXTRA NICETIES</a></p>
<dd>
<dt><a href="#lbCM">OUTPUT REDIRECTION</a></p>
<dd>
<dt><a href="#lbCN">AUTHOR</a></p>
<dd>
<dt><a href="#lbCO">COPYRIGHT</a></p>
<dd></dl>
