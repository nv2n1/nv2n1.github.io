---

title: "ledger(1)"
name: "ledger"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ledger/"
description: "ledger – Command-line, double-entry account reporting tool"
---

<h2>NAME</h2>
<p> <code>ledger</code> &#8211; Command-line, double-entry account reporting tool</p>
<p> [<i>command</i> ] [<i>options</i> ] [<i>arguments</i> ]</p>
<p> is a command-line accounting tool based on the power and completeness of double-entry accounting. It is only a reporting tool, which means it never modifies your data files, but it does offer a large selection of reports, and different ways to customize them to your needs.</p>
<h2>COMMANDS</h2>
<p> accepts several top-level commands, each of which generates a different kind of basic report. Most of them accept a <i>report-query</i> argument, in order to determine what should be reported. To understand the syntax of a <i>report-query</i> see the section on Sx QUERIES . In its most basic form, simply specifying one or more strings produces a report for all accounts containing those strings. </p>
<p> If no command is given, enters a <code>REPL</code> or command loop, allowing several commands to be executed on the same dataset without reparsing. </p>
<p> The following is a complete list of accepted reporting commands:</p>
<dl>
<dt><code>accounts </code>[<i>report-query </i>]</dt>
<dd> List all accounts for postings that match the <i>report-query</i></dd></dl>
<dl>
<dt><code>balance </code>[<i>report-query </i>]</dt>
<dd> Print a balance report showing totals for postings that match <i>report-query</i> and aggregate totals for parents of those accounts. Options most commonly used with this command are:</dd>
<dl>
<dt><code>&#8211;basis (-B</code> )</dt>
<dd> Report in terms of cost basis, not amount or value. This is the only form of report which is guaranteed to always balance to zero, when no <i>report-query</i> is specified. Only show totals for the top-most accounts.</dd>
<dt><code>&#8211;empty (-E</code> )</dt>
<dd> Show accounts whose total is zero.</dd>
<dt><code>&#8211;flat</code></dt>
<dd> Rather than display a hierarchical tree, flatten the report to show subtotals for only accounts matching <i>report-query</i></dd>
<dt><code>&#8211;no-total</code></dt>
<dd> Suppress the summary total shown at the bottom of the report.</dd></dl>
<p> The synonyms <code>bal</code> and <code>b</code> are also accepted.</p>
<dt><code>budget </code>[<i>report-query </i>]</dt>
<dd> A special balance report which includes three extra columns: the amount budgeted during the reporting period, how spending differed from the budget, and the percentage of budget spent (exceeds 100% if you go over budget). Note that budgeting requires one or more Do periodic transactions Dc to be defined in your data file(s). See the manual for more information.</dd>
<dt><code>cleared </code>[<i>report-query </i>]</dt>
<dd> A special balance report which adds two extra columns: the cleared balance for each account, and the date of the most recent cleared posting in that account. For this accounting to be meaningful, the cleared flag must be set on at least one posting. See the manual for more information.</dd>
<dt><code>commodities </code>[<i>report-query </i>]</dt>
<dd> List all commodities for postings matching the <i>report-query</i></dd>
<dt><code>convert</code></dt>
<dd> Reads data from a CSV (comma-separated values) file and generates transactions.</dd>
<dt><code>csv </code>[<i>report-query </i>]</dt>
<dd> Report of postings matching the <i>report-query</i> in CSV format (comma-separated values). Useful for exporting data to a spreadsheet for further analysis or charting.</dd>
<dt><code>entry </code>[<i>entry-template </i>]</dt>
<dd> Generate and display a new, properly formatted transaction by comparing the <i>entry-template</i> to the transactions in your data file(s). For more information on draft templates and using this command to quickly create new transactions, see the section Sx ENTRIES . </dd>
<p> The synonym <code>xact</code> is also accepted.</p>
<dt><code>emacs </code>[<i>query </i>]</dt>
<dd> Output posting and transaction data in a format readily consumed by the Emacs editor, in a series of Lisp forms. This is used by the ledger.el Emacs mode to process reporting data from <code>.</code></dd>
<dt><code>equity </code>[<i>report-query </i>]</dt>
<dd> Print a transaction with a series of postings that balance current totals for accounts matching the <i>report-query</i> in a special account called <code>Equity:Opening Balances</code> The purpose of this report is to close the books for a prior year, while using these equity postings to carry forward those balances.</dd>
<dt><code>org</code></dt>
<dd> Produce a journal file suitable for use in the Emacs org mode.</dd>
<dt><code>payees </code>[<i>report-query </i>]</dt>
<dd> List all payees for postings matching the <i>report-query</i></dd>
<dt><code>pricemap</code></dt>
<dd> Produce a file which can be used to generate a graph with graphviz showing the relationship of commodities in the file.</dd>
<dt><code>prices </code>[<i>report-query </i>]</dt>
<dd> Report prices for all commodities in postings matching the <i>report-query</i> The prices are reported with the granularity of a single day.</dd>
<dt><code>pricedb </code>[<i>report-query </i>]</dt>
<dd> Report prices for all commodities in postings matching the <i>report-query</i> Prices are reported down to the second, using the same format as the ~/.pricedb file.</dd>
<dt><code>print </code>[<i>report-query </i>]</dt>
<dd> Print out the full transactions of any matching postings using the same format as they would appear in a data file. This can be used to extract subsets from a file to transfer to other files.</dd>
<dt><code>push </code>[<i>options </i>]</dt>
<dd> In the <code>REPL</code> push a set of command-line <i>options</i> so that they will apply to all subsequent reports.</dd>
<dt><code>pop</code></dt>
<dd> In the <code>REPL</code> pop any option settings that have been <code>push</code> ed.</dd>
<dt><code>register </code>[<i>report-query </i>]</dt>
<dd> List all postings matching the <i>report-query</i> This is one of the most common commands, and can be used to provide a variety of useful reports. Options most commonly used with this command are: </dd>
<dl>
<dt><code>&#8211;average (-A</code> )</dt>
<dd> Show the running average, rather than a running total.</dd>
<dt><code>&#8211;current (-c</code> )</dt>
<dd> Don&#8217;t show postings beyond the present day.</dd>
<dt><code>&#8211;exchange </code><i>commodity (-</i><code>X</code> )</dt>
<dd> Render all values in the given <i>commodity</i> if a price conversion rate can be determined. Rates are always displayed relative to the date of the posting they are calculated for. This means a <code>register</code> report is a historical value report. For current values, it may be preferable to use the <code>balance</code> report.</dd>
<dt><code>&#8211;gain (-G</code> )</dt>
<dd> Show any gains (or losses) in commodity values over time.</dd>
<dt><code>&#8211;head </code><i>number</i></dt>
<dd> Only show the top <i>number</i> postings.</dd>
<dt><code>&#8211;historical (-H</code> )</dt>
<dd> Value commodities at the time of their acquisition.</dd>
<dt><code>&#8211;invert</code></dt>
<dd> Invert the value of amounts shown.</dd>
<dt><code>&#8211;market (-V</code> )</dt>
<dd> Show current market values for all amounts. This is determined in a somewhat magical fashion. It is probably more straightforward to use &#8211;<code>-exchange</code> option.</dd>
<dt><code>&#8211;period </code><i>time-period (-</i><code>p</code> )</dt>
<dd> Show postings only for the given <i>time-period</i></dd>
<dt><code>&#8211;related (-r</code> )</dt>
<dd> Show postings that are related to those that would have been shown. It has the effect of displaying the Qq other side of the postings.</dd>
<dt><code>&#8211;sort </code><i>value-expression (-</i><code>S</code> )</dt>
<dd> Sort postings by evaluating the given <i>value-expression</i> Note that a comma-separated list of expressions is allowed, in which case each sorting term is used in order to determine the final ordering. For example, to search by date and then amount, one would use: </dd>
<blockquote><p><tt>ledger reg --sort 'date, amount'</tt></p></blockquote>
<dt><code>&#8211;tail </code><i>number</i></dt>
<dd> Only show the last <i>number</i> postings.</dd>
<dt><code>&#8211;uncleared (-U</code> )</dt>
<dd> Only show uncleared (i.e., recent) postings.</dd></dl>
<p> There are also several grouping options that can be useful: </p>
<dl>
<dt><code>&#8211;by-payee (-P</code> )</dt>
<dd> Group postings by common payee names.</dd>
<dt><code>&#8211;daily (-D</code> )</dt>
<dd> Group postings by day.</dd>
<dt><code>&#8211;weekly (-W</code> )</dt>
<dd> Group postings by week (starting on Sundays).</dd>
<dt><code>&#8211;start-of-week </code><i>day</i></dt>
<dd> Set the start of each report grouped by week to the given <i>day</i></dd>
<dt><code>&#8211;monthly (-M</code> )</dt>
<dd> Group postings by month.</dd>
<dt><code>&#8211;quarterly</code></dt>
<dd> Group postings by fiscal quarter.</dd>
<dt><code>&#8211;yearly (-Y</code> )</dt>
<dd> Group postings by year.</dd>
<dt><code>&#8211;days-of-week</code></dt>
<dd> Group postings by the day of the week on which they took place.</dd>
<dt><code>&#8211;subtotal (-s</code> )</dt>
<dd> Group all postings together. This is very similar to the totals shown by the <code>balance</code> report.</dd></dl>
<p> The synonyms <code>reg</code> and <code>r</code> are also accepted.</p>
<dt><code>server</code></dt>
<dd> This command requires that Python support be active. If so, it starts up an <code>HTTP</code> server listening for requests on port 9000. This provides an alternate interface to creating and viewing reports. Note that this is very much a work-in-progress, and will not be fully functional until a later version.</dd>
<dt><code>select </code>[<i>sql-query </i>]</dt>
<dd> List all postings matching the <i>sql-query</i> This command allows to generate SQL-like queries, e.g.: </dd>
<blockquote><p><tt></tt><code>ledger select date,amount from posts where account=~/Income/</code> </p></blockquote>
<dt><code>source</code></dt>
<dd> Parse a journal file and checks it for errors. will return success if no errors are found.</dd>
<dt><code>stats </code>[<i>report-query </i>]</dt>
<dd> Provide summary information about all the postings matching <i>report-query</i> It provides information such as: </dd>
<ul>
<li> Time range of all matching postings
<li> Unique payees
<li> Unique accounts
<li> Postings total
<li> Uncleared postings
<li> Days since last posting
<li> Posts in the last 7 days
<li> Posts in the last 30 days
<li> Posts this month </ul>
<dt><code>xml </code>[<i>report-query </i>]</dt>
<dd> Output data relating to the current report in <code>XML</code> format. It includes all accounts and commodities involved in the report, plus the postings and the transactions they are contained in. See the manual for more information.</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;abbrev-len </code><i>INT</i></dt>
<dd> Set the minimum length an account can be abbreviated to if it doesn&#8217;t fit inside the <code>account-width</code> If <i>INT</i> is zero, then the account name will be truncated on the right. If <i>INT</i> is greater than <code>account-width</code> then the account will be truncated on the left, with no shortening of the account names in order to fit into the desired width.</dd>
<dt><code>&#8211;account </code><i>EXPR</i></dt>
<dd> Prepend <i>EXPR</i> to all accounts reported. That is, the option &#8211;<code>-account </code><i>&quot;&#8217;Personal&#8217;&quot;</i> would tack <i>Personal:</i> and &#8211;<code>-account </code><i>&quot;tag(&#8216;VAT&#8217;)&quot;</i> would tack the value of the VAT tag to the beginning of every account reported in a <code>balance</code> or <code>register</code> report.</dd>
<dt><code>&#8211;account-width </code><i>INT</i></dt>
<dd> Set the width of the account column in the <code>register</code> report to <i>INT</i> characters.</dd>
<dt><code>&#8211;actual (-L</code> )</dt>
<dd> Report only real transactions, with no automated or virtual transactions used.</dd>
<dt><code>&#8211;add-budget</code></dt>
<dd> Show only un-budgeted postings.</dd>
<dt><code>&#8211;amount </code><i>EXPR (-</i><code>t</code> )</dt>
<dd> Apply the given value expression to the posting amount. Using &#8211;<code>-amount </code><i>EXPR</i> you can apply an arbitrary transformation to the postings.</dd>
<dt><code>&#8211;amount-data (-j</code> )</dt>
<dd> On a register report print only the dates and amount of postings. Useful for graphing and spreadsheet applications.</dd>
<dt><code>&#8211;amount-width </code><i>INT</i></dt>
<dd> Set the width in characters of the amount column in the <code>register</code> report.</dd>
<dt><code>&#8211;anon</code></dt>
<dd> Anonymize registry output, mostly for sending in bug reports.</dd>
<dt><code>&#8211;ansi</code></dt>
<dd> Use color if the terminal supports it. Alias for &#8211;<code>-color</code></dd>
<dt><code>&#8211;args-only</code></dt>
<dd> Ignore init files and environment variables for the run.</dd>
<dt><code>&#8211;auto-match</code></dt>
<dd> When generating a ledger transaction from a CSV file using the <code>convert</code> command, automatically match an account from the Ledger journal.</dd>
<dt><code>&#8211;aux-date</code></dt>
<dd> Show auxiliary dates for all calculations. Alias for &#8211;<code>-effective</code></dd>
<dt><code>&#8211;average (-A</code> )</dt>
<dd> Print average values over the number of transactions instead of running totals.</dd>
<dt><code>&#8211;balance-format </code><i>FMT</i></dt>
<dd> Specify the format to use for the <code>balance</code> report.</dd>
<dt><code>&#8211;base</code></dt>
<dd> Reduce convertible commodities down the bottom of the conversion, e.g. display time in seconds.</dd>
<dt><code>&#8211;basis (-B</code> )</dt>
<dd> Report the cost basis on all posting. Alias for &#8211;<code>-cost</code></dd>
<dt><code>&#8211;begin </code><i>DATE (-</i><code>b</code> )</dt>
<dd> Specify the start <i>DATE</i> of all calculations. Transactions before that date will be ignored.</dd>
<dt><code>&#8211;bold-if </code><i>EXPR</i></dt>
<dd> Print the entire line in bold if the given value expression is true.</dd>
<dt><code>&#8211;budget</code></dt>
<dd> Only display budgeted items. In a <code>register</code> report this displays transaction in the budget, in a balance report this displays accounts in the budget.</dd>
<dt><code>&#8211;budget-format </code><i>FMT</i></dt>
<dd> Specify the format to use for the <code>budget</code> report.</dd>
<dt><code>&#8211;by-payee (-P</code> )</dt>
<dd> Group postings in the register report by common payee names.</dd>
<dt><code>&#8211;check-payees</code></dt>
<dd> Enable strict and pedantic checking for payees as well as accounts, commodities and tags.</dd>
<dt><code>&#8211;cleared (-C</code> )</dt>
<dd> Display only cleared postings.</dd>
<dt><code>&#8211;cleared-format </code><i>FMT</i></dt>
<dd> Specify the format to use for the <code>cleared</code> report</dd>
<dt><code>&#8211;collapse (-n</code> )</dt>
<dd> Print only the top level accounts.</dd>
<dt><code>&#8211;collapse-if-zero</code></dt>
<dd> Collapse the account display only if it has a zero balance.</dd>
<dt><code>&#8211;color</code></dt>
<dd> Use color if the terminal supports it. Alias for &#8211;<code>-ansi</code></dd>
<dt><code>&#8211;columns </code><i>INT</i></dt>
<dd> Make the <code>register</code> report <i>INT</i> characters wide. By default will use all available columns in your terminal.</dd>
<dt><code>&#8211;cost</code></dt>
<dd> Report the cost basis on all posting. Alias for &#8211;<code>-basis</code></dd>
<dt><code>&#8211;count</code></dt>
<dd> Direct to report the number of items when appended to the <code>commodities</code> <code>accounts</code> or <code>payees</code> commands.</dd>
<dt><code>&#8211;csv-format </code><i>FMT</i></dt>
<dd> Format <code>csv</code> report according to <i>FMT</i></dd>
<dt><code>&#8211;current (-c</code> )</dt>
<dd> Shorthand for &#8211;<code>-limit </code><i>&#8216;date &lt;= today&#8217;</i></dd>
<dt><code>&#8211;daily (-D</code> )</dt>
<dd> Shorthand for &#8211;<code>-period </code><i>daily</i></dd>
<dt><code>&#8211;date </code><i>EXPR</i></dt>
<dd> Transform the date of the transaction using <i>EXPR</i></dd>
<dt><code>&#8211;date-format </code><i>DATEFMT (-</i><code>y</code> )</dt>
<dd> Print dates using <i>DATEFMT</i> Refer to <a href="/docs/linux/man/3-strftime/">strftime</a>(3) for details on the format string syntax.</dd>
<dt><code>&#8211;datetime-format </code><i>DATETIMEFMT</i></dt>
<dd> Print datetimes using <i>DATETIMEFMT</i> Refer to <a href="/docs/linux/man/3-strftime/">strftime</a>(3) for details on the format string syntax.</dd>
<dt><code>&#8211;date-width </code><i>INT</i></dt>
<dd> Specify the width, in characters, of the date column in the <code>register</code> report.</dd>
<dt><code>&#8211;day-break</code></dt>
<dd> Break up <code>register</code> report of timelog entries that span multiple days by day.</dd>
<dt><code>&#8211;days-of-week</code></dt>
<dd> Group transactions by the days of the week. Alias for &#8211;<code>-dow</code></dd>
<dt><code>&#8211;dc</code></dt>
<dd> Display register or balance in debit/credit format If you use &#8211;<code>-dc</code> with either the <code>register</code> or <code>balance</code> commands, you will now get separate columns for debits and credits.</dd>
<dt><code>&#8211;debug </code><i>STR</i></dt>
<dd> If has been built with debug options this will provide extra data during the run.</dd>
<dt><code>&#8211;decimal-comma</code></dt>
<dd> Direct to parse journals using the European standard comma as decimal separator, vice a period.</dd>
<dt><code>&#8211;depth </code><i>INT</i></dt>
<dd> Limit the depth of the account tree. In a balance report, for example, &#8211;<code>-depth </code><i>2</i> will print balances only for accounts with two levels, i.e. <code>Expenses:Entertainment</code> but not <code>Expenses:Entertainment:Dining</code> This is a display predicate, which means it only affects display, not the total calculations.</dd>
<dt><code>&#8211;detail</code></dt>
<dd> Related to <code>convert</code> command. Synonym to &#8211;<code>-rich-data</code> option.</dd>
<dt><code>&#8211;deviation</code></dt>
<dd> Report each posting&#8217;s deviation from the average. It is only meaningful in the <code>register and prices</code> reports.</dd>
<dt><code>&#8211;display </code><i>EXPR (-</i><code>d</code> )</dt>
<dd> Display lines that satisfy the expression <i>EXPR</i></dd>
<dt><code>&#8211;display-amount </code><i>EXPR</i></dt>
<dd> Apply a transformation to the <i>displayed</i> amount. This occurs after calculations occur.</dd>
<dt><code>&#8211;display-total </code><i>EXPR</i></dt>
<dd> Apply a transformation to the <i>displayed</i> total. This occurs after calculations occur.</dd>
<dt><code>&#8211;dow</code></dt>
<dd> Group transactions by the days of the week. Alias for &#8211;<code>-days-of-week</code></dd>
<dt><code>&#8211;download</code></dt>
<dd> Cause quotes to be automagically downloaded, as needed, by running a script named <i>getquote</i> and expecting that script to return a value understood by <code>.</code> A sample implementation of a <i>getquote</i> script, implemented in Perl, is provided in the distribution. Downloaded quote price are then appended to the price database, usually specified using the environment variable <code>LEDGER_PRICE_DB</code></dd>
<dt><code>&#8211;effective</code></dt>
<dd> Show auxiliary dates for all calculations. Alias for &#8211;<code>-aux-date</code></dd>
<dt><code>&#8211;empty (-E</code> )</dt>
<dd> Include empty accounts in report.</dd>
<dt><code>&#8211;end </code><i>DATE (-</i><code>e</code> )</dt>
<dd> Constrain the report so that transactions on or after <i>DATE</i> are not considered.</dd>
<dt><code>&#8211;equity</code></dt>
<dd> Related to the <code>equity</code> command. Gives current account balances in the form of a register report.</dd>
<dt><code>&#8211;exact</code></dt>
<dd> Report beginning and ending of periods by the date of the first and last posting occurring in that period.</dd>
<dt><code>&#8211;exchange </code><i>COMMODITY </i>[, <i>COMMODITY, &#8230; (-</i><code>X</code> ) ]</dt>
<dd> Display values in terms of the given <i>COMMODITY</i> The latest available price is used.</dd>
<dt><code>&#8211;explicit</code></dt>
<dd> Direct to require pre-declarations for entities (such as accounts, commodities and tags) rather than taking entities from cleared transactions as defined.</dd>
<dt><code>&#8211;file </code><i>FILE</i></dt>
<dd> Read journal data from <i>FILE</i></dd>
<dt><code>&#8211;first </code><i>INT</i></dt>
<dd> Print the first <i>INT</i> entries. Opposite of &#8211;<code>-last </code><i>INT</i> Alias for &#8211;<code>-head</code></dd>
<dt><code>&#8211;flat</code></dt>
<dd> Force the full names of accounts to be used in the balance report. The balance report will not use an indented tree.</dd>
<dt><code>&#8211;force-color</code></dt>
<dd> Output TTY color codes even if the TTY doesn&#8217;t support them. Useful for TTYs that don&#8217;t advertise their capabilities correctly.</dd>
<dt><code>&#8211;force-pager</code></dt>
<dd> Force to paginate its output.</dd>
<dt><code>&#8211;forecast-while </code><i>EXPR</i></dt>
<dd> Continue forecasting while <i>VEXPR</i> is true. Alias for &#8211;<code>-forecast</code></dd>
<dt><code>&#8211;forecast-years </code><i>INT</i></dt>
<dd> Forecast at most <i>INT</i> years into the future.</dd>
<dt><code>&#8211;format </code><i>FMT (-</i><code>F</code> )</dt>
<dd> Use the given format string <i>FMT</i> to print output.</dd>
<dt><code>&#8211;gain (-G</code> )</dt>
<dd> Report net gain or loss for commodities that have a price history.</dd>
<dt><code>&#8211;generated</code></dt>
<dd> Include auto-generated postings (such as those from automated transactions) in the report, in cases where you normally wouldn&#8217;t want them.</dd>
<dt><code>&#8211;group-by </code><i>EXPR</i></dt>
<dd> Group transaction together in the <code>register</code> report. <i>EXPR</i> can be anything, although most common would be <i>payee</i> or <i>commodity</i> The Fn tag function is also useful here.</dd>
<dt><code>&#8211;group-title-format </code><i>FMT</i></dt>
<dd> Set the format for the headers that separate reports section of a grouped report. Only has effect with a &#8211;<code>-group-by </code><i>EXPR</i> register report.</dd>
<dt><code>&#8211;head </code><i>INT</i></dt>
<dd> Print the first <i>INT</i> entries. Opposite of &#8211;<code>-tail </code><i>INT</i> Alias for &#8211;<code>-first</code></dd>
<dt><code>&#8211;help</code></dt>
<dd> Print this man page.</dd>
<dt><code>&#8211;immediate</code></dt>
<dd> Evaluate calculations immediately rather than lazily.</dd>
<dt><code>&#8211;import </code><i>FILE</i></dt>
<dd> Import <i>FILE</i> as Python module.</dd>
<dt><code>&#8211;init-file </code><i>FILE (-</i><code>i</code> )</dt>
<dd> Read <i>FILE</i> before any other file. This file may not contain any postings, but it may contain option settings. To specify options in the init file, use the same syntax as the command-line, but put each option on its own line.</dd>
<dt><code>&#8211;inject </code><i>STR</i></dt>
<dd> Use <i>STR</i> amounts in calculations. In case you know what amount a transaction should be, but the actual transaction has the wrong value you can use metadata <i>STR</i> to specify the expected amount.</dd>
<dt><code>&#8211;input-date-format </code><i>DATEFMT</i></dt>
<dd> Specify the input date format for journal entries.</dd>
<dt><code>&#8211;invert</code></dt>
<dd> Change the sign of all reported values.</dd>
<dt><code>&#8211;last </code><i>INT</i></dt>
<dd> Report only the last <i>INT</i> entries. Opposite of &#8211;<code>-first </code><i>INT</i> Only useful on a register report. Alias for &#8211;<code>-tail</code></dd>
<dt><code>&#8211;leeway </code><i>INT (-</i><code>Z</code> )</dt>
<dd> Alias for &#8211;<code>-price-expr</code></dd>
<dt><code>&#8211;limit </code><i>EXPR (-</i><code>l</code> )</dt>
<dd> Limit postings in calculations.</dd>
<dt><code>&#8211;lot-dates</code></dt>
<dd> Report the date on which each commodity in a balance report was purchased.</dd>
<dt><code>&#8211;lot-notes</code></dt>
<dd> Report the tag attached to each commodity in a balance report.</dd>
<dt><code>&#8211;lot-prices</code></dt>
<dd> Report the price at which each commodity in a balance report was purchased.</dd>
<dt><code>&#8211;lots</code></dt>
<dd> Report the date and price at which each commodity was purchased in a balance report.</dd>
<dt><code>&#8211;lots-actual</code></dt>
<dd> Preserve the uniqueness of commodities so they aren&#8217;t merged during reporting without printing the lot annotations.</dd>
<dt><code>&#8211;market (-V</code> )</dt>
<dd> Use the latest market value for all commodities.</dd>
<dt><code>&#8211;master-account </code><i>STR</i></dt>
<dd> Prepend all account names with <i>STR</i></dd>
<dt><code>&#8211;meta </code><i>STR</i></dt>
<dd> In the register report, prepend the transaction with the value of the given tag <i>STR</i></dd>
<dt><code>&#8211;meta-width </code><i>INT</i></dt>
<dd> Specify the width of the Meta column used for the &#8211;<code>-meta </code><i>TAG</i> options.</dd>
<dt><code>&#8211;monthly (-M</code> )</dt>
<dd> Shorthand for &#8211;<code>-period </code><i>monthly</i></dd>
<dt><code>&#8211;no-aliases</code></dt>
<dd> Aliases are completely ignored.</dd>
<dt><code>&#8211;no-color</code></dt>
<dd> Suppress any color TTY output.</dd>
<dt><code>&#8211;no-pager</code></dt>
<dd> Disables the pager on TTY output.</dd>
<dt><code>&#8211;no-revalued</code></dt>
<dd> Stop from showing &lt;Revalued&gt; postings.</dd>
<dt><code>&#8211;no-rounding</code></dt>
<dd> Don&#8217;t output Qq Li &lt;Adjustment&gt; postings. Note that this will cause the running total to often not add up! Its main use is for &#8211;<code>-amount-data (-j</code> ) and &#8211;<code>-total-data (-J</code> ) reports.</dd>
<dt><code>&#8211;no-titles</code></dt>
<dd> Suppress the output of group titles.</dd>
<dt><code>&#8211;no-total</code></dt>
<dd> Suppress printing the final total line in a balance report.</dd>
<dt><code>&#8211;now </code><i>DATE</i></dt>
<dd> Use <i>DATE</i> as the current date. This affects the output when using &#8211;<code>-period</code> &#8211;<code>-begin</code> &#8211;<code>-end</code> or &#8211;<code>-current</code> to decide which dates lie in the past or future.</dd>
<dt><code>&#8211;only </code><i>EXPR</i></dt>
<dd> This is a postings predicate that applies after certain transforms have been executed, such as periodic gathering.</dd>
<dt><code>&#8211;options</code></dt>
<dd> Display the options in effect for this invocation, along with their values and the source of those values.</dd>
<dt><code>&#8211;output </code><i>FILE (-</i><code>o</code> )</dt>
<dd> Redirect the output of to <i>FILE</i></dd>
<dt><code>&#8211;pager </code><i>STR</i></dt>
<dd> Use <i>STR</i> as the pager program.</dd>
<dt><code>&#8211;payee</code></dt>
<dd> Sets a value expression for formatting the payee. In the <code>register</code> report this prevents the second entry from having a date and payee for each transaction.</dd>
<dt><code>&#8211;payee-width </code><i>INT</i></dt>
<dd> Set the number of columns dedicated to the payee in the register report to <i>INT</i></dd>
<dt><code>&#8211;pedantic</code></dt>
<dd> Accounts, tags or commodities not previously declared will cause errors.</dd>
<dt><code>&#8211;pending</code></dt>
<dd> Use only postings that are marked pending.</dd>
<dt><code>&#8211;percent (- ) </code></dt>
<dd> Calculate the percentage value of each account in a balance reports. Only works for account that have a single commodity.</dd>
<dt><code>&#8211;period </code><i>PERIOD (-</i><code>p</code> )</dt>
<dd> Define a period expression that sets the time period during which transactions are to be accounted. For a <code>register</code> report only the transactions that satisfy the period expression with be displayed. For a balance report only those transactions will be accounted in the final balances.</dd>
<dt><code>&#8211;period-sort</code></dt>
<dd> Sort the posting within transactions using the given value expression.</dd>
<dt><code>&#8211;permissive</code></dt>
<dd> Quiet balance assertions.</dd>
<dt><code>&#8211;pivot </code><i>TAG</i></dt>
<dd> Produce a balance pivot report Qq around the given <i>TAG</i></dd>
<dt><code>&#8211;plot-amount-format </code><i>FMT</i></dt>
<dd> Define the output format for an amount data plot.</dd>
<dt><code>&#8211;plot-total-format </code><i>FMT</i></dt>
<dd> Define the output format for a total data plot.</dd>
<dt><code>&#8211;prepend-format </code><i>FMT</i></dt>
<dd> Prepend <i>FMT</i> to every line of the output.</dd>
<dt><code>&#8211;prepend-width </code><i>INT</i></dt>
<dd> Reserve <i>INT</i> spaces at the beginning of each line of the output.</dd>
<dt><code>&#8211;price (-I</code> )</dt>
<dd> Use the price of the commodity purchase for performing calculations.</dd>
<dt><code>&#8211;price-db </code><i>FILE</i></dt>
<dd>
</dd><dt><code>&#8211;price-exp </code><i>STR (-</i><code>Z</code> )</dt>
<dd> Set the expected freshness of price quotes, in <i>INT</i> minutes. That is, if the last known quote for any commodity is older than this value, and if &#8211;<code>-download</code> is being used, then the Internet will be consulted again for a newer price. Otherwise, the old price is still considered to be fresh enough. Alias for &#8211;<code>-leeway</code></dd>
<dt><code>&#8211;prices-format </code><i>FMT</i></dt>
<dd> Set the format for the <code>prices</code> report.</dd>
<dt><code>&#8211;pricedb-format </code><i>FMT</i></dt>
<dd> Set the format expected for the historical price file.</dd>
<dt><code>&#8211;primary-date</code></dt>
<dd> Show primary dates for all calculations. Alias for &#8211;<code>-actual-dates</code></dd>
<dt><code>&#8211;quantity (-O</code> )</dt>
<dd> Report commodity totals (this is the default).</dd>
<dt><code>&#8211;quarterly</code></dt>
<dd> Shorthand for &#8211;<code>-period </code><i>quarterly</i></dd>
<dt><code>&#8211;raw</code></dt>
<dd> In the <code>print</code> report, show transactions using the exact same syntax as specified by the user in their data file. Don&#8217;t do any massaging or interpreting. Can be useful for minor cleanups, like just aligning amounts.</dd>
<dt><code>&#8211;real (-R</code> )</dt>
<dd> Account using only real transactions ignoring virtual and automatic transactions.</dd>
<dt><code>&#8211;recursive-aliases</code></dt>
<dd> Causes to try to expand aliases recursively, i.e. try to expand the result of an earlier expansion again, until no more expansions apply.</dd>
<dt><code>&#8211;register-format </code><i>FMT</i></dt>
<dd> Define the output format for the <code>register</code> report.</dd>
<dt><code>&#8211;related (-r</code> )</dt>
<dd> In a register report show the related account. This is the other <i>side</i> of the transaction.</dd>
<dt><code>&#8211;related-all</code></dt>
<dd> Show all postings in a transaction, similar to &#8211;<code>-related</code> but show both sides of each transaction.</dd>
<dt><code>&#8211;revalued</code></dt>
<dd> Report discrepancy in values for manual reports by inserting &lt;Revalued&gt; postings. This is implied when using the &#8211;<code>-exchange (-X</code> ) or &#8211;<code>-market (-V</code> ) option.</dd>
<dt><code>&#8211;revalued-only</code></dt>
<dd> Show only &lt;Revalued&gt; postings.</dd>
<dt><code>&#8211;revalued-total</code></dt>
<dd> Display the sum of the revalued postings as the running total, which serves to show unrealized capital in a gain/losses report.</dd>
<dt><code>&#8211;rich-data</code></dt>
<dd> When generating a ledger transaction from a CSV file using the <code>convert</code> command, add CSV, Imported, and UUID meta-data.</dd>
<dt><code>&#8211;seed </code><i>INT</i></dt>
<dd> Set the random seed to <i>INT</i> for the <code>generate</code> command. Used as part of development testing.</dd>
<dt><code>&#8211;script </code><i>FILE</i></dt>
<dd> Execute a script.</dd>
<dt><code>&#8211;sort </code><i>EXPR (-</i><code>S</code> )</dt>
<dd> Sort the register report based on the value expression <i>EXPR</i></dd>
<dt><code>&#8211;sort-xacts</code></dt>
<dd> Sort the posting within transactions using the given value expression.</dd>
<dt><code>&#8211;start-of-week </code><i>STR</i></dt>
<dd> Use <i>STR</i> as the particular day of the week to start when using the &#8211;<code>-weekly</code> option. <i>STR</i> can be day names, their abbreviations like Qq Mon , or the weekday number starting at 0 for Sunday.</dd>
<dt><code>&#8211;strict</code></dt>
<dd> Accounts, tags or commodities not previously declared will cause warnings.</dd>
<dt><code>&#8211;subtotal (-s</code> )</dt>
<dd> Report register as a single subtotal.</dd>
<dt><code>&#8211;tail </code><i>INT</i></dt>
<dd> Report only the last <i>INT</i> entries. Only useful on a register report. Alias for &#8211;<code>-last </code><i>INT</i></dd>
<dt><code>&#8211;time-colon</code></dt>
<dd> Display the value for commodities based on seconds as hours and minutes. Thus 8100s will be displayed as 2:15h instead of 2.25h.</dd>
<dt><code>&#8211;time-report</code></dt>
<dd> Add two columns to the <code>balance</code> report to show the earliest checkin and checkout times for timelog entries.</dd>
<dt><code>&#8211;total </code><i>EXPR (-</i><code>T</code> )</dt>
<dd> Define a value expression used to calculate the total in reports.</dd>
<dt><code>&#8211;total-data (-J</code> )</dt>
<dd> Show only dates and totals to format the output for plots.</dd>
<dt><code>&#8211;total-width </code><i>INT</i></dt>
<dd> Set the width of the total field in the register report.</dd>
<dt><code>&#8211;trace </code><i>INT</i></dt>
<dd> Enable tracing. The <i>INT</i> specifies the level of trace desired.</dd>
<dt><code>&#8211;truncate </code><i>STR</i></dt>
<dd> Indicates how truncation should happen when the contents of columns exceed their width. Valid arguments for <i>STR</i> are <i>leading</i> <i>middle</i> and <i>trailing</i> The default is smarter than any of these three, as it considers sub-names within the account name (that style is called Qq abbreviate ) .</dd>
<dt><code>&#8211;unbudgeted</code></dt>
<dd> Show only un-budgeted postings.</dd>
<dt><code>&#8211;uncleared (-U</code> )</dt>
<dd> Use only uncleared transactions in calculations and reports.</dd>
<dt><code>&#8211;unrealized</code></dt>
<dd> Show generated unrealized gain and loss accounts in the balance report.</dd>
<dt><code>&#8211;unrealized-gains</code></dt>
<dd> Allow the user to specify what account name should be used for unrealized gains. Defaults to <code>Equity:Unrealized Gains</code> Often set in one&#8217;s ~/.ledgerrc file to change the default.</dd>
<dt><code>&#8211;unrealized-losses</code></dt>
<dd> Allow the user to specify what account name should be used for unrealized losses. Defaults to <code>Equity:Unrealized Losses</code> Often set in one&#8217;s ~/.ledgerrc file to change the default.</dd>
<dt><code>&#8211;unround</code></dt>
<dd> Perform all calculations without rounding and display results to full precision.</dd>
<dt><code>&#8211;values</code></dt>
<dd> Show the values used by each tag when used in combination with the <code>tags</code> command.</dd>
<dt><code>&#8211;value-expr </code><i>EXPR</i></dt>
<dd> Set a global value expression annotation.</dd>
<dt><code>&#8211;verbose</code></dt>
<dd> Print detailed information on the execution of <code>.</code></dd>
<dt><code>&#8211;verify</code></dt>
<dd> Enable additional assertions during run-time. This causes a significant slowdown. When combined with &#8211;<code>-debug </code><i>CODE</i> will produce memory trace information.</dd>
<dt><code>&#8211;verify-memory</code></dt>
<dd> Verify that every constructed object is properly destructed. This is for debugging purposes only.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print version information and exit.</dd>
<dt><code>&#8211;weekly (-W</code> )</dt>
<dd> Shorthand for &#8211;<code>-period </code><i>weekly</i></dd>
<dt><code>&#8211;wide (-w</code> )</dt>
<dd> Assume 132 columns instead of the TTY width.</dd>
<dt><code>&#8211;yearly (-Y</code> )</dt>
<dd> Shorthand for &#8211;<code>-period </code><i>yearly</i></dd></dl>
<h2>PRE-COMMANDS</h2>
<p> Pre-commands are useful when you aren&#8217;t sure how a command or option will work. The difference between a pre-command and a regular command is that pre-commands ignore the journal data file completely, nor is the user&#8217;s init file read.</p>
<dl>
<dt><code>args / query</code></dt>
<dd> Evaluate the given arguments and report how interprets it against the following model transaction: </dd>
<blockquote>
<pre><code>
2004 / 05 / 27 Book Store;
This note applies to all postings. : SecondTag : Expenses : Books 20 BOOK @$10;
Metadata : Some Value;
Typed::$100 + $200; :ExampleTag:
    ;
