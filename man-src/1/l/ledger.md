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
<h2>SYNOPSIS</h2>
<p> [<i>command</i> ] [<i>options</i> ] [<i>arguments</i> ]</p>
<h2>DESCRIPTION</h2>
<p> is a command-line accounting tool based on the power and completeness of double-entry accounting. It is only a reporting tool, which means it never modifies your data files, but it does offer a large selection of reports, and different ways to customize them to your needs.</p>
<h2>COMMANDS</h2>
<p> accepts several top-level commands, each of which generates a different kind of basic report. Most of them accept a <i>report-query</i> argument, in order to determine what should be reported. To understand the syntax of a <i>report-query</i> see the section on Sx QUERIES . In its most basic form, simply specifying one or more strings produces a report for all accounts containing those strings. </p>
<p> If no command is given, enters a <code>REPL</code> or command loop, allowing several commands to be executed on the same dataset without reparsing. </p>
<p> The following is a complete list of accepted reporting commands:</p>
<dl>
<dt><code>accounts </code>[<i>report-query </i>]</p>
<dd> List all accounts for postings that match the <i>report-query</i></dl>
<dl>
<dt><code>balance </code>[<i>report-query </i>]</p>
<dd> Print a balance report showing totals for postings that match <i>report-query</i> and aggregate totals for parents of those accounts. Options most commonly used with this command are:</p>
<dl>
<dt><code>&#8211;basis (-B</code> )</p>
<dd> Report in terms of cost basis, not amount or value. This is the only form of report which is guaranteed to always balance to zero, when no <i>report-query</i> is specified. Only show totals for the top-most accounts.</p>
<dt><code>&#8211;empty (-E</code> )</p>
<dd> Show accounts whose total is zero.</p>
<dt><code>&#8211;flat</code></p>
<dd> Rather than display a hierarchical tree, flatten the report to show subtotals for only accounts matching <i>report-query</i></p>
<dt><code>&#8211;no-total</code></p>
<dd> Suppress the summary total shown at the bottom of the report.</dl>
<p> The synonyms <code>bal</code> and <code>b</code> are also accepted.</p>
<dt><code>budget </code>[<i>report-query </i>]</p>
<dd> A special balance report which includes three extra columns: the amount budgeted during the reporting period, how spending differed from the budget, and the percentage of budget spent (exceeds 100% if you go over budget). Note that budgeting requires one or more Do periodic transactions Dc to be defined in your data file(s). See the manual for more information.</p>
<dt><code>cleared </code>[<i>report-query </i>]</p>
<dd> A special balance report which adds two extra columns: the cleared balance for each account, and the date of the most recent cleared posting in that account. For this accounting to be meaningful, the cleared flag must be set on at least one posting. See the manual for more information.</p>
<dt><code>commodities </code>[<i>report-query </i>]</p>
<dd> List all commodities for postings matching the <i>report-query</i></p>
<dt><code>convert</code></p>
<dd> Reads data from a CSV (comma-separated values) file and generates transactions.</p>
<dt><code>csv </code>[<i>report-query </i>]</p>
<dd> Report of postings matching the <i>report-query</i> in CSV format (comma-separated values). Useful for exporting data to a spreadsheet for further analysis or charting.</p>
<dt><code>entry </code>[<i>entry-template </i>]</p>
<dd> Generate and display a new, properly formatted transaction by comparing the <i>entry-template</i> to the transactions in your data file(s). For more information on draft templates and using this command to quickly create new transactions, see the section Sx ENTRIES . </p>
<p> The synonym <code>xact</code> is also accepted.</p>
<dt><code>emacs </code>[<i>query </i>]</p>
<dd> Output posting and transaction data in a format readily consumed by the Emacs editor, in a series of Lisp forms. This is used by the ledger.el Emacs mode to process reporting data from <code>.</code></p>
<dt><code>equity </code>[<i>report-query </i>]</p>
<dd> Print a transaction with a series of postings that balance current totals for accounts matching the <i>report-query</i> in a special account called <code>Equity:Opening Balances</code> The purpose of this report is to close the books for a prior year, while using these equity postings to carry forward those balances.</p>
<dt><code>org</code></p>
<dd> Produce a journal file suitable for use in the Emacs org mode.</p>
<dt><code>payees </code>[<i>report-query </i>]</p>
<dd> List all payees for postings matching the <i>report-query</i></p>
<dt><code>pricemap</code></p>
<dd> Produce a file which can be used to generate a graph with graphviz showing the relationship of commodities in the file.</p>
<dt><code>prices </code>[<i>report-query </i>]</p>
<dd> Report prices for all commodities in postings matching the <i>report-query</i> The prices are reported with the granularity of a single day.</p>
<dt><code>pricedb </code>[<i>report-query </i>]</p>
<dd> Report prices for all commodities in postings matching the <i>report-query</i> Prices are reported down to the second, using the same format as the ~/.pricedb file.</p>
<dt><code>print </code>[<i>report-query </i>]</p>
<dd> Print out the full transactions of any matching postings using the same format as they would appear in a data file. This can be used to extract subsets from a file to transfer to other files.</p>
<dt><code>push </code>[<i>options </i>]</p>
<dd> In the <code>REPL</code> push a set of command-line <i>options</i> so that they will apply to all subsequent reports.</p>
<dt><code>pop</code></p>
<dd> In the <code>REPL</code> pop any option settings that have been <code>push</code> ed.</p>
<dt><code>register </code>[<i>report-query </i>]</p>
<dd> List all postings matching the <i>report-query</i> This is one of the most common commands, and can be used to provide a variety of useful reports. Options most commonly used with this command are: </p>
<dl>
<dt><code>&#8211;average (-A</code> )</p>
<dd> Show the running average, rather than a running total.</p>
<dt><code>&#8211;current (-c</code> )</p>
<dd> Don&#8217;t show postings beyond the present day.</p>
<dt><code>&#8211;exchange </code><i>commodity (-</i><code>X</code> )</p>
<dd> Render all values in the given <i>commodity</i> if a price conversion rate can be determined. Rates are always displayed relative to the date of the posting they are calculated for. This means a <code>register</code> report is a historical value report. For current values, it may be preferable to use the <code>balance</code> report.</p>
<dt><code>&#8211;gain (-G</code> )</p>
<dd> Show any gains (or losses) in commodity values over time.</p>
<dt><code>&#8211;head </code><i>number</i></p>
<dd> Only show the top <i>number</i> postings.</p>
<dt><code>&#8211;historical (-H</code> )</p>
<dd> Value commodities at the time of their acquisition.</p>
<dt><code>&#8211;invert</code></p>
<dd> Invert the value of amounts shown.</p>
<dt><code>&#8211;market (-V</code> )</p>
<dd> Show current market values for all amounts. This is determined in a somewhat magical fashion. It is probably more straightforward to use &#8211;<code>-exchange</code> option.</p>
<dt><code>&#8211;period </code><i>time-period (-</i><code>p</code> )</p>
<dd> Show postings only for the given <i>time-period</i></p>
<dt><code>&#8211;related (-r</code> )</p>
<dd> Show postings that are related to those that would have been shown. It has the effect of displaying the Qq other side of the postings.</p>
<dt><code>&#8211;sort </code><i>value-expression (-</i><code>S</code> )</p>
<dd> Sort postings by evaluating the given <i>value-expression</i> Note that a comma-separated list of expressions is allowed, in which case each sorting term is used in order to determine the final ordering. For example, to search by date and then amount, one would use: </p>
<blockquote><p><tt>ledger reg --sort 'date, amount'</tt></p></blockquote>
<dt><code>&#8211;tail </code><i>number</i></p>
<dd> Only show the last <i>number</i> postings.</p>
<dt><code>&#8211;uncleared (-U</code> )</p>
<dd> Only show uncleared (i.e., recent) postings.</dl>
<p> There are also several grouping options that can be useful: </p>
<dl>
<dt><code>&#8211;by-payee (-P</code> )</p>
<dd> Group postings by common payee names.</p>
<dt><code>&#8211;daily (-D</code> )</p>
<dd> Group postings by day.</p>
<dt><code>&#8211;weekly (-W</code> )</p>
<dd> Group postings by week (starting on Sundays).</p>
<dt><code>&#8211;start-of-week </code><i>day</i></p>
<dd> Set the start of each report grouped by week to the given <i>day</i></p>
<dt><code>&#8211;monthly (-M</code> )</p>
<dd> Group postings by month.</p>
<dt><code>&#8211;quarterly</code></p>
<dd> Group postings by fiscal quarter.</p>
<dt><code>&#8211;yearly (-Y</code> )</p>
<dd> Group postings by year.</p>
<dt><code>&#8211;days-of-week</code></p>
<dd> Group postings by the day of the week on which they took place.</p>
<dt><code>&#8211;subtotal (-s</code> )</p>
<dd> Group all postings together. This is very similar to the totals shown by the <code>balance</code> report.</dl>
<p> The synonyms <code>reg</code> and <code>r</code> are also accepted.</p>
<dt><code>server</code></p>
<dd> This command requires that Python support be active. If so, it starts up an <code>HTTP</code> server listening for requests on port 9000. This provides an alternate interface to creating and viewing reports. Note that this is very much a work-in-progress, and will not be fully functional until a later version.</p>
<dt><code>select </code>[<i>sql-query </i>]</p>
<dd> List all postings matching the <i>sql-query</i> This command allows to generate SQL-like queries, e.g.: </p>
<blockquote><p><tt></tt><code>ledger select date,amount from posts where account=~/Income/</code> </p></blockquote>
<dt><code>source</code></p>
<dd> Parse a journal file and checks it for errors. will return success if no errors are found.</p>
<dt><code>stats </code>[<i>report-query </i>]</p>
<dd> Provide summary information about all the postings matching <i>report-query</i> It provides information such as: </p>
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
<dt><code>xml </code>[<i>report-query </i>]</p>
<dd> Output data relating to the current report in <code>XML</code> format. It includes all accounts and commodities involved in the report, plus the postings and the transactions they are contained in. See the manual for more information.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;abbrev-len </code><i>INT</i></p>
<dd> Set the minimum length an account can be abbreviated to if it doesn&#8217;t fit inside the <code>account-width</code> If <i>INT</i> is zero, then the account name will be truncated on the right. If <i>INT</i> is greater than <code>account-width</code> then the account will be truncated on the left, with no shortening of the account names in order to fit into the desired width.</p>
<dt><code>&#8211;account </code><i>EXPR</i></p>
<dd> Prepend <i>EXPR</i> to all accounts reported. That is, the option &#8211;<code>-account </code><i>&quot;&#8217;Personal&#8217;&quot;</i> would tack <i>Personal:</i> and &#8211;<code>-account </code><i>&quot;tag(&#8216;VAT&#8217;)&quot;</i> would tack the value of the VAT tag to the beginning of every account reported in a <code>balance</code> or <code>register</code> report.</p>
<dt><code>&#8211;account-width </code><i>INT</i></p>
<dd> Set the width of the account column in the <code>register</code> report to <i>INT</i> characters.</p>
<dt><code>&#8211;actual (-L</code> )</p>
<dd> Report only real transactions, with no automated or virtual transactions used.</p>
<dt><code>&#8211;add-budget</code></p>
<dd> Show only un-budgeted postings.</p>
<dt><code>&#8211;amount </code><i>EXPR (-</i><code>t</code> )</p>
<dd> Apply the given value expression to the posting amount. Using &#8211;<code>-amount </code><i>EXPR</i> you can apply an arbitrary transformation to the postings.</p>
<dt><code>&#8211;amount-data (-j</code> )</p>
<dd> On a register report print only the dates and amount of postings. Useful for graphing and spreadsheet applications.</p>
<dt><code>&#8211;amount-width </code><i>INT</i></p>
<dd> Set the width in characters of the amount column in the <code>register</code> report.</p>
<dt><code>&#8211;anon</code></p>
<dd> Anonymize registry output, mostly for sending in bug reports.</p>
<dt><code>&#8211;ansi</code></p>
<dd> Use color if the terminal supports it. Alias for &#8211;<code>-color</code></p>
<dt><code>&#8211;args-only</code></p>
<dd> Ignore init files and environment variables for the run.</p>
<dt><code>&#8211;auto-match</code></p>
<dd> When generating a ledger transaction from a CSV file using the <code>convert</code> command, automatically match an account from the Ledger journal.</p>
<dt><code>&#8211;aux-date</code></p>
<dd> Show auxiliary dates for all calculations. Alias for &#8211;<code>-effective</code></p>
<dt><code>&#8211;average (-A</code> )</p>
<dd> Print average values over the number of transactions instead of running totals.</p>
<dt><code>&#8211;balance-format </code><i>FMT</i></p>
<dd> Specify the format to use for the <code>balance</code> report.</p>
<dt><code>&#8211;base</code></p>
<dd> Reduce convertible commodities down the bottom of the conversion, e.g. display time in seconds.</p>
<dt><code>&#8211;basis (-B</code> )</p>
<dd> Report the cost basis on all posting. Alias for &#8211;<code>-cost</code></p>
<dt><code>&#8211;begin </code><i>DATE (-</i><code>b</code> )</p>
<dd> Specify the start <i>DATE</i> of all calculations. Transactions before that date will be ignored.</p>
<dt><code>&#8211;bold-if </code><i>EXPR</i></p>
<dd> Print the entire line in bold if the given value expression is true.</p>
<dt><code>&#8211;budget</code></p>
<dd> Only display budgeted items. In a <code>register</code> report this displays transaction in the budget, in a balance report this displays accounts in the budget.</p>
<dt><code>&#8211;budget-format </code><i>FMT</i></p>
<dd> Specify the format to use for the <code>budget</code> report.</p>
<dt><code>&#8211;by-payee (-P</code> )</p>
<dd> Group postings in the register report by common payee names.</p>
<dt><code>&#8211;check-payees</code></p>
<dd> Enable strict and pedantic checking for payees as well as accounts, commodities and tags.</p>
<dt><code>&#8211;cleared (-C</code> )</p>
<dd> Display only cleared postings.</p>
<dt><code>&#8211;cleared-format </code><i>FMT</i></p>
<dd> Specify the format to use for the <code>cleared</code> report</p>
<dt><code>&#8211;collapse (-n</code> )</p>
<dd> Print only the top level accounts.</p>
<dt><code>&#8211;collapse-if-zero</code></p>
<dd> Collapse the account display only if it has a zero balance.</p>
<dt><code>&#8211;color</code></p>
<dd> Use color if the terminal supports it. Alias for &#8211;<code>-ansi</code></p>
<dt><code>&#8211;columns </code><i>INT</i></p>
<dd> Make the <code>register</code> report <i>INT</i> characters wide. By default will use all available columns in your terminal.</p>
<dt><code>&#8211;cost</code></p>
<dd> Report the cost basis on all posting. Alias for &#8211;<code>-basis</code></p>
<dt><code>&#8211;count</code></p>
<dd> Direct to report the number of items when appended to the <code>commodities</code> <code>accounts</code> or <code>payees</code> commands.</p>
<dt><code>&#8211;csv-format </code><i>FMT</i></p>
<dd> Format <code>csv</code> report according to <i>FMT</i></p>
<dt><code>&#8211;current (-c</code> )</p>
<dd> Shorthand for &#8211;<code>-limit </code><i>&#8216;date &lt;= today&#8217;</i></p>
<dt><code>&#8211;daily (-D</code> )</p>
<dd> Shorthand for &#8211;<code>-period </code><i>daily</i></p>
<dt><code>&#8211;date </code><i>EXPR</i></p>
<dd> Transform the date of the transaction using <i>EXPR</i></p>
<dt><code>&#8211;date-format </code><i>DATEFMT (-</i><code>y</code> )</p>
<dd> Print dates using <i>DATEFMT</i> Refer to <a href="/docs/linux/man/3-strftime/">strftime</a>(3) for details on the format string syntax.</p>
<dt><code>&#8211;datetime-format </code><i>DATETIMEFMT</i></p>
<dd> Print datetimes using <i>DATETIMEFMT</i> Refer to <a href="/docs/linux/man/3-strftime/">strftime</a>(3) for details on the format string syntax.</p>
<dt><code>&#8211;date-width </code><i>INT</i></p>
<dd> Specify the width, in characters, of the date column in the <code>register</code> report.</p>
<dt><code>&#8211;day-break</code></p>
<dd> Break up <code>register</code> report of timelog entries that span multiple days by day.</p>
<dt><code>&#8211;days-of-week</code></p>
<dd> Group transactions by the days of the week. Alias for &#8211;<code>-dow</code></p>
<dt><code>&#8211;dc</code></p>
<dd> Display register or balance in debit/credit format If you use &#8211;<code>-dc</code> with either the <code>register</code> or <code>balance</code> commands, you will now get separate columns for debits and credits.</p>
<dt><code>&#8211;debug </code><i>STR</i></p>
<dd> If has been built with debug options this will provide extra data during the run.</p>
<dt><code>&#8211;decimal-comma</code></p>
<dd> Direct to parse journals using the European standard comma as decimal separator, vice a period.</p>
<dt><code>&#8211;depth </code><i>INT</i></p>
<dd> Limit the depth of the account tree. In a balance report, for example, &#8211;<code>-depth </code><i>2</i> will print balances only for accounts with two levels, i.e. <code>Expenses:Entertainment</code> but not <code>Expenses:Entertainment:Dining</code> This is a display predicate, which means it only affects display, not the total calculations.</p>
<dt><code>&#8211;detail</code></p>
<dd> Related to <code>convert</code> command. Synonym to &#8211;<code>-rich-data</code> option.</p>
<dt><code>&#8211;deviation</code></p>
<dd> Report each posting&#8217;s deviation from the average. It is only meaningful in the <code>register and prices</code> reports.</p>
<dt><code>&#8211;display </code><i>EXPR (-</i><code>d</code> )</p>
<dd> Display lines that satisfy the expression <i>EXPR</i></p>
<dt><code>&#8211;display-amount </code><i>EXPR</i></p>
<dd> Apply a transformation to the <i>displayed</i> amount. This occurs after calculations occur.</p>
<dt><code>&#8211;display-total </code><i>EXPR</i></p>
<dd> Apply a transformation to the <i>displayed</i> total. This occurs after calculations occur.</p>
<dt><code>&#8211;dow</code></p>
<dd> Group transactions by the days of the week. Alias for &#8211;<code>-days-of-week</code></p>
<dt><code>&#8211;download</code></p>
<dd> Cause quotes to be automagically downloaded, as needed, by running a script named <i>getquote</i> and expecting that script to return a value understood by <code>.</code> A sample implementation of a <i>getquote</i> script, implemented in Perl, is provided in the distribution. Downloaded quote price are then appended to the price database, usually specified using the environment variable <code>LEDGER_PRICE_DB</code></p>
<dt><code>&#8211;effective</code></p>
<dd> Show auxiliary dates for all calculations. Alias for &#8211;<code>-aux-date</code></p>
<dt><code>&#8211;empty (-E</code> )</p>
<dd> Include empty accounts in report.</p>
<dt><code>&#8211;end </code><i>DATE (-</i><code>e</code> )</p>
<dd> Constrain the report so that transactions on or after <i>DATE</i> are not considered.</p>
<dt><code>&#8211;equity</code></p>
<dd> Related to the <code>equity</code> command. Gives current account balances in the form of a register report.</p>
<dt><code>&#8211;exact</code></p>
<dd> Report beginning and ending of periods by the date of the first and last posting occurring in that period.</p>
<dt><code>&#8211;exchange </code><i>COMMODITY </i>[, <i>COMMODITY, &#8230; (-</i><code>X</code> ) ]</p>
<dd> Display values in terms of the given <i>COMMODITY</i> The latest available price is used.</p>
<dt><code>&#8211;explicit</code></p>
<dd> Direct to require pre-declarations for entities (such as accounts, commodities and tags) rather than taking entities from cleared transactions as defined.</p>
<dt><code>&#8211;file </code><i>FILE</i></p>
<dd> Read journal data from <i>FILE</i></p>
<dt><code>&#8211;first </code><i>INT</i></p>
<dd> Print the first <i>INT</i> entries. Opposite of &#8211;<code>-last </code><i>INT</i> Alias for &#8211;<code>-head</code></p>
<dt><code>&#8211;flat</code></p>
<dd> Force the full names of accounts to be used in the balance report. The balance report will not use an indented tree.</p>
<dt><code>&#8211;force-color</code></p>
<dd> Output TTY color codes even if the TTY doesn&#8217;t support them. Useful for TTYs that don&#8217;t advertise their capabilities correctly.</p>
<dt><code>&#8211;force-pager</code></p>
<dd> Force to paginate its output.</p>
<dt><code>&#8211;forecast-while </code><i>EXPR</i></p>
<dd> Continue forecasting while <i>VEXPR</i> is true. Alias for &#8211;<code>-forecast</code></p>
<dt><code>&#8211;forecast-years </code><i>INT</i></p>
<dd> Forecast at most <i>INT</i> years into the future.</p>
<dt><code>&#8211;format </code><i>FMT (-</i><code>F</code> )</p>
<dd> Use the given format string <i>FMT</i> to print output.</p>
<dt><code>&#8211;gain (-G</code> )</p>
<dd> Report net gain or loss for commodities that have a price history.</p>
<dt><code>&#8211;generated</code></p>
<dd> Include auto-generated postings (such as those from automated transactions) in the report, in cases where you normally wouldn&#8217;t want them.</p>
<dt><code>&#8211;group-by </code><i>EXPR</i></p>
<dd> Group transaction together in the <code>register</code> report. <i>EXPR</i> can be anything, although most common would be <i>payee</i> or <i>commodity</i> The Fn tag function is also useful here.</p>
<dt><code>&#8211;group-title-format </code><i>FMT</i></p>
<dd> Set the format for the headers that separate reports section of a grouped report. Only has effect with a &#8211;<code>-group-by </code><i>EXPR</i> register report.</p>
<dt><code>&#8211;head </code><i>INT</i></p>
<dd> Print the first <i>INT</i> entries. Opposite of &#8211;<code>-tail </code><i>INT</i> Alias for &#8211;<code>-first</code></p>
<dt><code>&#8211;help</code></p>
<dd> Print this man page.</p>
<dt><code>&#8211;immediate</code></p>
<dd> Evaluate calculations immediately rather than lazily.</p>
<dt><code>&#8211;import </code><i>FILE</i></p>
<dd> Import <i>FILE</i> as Python module.</p>
<dt><code>&#8211;init-file </code><i>FILE (-</i><code>i</code> )</p>
<dd> Read <i>FILE</i> before any other file. This file may not contain any postings, but it may contain option settings. To specify options in the init file, use the same syntax as the command-line, but put each option on its own line.</p>
<dt><code>&#8211;inject </code><i>STR</i></p>
<dd> Use <i>STR</i> amounts in calculations. In case you know what amount a transaction should be, but the actual transaction has the wrong value you can use metadata <i>STR</i> to specify the expected amount.</p>
<dt><code>&#8211;input-date-format </code><i>DATEFMT</i></p>
<dd> Specify the input date format for journal entries.</p>
<dt><code>&#8211;invert</code></p>
<dd> Change the sign of all reported values.</p>
<dt><code>&#8211;last </code><i>INT</i></p>
<dd> Report only the last <i>INT</i> entries. Opposite of &#8211;<code>-first </code><i>INT</i> Only useful on a register report. Alias for &#8211;<code>-tail</code></p>
<dt><code>&#8211;leeway </code><i>INT (-</i><code>Z</code> )</p>
<dd> Alias for &#8211;<code>-price-expr</code></p>
<dt><code>&#8211;limit </code><i>EXPR (-</i><code>l</code> )</p>
<dd> Limit postings in calculations.</p>
<dt><code>&#8211;lot-dates</code></p>
<dd> Report the date on which each commodity in a balance report was purchased.</p>
<dt><code>&#8211;lot-notes</code></p>
<dd> Report the tag attached to each commodity in a balance report.</p>
<dt><code>&#8211;lot-prices</code></p>
<dd> Report the price at which each commodity in a balance report was purchased.</p>
<dt><code>&#8211;lots</code></p>
<dd> Report the date and price at which each commodity was purchased in a balance report.</p>
<dt><code>&#8211;lots-actual</code></p>
<dd> Preserve the uniqueness of commodities so they aren&#8217;t merged during reporting without printing the lot annotations.</p>
<dt><code>&#8211;market (-V</code> )</p>
<dd> Use the latest market value for all commodities.</p>
<dt><code>&#8211;master-account </code><i>STR</i></p>
<dd> Prepend all account names with <i>STR</i></p>
<dt><code>&#8211;meta </code><i>STR</i></p>
<dd> In the register report, prepend the transaction with the value of the given tag <i>STR</i></p>
<dt><code>&#8211;meta-width </code><i>INT</i></p>
<dd> Specify the width of the Meta column used for the &#8211;<code>-meta </code><i>TAG</i> options.</p>
<dt><code>&#8211;monthly (-M</code> )</p>
<dd> Shorthand for &#8211;<code>-period </code><i>monthly</i></p>
<dt><code>&#8211;no-aliases</code></p>
<dd> Aliases are completely ignored.</p>
<dt><code>&#8211;no-color</code></p>
<dd> Suppress any color TTY output.</p>
<dt><code>&#8211;no-pager</code></p>
<dd> Disables the pager on TTY output.</p>
<dt><code>&#8211;no-revalued</code></p>
<dd> Stop from showing &lt;Revalued&gt; postings.</p>
<dt><code>&#8211;no-rounding</code></p>
<dd> Don&#8217;t output Qq Li &lt;Adjustment&gt; postings. Note that this will cause the running total to often not add up! Its main use is for &#8211;<code>-amount-data (-j</code> ) and &#8211;<code>-total-data (-J</code> ) reports.</p>
<dt><code>&#8211;no-titles</code></p>
<dd> Suppress the output of group titles.</p>
<dt><code>&#8211;no-total</code></p>
<dd> Suppress printing the final total line in a balance report.</p>
<dt><code>&#8211;now </code><i>DATE</i></p>
<dd> Use <i>DATE</i> as the current date. This affects the output when using &#8211;<code>-period</code> &#8211;<code>-begin</code> &#8211;<code>-end</code> or &#8211;<code>-current</code> to decide which dates lie in the past or future.</p>
<dt><code>&#8211;only </code><i>EXPR</i></p>
<dd> This is a postings predicate that applies after certain transforms have been executed, such as periodic gathering.</p>
<dt><code>&#8211;options</code></p>
<dd> Display the options in effect for this invocation, along with their values and the source of those values.</p>
<dt><code>&#8211;output </code><i>FILE (-</i><code>o</code> )</p>
<dd> Redirect the output of to <i>FILE</i></p>
<dt><code>&#8211;pager </code><i>STR</i></p>
<dd> Use <i>STR</i> as the pager program.</p>
<dt><code>&#8211;payee</code></p>
<dd> Sets a value expression for formatting the payee. In the <code>register</code> report this prevents the second entry from having a date and payee for each transaction.</p>
<dt><code>&#8211;payee-width </code><i>INT</i></p>
<dd> Set the number of columns dedicated to the payee in the register report to <i>INT</i></p>
<dt><code>&#8211;pedantic</code></p>
<dd> Accounts, tags or commodities not previously declared will cause errors.</p>
<dt><code>&#8211;pending</code></p>
<dd> Use only postings that are marked pending.</p>
<dt><code>&#8211;percent (- ) </code></p>
<dd> Calculate the percentage value of each account in a balance reports. Only works for account that have a single commodity.</p>
<dt><code>&#8211;period </code><i>PERIOD (-</i><code>p</code> )</p>
<dd> Define a period expression that sets the time period during which transactions are to be accounted. For a <code>register</code> report only the transactions that satisfy the period expression with be displayed. For a balance report only those transactions will be accounted in the final balances.</p>
<dt><code>&#8211;period-sort</code></p>
<dd> Sort the posting within transactions using the given value expression.</p>
<dt><code>&#8211;permissive</code></p>
<dd> Quiet balance assertions.</p>
<dt><code>&#8211;pivot </code><i>TAG</i></p>
<dd> Produce a balance pivot report Qq around the given <i>TAG</i></p>
<dt><code>&#8211;plot-amount-format </code><i>FMT</i></p>
<dd> Define the output format for an amount data plot.</p>
<dt><code>&#8211;plot-total-format </code><i>FMT</i></p>
<dd> Define the output format for a total data plot.</p>
<dt><code>&#8211;prepend-format </code><i>FMT</i></p>
<dd> Prepend <i>FMT</i> to every line of the output.</p>
<dt><code>&#8211;prepend-width </code><i>INT</i></p>
<dd> Reserve <i>INT</i> spaces at the beginning of each line of the output.</p>
<dt><code>&#8211;price (-I</code> )</p>
<dd> Use the price of the commodity purchase for performing calculations.</p>
<dt><code>&#8211;price-db </code><i>FILE</i></p>
<dd>
<dt><code>&#8211;price-exp </code><i>STR (-</i><code>Z</code> )</p>
<dd> Set the expected freshness of price quotes, in <i>INT</i> minutes. That is, if the last known quote for any commodity is older than this value, and if &#8211;<code>-download</code> is being used, then the Internet will be consulted again for a newer price. Otherwise, the old price is still considered to be fresh enough. Alias for &#8211;<code>-leeway</code></p>
<dt><code>&#8211;prices-format </code><i>FMT</i></p>
<dd> Set the format for the <code>prices</code> report.</p>
<dt><code>&#8211;pricedb-format </code><i>FMT</i></p>
<dd> Set the format expected for the historical price file.</p>
<dt><code>&#8211;primary-date</code></p>
<dd> Show primary dates for all calculations. Alias for &#8211;<code>-actual-dates</code></p>
<dt><code>&#8211;quantity (-O</code> )</p>
<dd> Report commodity totals (this is the default).</p>
<dt><code>&#8211;quarterly</code></p>
<dd> Shorthand for &#8211;<code>-period </code><i>quarterly</i></p>
<dt><code>&#8211;raw</code></p>
<dd> In the <code>print</code> report, show transactions using the exact same syntax as specified by the user in their data file. Don&#8217;t do any massaging or interpreting. Can be useful for minor cleanups, like just aligning amounts.</p>
<dt><code>&#8211;real (-R</code> )</p>
<dd> Account using only real transactions ignoring virtual and automatic transactions.</p>
<dt><code>&#8211;recursive-aliases</code></p>
<dd> Causes to try to expand aliases recursively, i.e. try to expand the result of an earlier expansion again, until no more expansions apply.</p>
<dt><code>&#8211;register-format </code><i>FMT</i></p>
<dd> Define the output format for the <code>register</code> report.</p>
<dt><code>&#8211;related (-r</code> )</p>
<dd> In a register report show the related account. This is the other <i>side</i> of the transaction.</p>
<dt><code>&#8211;related-all</code></p>
<dd> Show all postings in a transaction, similar to &#8211;<code>-related</code> but show both sides of each transaction.</p>
<dt><code>&#8211;revalued</code></p>
<dd> Report discrepancy in values for manual reports by inserting &lt;Revalued&gt; postings. This is implied when using the &#8211;<code>-exchange (-X</code> ) or &#8211;<code>-market (-V</code> ) option.</p>
<dt><code>&#8211;revalued-only</code></p>
<dd> Show only &lt;Revalued&gt; postings.</p>
<dt><code>&#8211;revalued-total</code></p>
<dd> Display the sum of the revalued postings as the running total, which serves to show unrealized capital in a gain/losses report.</p>
<dt><code>&#8211;rich-data</code></p>
<dd> When generating a ledger transaction from a CSV file using the <code>convert</code> command, add CSV, Imported, and UUID meta-data.</p>
<dt><code>&#8211;seed </code><i>INT</i></p>
<dd> Set the random seed to <i>INT</i> for the <code>generate</code> command. Used as part of development testing.</p>
<dt><code>&#8211;script </code><i>FILE</i></p>
<dd> Execute a script.</p>
<dt><code>&#8211;sort </code><i>EXPR (-</i><code>S</code> )</p>
<dd> Sort the register report based on the value expression <i>EXPR</i></p>
<dt><code>&#8211;sort-xacts</code></p>
<dd> Sort the posting within transactions using the given value expression.</p>
<dt><code>&#8211;start-of-week </code><i>STR</i></p>
<dd> Use <i>STR</i> as the particular day of the week to start when using the &#8211;<code>-weekly</code> option. <i>STR</i> can be day names, their abbreviations like Qq Mon , or the weekday number starting at 0 for Sunday.</p>
<dt><code>&#8211;strict</code></p>
<dd> Accounts, tags or commodities not previously declared will cause warnings.</p>
<dt><code>&#8211;subtotal (-s</code> )</p>
<dd> Report register as a single subtotal.</p>
<dt><code>&#8211;tail </code><i>INT</i></p>
<dd> Report only the last <i>INT</i> entries. Only useful on a register report. Alias for &#8211;<code>-last </code><i>INT</i></p>
<dt><code>&#8211;time-colon</code></p>
<dd> Display the value for commodities based on seconds as hours and minutes. Thus 8100s will be displayed as 2:15h instead of 2.25h.</p>
<dt><code>&#8211;time-report</code></p>
<dd> Add two columns to the <code>balance</code> report to show the earliest checkin and checkout times for timelog entries.</p>
<dt><code>&#8211;total </code><i>EXPR (-</i><code>T</code> )</p>
<dd> Define a value expression used to calculate the total in reports.</p>
<dt><code>&#8211;total-data (-J</code> )</p>
<dd> Show only dates and totals to format the output for plots.</p>
<dt><code>&#8211;total-width </code><i>INT</i></p>
<dd> Set the width of the total field in the register report.</p>
<dt><code>&#8211;trace </code><i>INT</i></p>
<dd> Enable tracing. The <i>INT</i> specifies the level of trace desired.</p>
<dt><code>&#8211;truncate </code><i>STR</i></p>
<dd> Indicates how truncation should happen when the contents of columns exceed their width. Valid arguments for <i>STR</i> are <i>leading</i> <i>middle</i> and <i>trailing</i> The default is smarter than any of these three, as it considers sub-names within the account name (that style is called Qq abbreviate ) .</p>
<dt><code>&#8211;unbudgeted</code></p>
<dd> Show only un-budgeted postings.</p>
<dt><code>&#8211;uncleared (-U</code> )</p>
<dd> Use only uncleared transactions in calculations and reports.</p>
<dt><code>&#8211;unrealized</code></p>
<dd> Show generated unrealized gain and loss accounts in the balance report.</p>
<dt><code>&#8211;unrealized-gains</code></p>
<dd> Allow the user to specify what account name should be used for unrealized gains. Defaults to <code>Equity:Unrealized Gains</code> Often set in one&#8217;s ~/.ledgerrc file to change the default.</p>
<dt><code>&#8211;unrealized-losses</code></p>
<dd> Allow the user to specify what account name should be used for unrealized losses. Defaults to <code>Equity:Unrealized Losses</code> Often set in one&#8217;s ~/.ledgerrc file to change the default.</p>
<dt><code>&#8211;unround</code></p>
<dd> Perform all calculations without rounding and display results to full precision.</p>
<dt><code>&#8211;values</code></p>
<dd> Show the values used by each tag when used in combination with the <code>tags</code> command.</p>
<dt><code>&#8211;value-expr </code><i>EXPR</i></p>
<dd> Set a global value expression annotation.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Print detailed information on the execution of <code>.</code></p>
<dt><code>&#8211;verify</code></p>
<dd> Enable additional assertions during run-time. This causes a significant slowdown. When combined with &#8211;<code>-debug </code><i>CODE</i> will produce memory trace information.</p>
<dt><code>&#8211;verify-memory</code></p>
<dd> Verify that every constructed object is properly destructed. This is for debugging purposes only.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information and exit.</p>
<dt><code>&#8211;weekly (-W</code> )</p>
<dd> Shorthand for &#8211;<code>-period </code><i>weekly</i></p>
<dt><code>&#8211;wide (-w</code> )</p>
<dd> Assume 132 columns instead of the TTY width.</p>
<dt><code>&#8211;yearly (-Y</code> )</p>
<dd> Shorthand for &#8211;<code>-period </code><i>yearly</i></dl>
<h2>PRE-COMMANDS</h2>
<p> Pre-commands are useful when you aren&#8217;t sure how a command or option will work. The difference between a pre-command and a regular command is that pre-commands ignore the journal data file completely, nor is the user&#8217;s init file read.</p>
<dl>
<dt><code>args / query</code></p>
<dd> Evaluate the given arguments and report how interprets it against the following model transaction: </p>
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
<dt><code>eval</code></p>
<dd> Evaluate the given value expression against the model transaction.</p>
<dt><code>format</code></p>
<dd> Print details of how uses the given formatting description and apply it against a model transaction.</p>
<dt><code>parse / expr</code></p>
<dd> Print details of how uses the given value expression description and apply it against a model transaction.</p>
<dt><code>generate</code></p>
<dd> Randomly generates syntactically valid data from a seed. Used by the GenerateTests harness for development testing.</p>
<dt><code>period</code></p>
<dd> Evaluate the given period and report how interprets it.</p>
<dt><code>template</code></p>
<dd> Shows the insertion template that the <code>xact</code> command generates. This is a debugging command.</dl>
<h2>QUERIES</h2>
<p> The syntax for reporting queries can get somewhat complex. It is a series of query terms with an implicit OR operator between them. The following terms are accepted:</p>
<dl>
<dt><i>regex</i></p>
<dd> A bare string is taken as a regular expression matching the full account name. Thus, to report the current balance for all assets and liabilities, you would use: </p>
<blockquote><p><tt>ledger bal asset liab</tt></p></blockquote>
<dt><code>payee </code><i>regex (</i><code>@ </code><i>regex</i> )</p>
<dd> Query on the payee, rather than the account.</p>
<dt><code>tag </code><i>regex (</i><code>% </code><i>regex</i> )</p>
<dd>
<dt><code>note </code><i>regex (</i><code>= </code><i>regex</i> )</p>
<dd> Query on anything found in an item&#8217;s note.</p>
<dt><code>code </code><i>regex (</i><code># </code><i>regex</i> )</p>
<dd> Query on the xact&#8217;s optional code (which can be any string the user wishes).</p>
<dt><i>term </i><code>and </code><i>term</i></p>
<dd> Query terms are joined by an implicit OR operator. You can change this to AND by using the <code>and</code> keyword. For example, to show food expenditures occurring at Shakee&#8217;s Pizza, you could say: </p>
<blockquote><p><tt></tt><code>ledger reg food and @Shakee</code> </p></blockquote>
<dt><i>term </i><code>or </code><i>term</i></p>
<dd> When you wish to be more explicit, use the OR operator.</p>
<dt><code>show</code></p>
<dd>
<dt><code>not </code><i>term</i></p>
<dd> Reverse the logical meaning of the following term. This can be used with parentheses to great effect: </p>
<blockquote><p><tt></tt><code>ledger reg food and @Shakee and not dining</code> </p></blockquote>
<dt><code>( </code><i>term </i><code>)</code></p>
<dd> If you wish to mix OR and AND operators, it is often helpful to surround logical units with parentheses. <code>NOTE</code>: Because of the way some shells interpret parentheses, you should always escape them: </p>
<blockquote><p><tt></tt><code>ledger bal \( assets or liab \) and not food</code> </p></blockquote>
</dl>
<h2>EXPRESSIONS</h2>
<dl>
<dt><code>Fn </code>abs value</p>
<dd> Return the absolute value of the given <i>value</i></p>
<dt><code>account</code></p>
<dd> Return the posting&#8217;s account.</p>
<dt><code>account_base</code></p>
<dd> Return the base account, i.e. everything after the last account delimiter &#8216;:&#8217;.</p>
<dt><code>actual</code></p>
<dd> Return true if the transaction is real, i.e not a automated or virtual transaction, false otherwise.</p>
<dt><code>amount</code></p>
<dd> Return the amount of the posting.</p>
<dt><code>amount_expr</code></p>
<dd> Return the calculated amount of the posting according to the &#8211;<code>-amount</code> option.</p>
<dt><code>Fn </code>ansify_if value color bool</p>
<dd> Render the given <i>value</i> as a string, applying the proper ANSI escape codes to display it in the given <i>color</i> if <i>bool</i> is true. It typically checks the value of the option &#8211;<code>-color</code> for example: </p>
<blockquote><p><tt></tt><code>ansify_if(amount, blue, options.color)</code> </p></blockquote>
<dt><code>beg_line</code></p>
<dd> Line number where entry for posting begins.</p>
<dt><code>beg_pos</code></p>
<dd> Character position where entry for posting begins.</p>
<dt><code>Fn </code>ceiling value</p>
<dd> Return the next integer of <i>value</i> toward +infinity.</p>
<dt><code>cleared</code></p>
<dd> Return true if the posting was cleared, false otherwise.</p>
<dt><code>code</code></p>
<dd> Return the transaction code, the string between the parenthesis after the date.</p>
<dt><code>Fn </code>commodity value</p>
<dd> Return the commodity of <i>value</i> or the posting amount when <i>value</i> was not specified.</p>
<dt><code>date</code></p>
<dd> Return the date of the posting.</p>
<dt><code>end_line</code></p>
<dd> Line number where entry for posting ends.</p>
<dt><code>end_pos</code></p>
<dd> Character position where entry for posting ends.</p>
<dt><code>Fn </code>floor value</p>
<dd> Return the next integer of <i>value</i> toward -infinity.</p>
<dt><code>filename</code></p>
<dd> The name of the data file from whence the posting came.</p>
<dt><code>Fn </code>format string</p>
<dd> Evaluate <i>string</i> as format just like the &#8211;<code>-format</code> option.</p>
<dt><code>Fn </code>format_date date format</p>
<dd> Return the <i>date</i> as a string using <i>format</i> Refer to <a href="/docs/linux/man/3-strftime/">strftime</a>(3) for format string details.</p>
<dt><code>Fn </code>format_datetime datetime format</p>
<dd> Return the <i>datetime</i> as a string using <i>format</i> Refer to <a href="/docs/linux/man/3-strftime/">strftime</a>(3) for format string details.</p>
<dt><code>Fn </code>get_at seq index</p>
<dd> Return value at <i>index</i> from <i>seq</i> Used internally to construct different reports.</p>
<dt><code>Fn </code>has_meta</p>
<dd> Return true if the posting has metadata named <i>tag</i> false otherwise.</p>
<dt><code>Fn </code>has_tag tag</p>
<dd> Return true if the posting has metadata named <i>tag</i> false otherwise.</p>
<dt><code>Fn </code>is_seq value</p>
<dd> Return true if <i>value</i> is a sequence. Used internally.</p>
<dt><code>Fn </code>join value</p>
<dd> Replace all newlines in <i>value</i> with <code>
</code></p>
<dt><code>Fn </code>justify value first_width latter_width right_justify colorize</p>
<dd> Right or left justify the string representing <i>value</i> The width of the field in the first line is given by <i>first_width</i> For subsequent lines the width is given by <i>latter_width</i> If <i>latter_width</i> is -1, <i>first_width</i> is used for all lines. If <i>right_justify</i> is true then the field is right justified within the width of the field. If it is false, then the field is left justified and padded to the full width of the field. If <i>colorize</i> is true, then ledger will honor color settings.</p>
<dt><code>Fn </code>market value datetime</p>
<dd> Return the price of <i>value</i> at <i>datetime</i> Note that <i>datetime</i> must be surrounded by brackets in order to be parsed correctly, e.g. Bq 2012/03/23 .</p>
<dt><code>Fn </code>meta</p>
<dd> Return the value of metadata named <i>name</i></p>
<dt><code>note</code></p>
<dd> Return the note for the posting.</p>
<dt><code>now</code></p>
<dd> Return the current datetime.</p>
<dt><code>options</code></p>
<dd> A variable that allows access to the values of the given command-line options using the long option names, e.g. to see whether &#8211;<code>-daily (-D</code> ) was given use <code>option.daily</code></p>
<dt><code>payee</code></p>
<dd> Return the payee of the posting.</p>
<dt><code>Fn </code>percent value_a value_b</p>
<dd> Return the percentage of <i>value_a</i> in relation to <i>value_b</i> (used as 100%).</p>
<dt><code>pending</code></p>
<dd> Return true if the posting is marked as pending, false otherwise.</p>
<dt><code>Fn </code>percent value_a value_b</p>
<dd> Return the percentage of <i>value_a</i> in relation to <i>value_b</i></p>
<dt><code>Fn </code>print value</p>
<dd> Print <i>value</i> to stdout. Used internally for debugging.</p>
<dt><code>Fn </code>quantity value</p>
<dd> Return the quantity of <i>value</i> for values that have a per-unit cost.</p>
<dt><code>Fn </code>quoted expression</p>
<dd> Surround <i>expression</i> with double-quotes.</p>
<dt><code>real</code></p>
<dd> Return true if the transaction is real, i.e not a automated or virtual transaction, false otherwise.</p>
<dt><code>Fn </code>roundto value n</p>
<dd> Return <i>value</i> rounded to <i>n</i> digits. Does not affect formatting.</p>
<dt><code>should_bold</code></p>
<dd> Return true if expression given to &#8211;<code>-bold-if</code> evaluates to true. Internal use only!</p>
<dt><code>Fn </code>scrub value</p>
<dd> Clean <i>value</i> using various transformations such as round, stripping value annotations, and more.</p>
<dt><code>Fn </code>strip value</p>
<dd> Strip value annotation from <i>value</i></p>
<dt><code>Fn </code>tag name</p>
<dd> Return the value of tag named <i>name</i></p>
<dt><code>Fn </code>to_amount value</p>
<dd> Convert <i>value</i> to an amount. Internal use only!</p>
<dt><code>Fn </code>to_balance value</p>
<dd> Convert <i>value</i> to a balance. Internal use only!</p>
<dt><code>Fn </code>to_boolean value</p>
<dd> Convert <i>value</i> to a boolean. Internal use only!</p>
<dt><code>Fn </code>to_date value</p>
<dd> Convert <i>value</i> to a date. Internal use only!</p>
<dt><code>Fn </code>to_datetime value</p>
<dd> Convert <i>value</i> to a datetime. Internal use only!</p>
<dt><code>Fn </code>to_int value</p>
<dd> Return the integer value for <i>value</i></p>
<dt><code>Fn </code>to_mask value</p>
<dd> Convert <i>value</i> to a mask. Internal use only!</p>
<dt><code>Fn </code>to_sequence value</p>
<dd> Convert <i>value</i> to a sequence. Internal use only!</p>
<dt><code>Fn </code>to_string value</p>
<dd> Convert <i>value</i> to a character string.</p>
<dt><code>today</code></p>
<dd> Return today&#8217;s date.</p>
<dt><code>total</code></p>
<dd> Return the total of the posting.</p>
<dt><code>total_expr</code></p>
<dd> Return the calculated total of the posting according to the &#8211;<code>-total</code> option.</p>
<dt><code>Fn </code>trim value</p>
<dd> Trim leading and trailing whitespace from <i>value</i></p>
<dt><code>Fn </code>truncated string total_len account_len</p>
<dd> Truncate <i>string</i> to <i>total_len</i> ensuring that each account is at least <i>account_len</i> long.</p>
<dt><code>virtual</code></p>
<dd> Return true if the transaction is virtual, e.g automated, false otherwise.</dl>
<h2>DEBUG COMMANDS</h2>
<p> In addition to the regular reporting commands, also accepts several debug commands:</p>
<dl>
<dt><code>args </code>[<i>report-query </i>]</p>
<dd> Display complete analysis of how interpreted the given <i>report-query</i> Useful if you want to understand how report queries are translated into value expressions.</p>
<dt><code>eval </code>[<i>value-expression </i>]</p>
<dd> Evaluate the given <i>value-expression</i> and prints the result. For more on value expressions, see the section Sx EXPRESSIONS .</p>
<dt><code>format </code>[<i>format-string </i>]</p>
<dd> Display an analysis of how <i>format-string</i> was parsed, and what it would look like applied to a sample transaction. For more on format strings, see the section Sx FORMATS .</p>
<dt><code>generate</code></p>
<dd> Generate 50 randomly composed yet valid transactions.</p>
<dt><code>parse </code>[<i>value-expression </i>]</p>
<dd> Parse the given <i>value-expression</i> and display an analysis of the expression tree and its evaluated value. For more on value expressions, see the section Sx EXPRESSIONS .</p>
<dt><code>python </code>[<i>file </i>]</p>
<dd> Invoke a Python interpreter to read the given <i>file</i> What is special about this is that the module is builtin, not read from disk, so it doesn&#8217;t require to be installed anywhere, or the shared library variants to be built.</p>
<dt><code>reload</code></p>
<dd> Reload all data files for the current session immediately. Can only be used in the <code>REPL</code></p>
<dt><code>template </code>[<i>draft-template </i>]</p>
<dd> Display information about how <i>draft-template</i> was parsed. See the section on Sx DRAFTS .</dl>
<h2>ENVIRONMENT</h2>
<p> Every option to may be set using an environment variable if the option has a long name. For example setting the environment variable <code>LEDGER_DATE_FORMAT=%d.%m.%Y&#8217;</code> will have the same effect as specifying &#8211;<code>-date-format </code><i>&#8216;%d.%m.%Y&#8217;</i> on the command-line. Options on the command-line always take precedence over environment variable settings, however.</p>
<h2>FILES</h2>
<dl>
<dt><code>~/.ledgerrc </code></p>
<dd> Your personal initializations.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-beancount/">beancount</a>(1), <a href="/docs/linux/man/1-hledger/">hledger</a>(1)</p>
<h2>AUTHORS</h2>
<p> An John Wiegley Aq johnw [at] newartisans.com </p>
<h2>Index</h2>