Here follows a note describing the posting.Liabilities : MasterCard $ - 200.00
</code></pre>
</blockquote>
<dt><code>eval</code></dt>
<dd> Evaluate the given value expression against the model transaction.</dd>
<dt><code>format</code></dt>
<dd> Print details of how uses the given formatting description and apply it against a model transaction.</dd>
<dt><code>parse / expr</code></dt>
<dd> Print details of how uses the given value expression description and apply it against a model transaction.</dd>
<dt><code>generate</code></dt>
<dd> Randomly generates syntactically valid data from a seed. Used by the GenerateTests harness for development testing.</dd>
<dt><code>period</code></dt>
<dd> Evaluate the given period and report how interprets it.</dd>
<dt><code>template</code></dt>
<dd> Shows the insertion template that the <code>xact</code> command generates. This is a debugging command.</dd></dl>
<h2>QUERIES</h2>
<p> The syntax for reporting queries can get somewhat complex. It is a series of query terms with an implicit OR operator between them. The following terms are accepted:</p>
<dl>
<dt><i>regex</i></dt>
<dd> A bare string is taken as a regular expression matching the full account name. Thus, to report the current balance for all assets and liabilities, you would use: </dd>
<blockquote><p><tt>ledger bal asset liab</tt></p></blockquote>
<dt><code>payee </code><i>regex (</i><code>@ </code><i>regex</i> )</dt>
<dd> Query on the payee, rather than the account.</dd>
<dt><code>tag </code><i>regex (</i><code>% </code><i>regex</i> )</dt>
<dd>
</dd><dt><code>note </code><i>regex (</i><code>= </code><i>regex</i> )</dt>
<dd> Query on anything found in an item&#8217;s note.</dd>
<dt><code>code </code><i>regex (</i><code># </code><i>regex</i> )</dt>
<dd> Query on the xact&#8217;s optional code (which can be any string the user wishes).</dd>
<dt><i>term </i><code>and </code><i>term</i></dt>
<dd> Query terms are joined by an implicit OR operator. You can change this to AND by using the <code>and</code> keyword. For example, to show food expenditures occurring at Shakee&#8217;s Pizza, you could say: </dd>
<blockquote><p><tt></tt><code>ledger reg food and @Shakee</code> </p></blockquote>
<dt><i>term </i><code>or </code><i>term</i></dt>
<dd> When you wish to be more explicit, use the OR operator.</dd>
<dt><code>show</code></dt>
<dd>
</dd><dt><code>not </code><i>term</i></dt>
<dd> Reverse the logical meaning of the following term. This can be used with parentheses to great effect: </dd>
<blockquote><p><tt></tt><code>ledger reg food and @Shakee and not dining</code> </p></blockquote>
<dt><code>( </code><i>term </i><code>)</code></dt>
<dd> If you wish to mix OR and AND operators, it is often helpful to surround logical units with parentheses. <code>NOTE</code>: Because of the way some shells interpret parentheses, you should always escape them: </dd>
<blockquote><p><tt></tt><code>ledger bal \( assets or liab \) and not food</code> </p></blockquote>
</dl>
<h2>EXPRESSIONS</h2>
<dl>
<dt><code>Fn </code>abs value</dt>
<dd> Return the absolute value of the given <i>value</i></dd>
<dt><code>account</code></dt>
<dd> Return the posting&#8217;s account.</dd>
<dt><code>account_base</code></dt>
<dd> Return the base account, i.e. everything after the last account delimiter &#8216;:&#8217;.</dd>
<dt><code>actual</code></dt>
<dd> Return true if the transaction is real, i.e not a automated or virtual transaction, false otherwise.</dd>
<dt><code>amount</code></dt>
<dd> Return the amount of the posting.</dd>
<dt><code>amount_expr</code></dt>
<dd> Return the calculated amount of the posting according to the &#8211;<code>-amount</code> option.</dd>
<dt><code>Fn </code>ansify_if value color bool</dt>
<dd> Render the given <i>value</i> as a string, applying the proper ANSI escape codes to display it in the given <i>color</i> if <i>bool</i> is true. It typically checks the value of the option &#8211;<code>-color</code> for example: </dd>
<blockquote><p><tt></tt><code>ansify_if(amount, blue, options.color)</code> </p></blockquote>
<dt><code>beg_line</code></dt>
<dd> Line number where entry for posting begins.</dd>
<dt><code>beg_pos</code></dt>
<dd> Character position where entry for posting begins.</dd>
<dt><code>Fn </code>ceiling value</dt>
<dd> Return the next integer of <i>value</i> toward +infinity.</dd>
<dt><code>cleared</code></dt>
<dd> Return true if the posting was cleared, false otherwise.</dd>
<dt><code>code</code></dt>
<dd> Return the transaction code, the string between the parenthesis after the date.</dd>
<dt><code>Fn </code>commodity value</dt>
<dd> Return the commodity of <i>value</i> or the posting amount when <i>value</i> was not specified.</dd>
<dt><code>date</code></dt>
<dd> Return the date of the posting.</dd>
<dt><code>end_line</code></dt>
<dd> Line number where entry for posting ends.</dd>
<dt><code>end_pos</code></dt>
<dd> Character position where entry for posting ends.</dd>
<dt><code>Fn </code>floor value</dt>
<dd> Return the next integer of <i>value</i> toward -infinity.</dd>
<dt><code>filename</code></dt>
<dd> The name of the data file from whence the posting came.</dd>
<dt><code>Fn </code>format string</dt>
<dd> Evaluate <i>string</i> as format just like the &#8211;<code>-format</code> option.</dd>
<dt><code>Fn </code>format_date date format</dt>
<dd> Return the <i>date</i> as a string using <i>format</i> Refer to <a href="/docs/linux/man/3-strftime/">strftime</a>(3) for format string details.</dd>
<dt><code>Fn </code>format_datetime datetime format</dt>
<dd> Return the <i>datetime</i> as a string using <i>format</i> Refer to <a href="/docs/linux/man/3-strftime/">strftime</a>(3) for format string details.</dd>
<dt><code>Fn </code>get_at seq index</dt>
<dd> Return value at <i>index</i> from <i>seq</i> Used internally to construct different reports.</dd>
<dt><code>Fn </code>has_meta</dt>
<dd> Return true if the posting has metadata named <i>tag</i> false otherwise.</dd>
<dt><code>Fn </code>has_tag tag</dt>
<dd> Return true if the posting has metadata named <i>tag</i> false otherwise.</dd>
<dt><code>Fn </code>is_seq value</dt>
<dd> Return true if <i>value</i> is a sequence. Used internally.</dd>
<dt><code>Fn </code>join value</dt>
<dd> Replace all newlines in <i>value</i> with <code>
</code></dd>
<dt><code>Fn </code>justify value first_width latter_width right_justify colorize</dt>
<dd> Right or left justify the string representing <i>value</i> The width of the field in the first line is given by <i>first_width</i> For subsequent lines the width is given by <i>latter_width</i> If <i>latter_width</i> is -1, <i>first_width</i> is used for all lines. If <i>right_justify</i> is true then the field is right justified within the width of the field. If it is false, then the field is left justified and padded to the full width of the field. If <i>colorize</i> is true, then ledger will honor color settings.</dd>
<dt><code>Fn </code>market value datetime</dt>
<dd> Return the price of <i>value</i> at <i>datetime</i> Note that <i>datetime</i> must be surrounded by brackets in order to be parsed correctly, e.g. Bq 2012/03/23 .</dd>
<dt><code>Fn </code>meta</dt>
<dd> Return the value of metadata named <i>name</i></dd>
<dt><code>note</code></dt>
<dd> Return the note for the posting.</dd>
<dt><code>now</code></dt>
<dd> Return the current datetime.</dd>
<dt><code>options</code></dt>
<dd> A variable that allows access to the values of the given command-line options using the long option names, e.g. to see whether &#8211;<code>-daily (-D</code> ) was given use <code>option.daily</code></dd>
<dt><code>payee</code></dt>
<dd> Return the payee of the posting.</dd>
<dt><code>Fn </code>percent value_a value_b</dt>
<dd> Return the percentage of <i>value_a</i> in relation to <i>value_b</i> (used as 100%).</dd>
<dt><code>pending</code></dt>
<dd> Return true if the posting is marked as pending, false otherwise.</dd>
<dt><code>Fn </code>percent value_a value_b</dt>
<dd> Return the percentage of <i>value_a</i> in relation to <i>value_b</i></dd>
<dt><code>Fn </code>print value</dt>
<dd> Print <i>value</i> to stdout. Used internally for debugging.</dd>
<dt><code>Fn </code>quantity value</dt>
<dd> Return the quantity of <i>value</i> for values that have a per-unit cost.</dd>
<dt><code>Fn </code>quoted expression</dt>
<dd> Surround <i>expression</i> with double-quotes.</dd>
<dt><code>real</code></dt>
<dd> Return true if the transaction is real, i.e not a automated or virtual transaction, false otherwise.</dd>
<dt><code>Fn </code>roundto value n</dt>
<dd> Return <i>value</i> rounded to <i>n</i> digits. Does not affect formatting.</dd>
<dt><code>should_bold</code></dt>
<dd> Return true if expression given to &#8211;<code>-bold-if</code> evaluates to true. Internal use only!</dd>
<dt><code>Fn </code>scrub value</dt>
<dd> Clean <i>value</i> using various transformations such as round, stripping value annotations, and more.</dd>
<dt><code>Fn </code>strip value</dt>
<dd> Strip value annotation from <i>value</i></dd>
<dt><code>Fn </code>tag name</dt>
<dd> Return the value of tag named <i>name</i></dd>
<dt><code>Fn </code>to_amount value</dt>
<dd> Convert <i>value</i> to an amount. Internal use only!</dd>
<dt><code>Fn </code>to_balance value</dt>
<dd> Convert <i>value</i> to a balance. Internal use only!</dd>
<dt><code>Fn </code>to_boolean value</dt>
<dd> Convert <i>value</i> to a boolean. Internal use only!</dd>
<dt><code>Fn </code>to_date value</dt>
<dd> Convert <i>value</i> to a date. Internal use only!</dd>
<dt><code>Fn </code>to_datetime value</dt>
<dd> Convert <i>value</i> to a datetime. Internal use only!</dd>
<dt><code>Fn </code>to_int value</dt>
<dd> Return the integer value for <i>value</i></dd>
<dt><code>Fn </code>to_mask value</dt>
<dd> Convert <i>value</i> to a mask. Internal use only!</dd>
<dt><code>Fn </code>to_sequence value</dt>
<dd> Convert <i>value</i> to a sequence. Internal use only!</dd>
<dt><code>Fn </code>to_string value</dt>
<dd> Convert <i>value</i> to a character string.</dd>
<dt><code>today</code></dt>
<dd> Return today&#8217;s date.</dd>
<dt><code>total</code></dt>
<dd> Return the total of the posting.</dd>
<dt><code>total_expr</code></dt>
<dd> Return the calculated total of the posting according to the &#8211;<code>-total</code> option.</dd>
<dt><code>Fn </code>trim value</dt>
<dd> Trim leading and trailing whitespace from <i>value</i></dd>
<dt><code>Fn </code>truncated string total_len account_len</dt>
<dd> Truncate <i>string</i> to <i>total_len</i> ensuring that each account is at least <i>account_len</i> long.</dd>
<dt><code>virtual</code></dt>
<dd> Return true if the transaction is virtual, e.g automated, false otherwise.</dd></dl>
<h2>DEBUG COMMANDS</h2>
<p> In addition to the regular reporting commands, also accepts several debug commands:</p>
<dl>
<dt><code>args </code>[<i>report-query </i>]</dt>
<dd> Display complete analysis of how interpreted the given <i>report-query</i> Useful if you want to understand how report queries are translated into value expressions.</dd>
<dt><code>eval </code>[<i>value-expression </i>]</dt>
<dd> Evaluate the given <i>value-expression</i> and prints the result. For more on value expressions, see the section Sx EXPRESSIONS .</dd>
<dt><code>format </code>[<i>format-string </i>]</dt>
<dd> Display an analysis of how <i>format-string</i> was parsed, and what it would look like applied to a sample transaction. For more on format strings, see the section Sx FORMATS .</dd>
<dt><code>generate</code></dt>
<dd> Generate 50 randomly composed yet valid transactions.</dd>
<dt><code>parse </code>[<i>value-expression </i>]</dt>
<dd> Parse the given <i>value-expression</i> and display an analysis of the expression tree and its evaluated value. For more on value expressions, see the section Sx EXPRESSIONS .</dd>
<dt><code>python </code>[<i>file </i>]</dt>
<dd> Invoke a Python interpreter to read the given <i>file</i> What is special about this is that the module is builtin, not read from disk, so it doesn&#8217;t require to be installed anywhere, or the shared library variants to be built.</dd>
<dt><code>reload</code></dt>
<dd> Reload all data files for the current session immediately. Can only be used in the <code>REPL</code></dd>
<dt><code>template </code>[<i>draft-template </i>]</dt>
<dd> Display information about how <i>draft-template</i> was parsed. See the section on Sx DRAFTS .</dd></dl>
<h2>ENVIRONMENT</h2>
<p> Every option to may be set using an environment variable if the option has a long name. For example setting the environment variable <code>LEDGER_DATE_FORMAT=%d.%m.%Y&#8217;</code> will have the same effect as specifying &#8211;<code>-date-format </code><i>&#8216;%d.%m.%Y&#8217;</i> on the command-line. Options on the command-line always take precedence over environment variable settings, however.</p>
<h2>FILES</h2>
<dl>
<dt><code>~/.ledgerrc </code></dt>
<dd> Your personal initializations.</dd></dl>
<h2>SEE ALSO</h2>
<p> beancount(1), hledger(1)</p>
<h2>AUTHORS</h2>
<p> An John Wiegley Aq johnw [at] newartisans.com </p>
