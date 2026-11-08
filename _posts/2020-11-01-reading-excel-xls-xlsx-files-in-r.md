---
title: "Reading Excel Files in R"
date: 2020-11-01 09:30:03 +0000
modified: 2026-04-11 17:38:12 +0000
author: "Daniel"
layout: post
categories: [scripting-utilities]
canonical: /reading-excel-xls-xlsx-files-in-r/
---

Excel files remain a common data format you’ll encounter. The `readxl` package handles both .xls and .xlsx formats efficiently without external dependencies, making it the standard choice for Excel import in R.

## Installation

Install the package once per R environment:

``` r
install.packages("readxl")
```

Load it in your session or script:

``` r
library(readxl)
```

## Basic Import

The `read_excel()` function handles both xls and xlsx formats automatically:

``` r
data <- read_excel("path/to/file.xlsx")
```

The function returns a tibble by default. To convert to a data frame if needed:

``` r
data <- as.data.frame(read_excel("path/to/file.xlsx"))
```

## Working with Multiple Sheets

Excel workbooks often contain multiple sheets. Specify which sheet to read by name or position:

``` r
# By sheet name
budget_data <- read_excel("financials.xlsx", sheet = "Budget")

# By position (1-indexed)
first_sheet <- read_excel("financials.xlsx", sheet = 1)
second_sheet <- read_excel("financials.xlsx", sheet = 2)

# List all sheet names
excel_sheets("financials.xlsx")
```

## Column Type Control

By default, `read_excel()` guesses column types. You can specify them explicitly to avoid type conversion issues:

``` r
data <- read_excel(
  "sales.xlsx",
  col_types = c("text", "numeric", "date", "logical", "skip")
)
```

Available types: “skip”, “guess”, “logical”, “numeric”, “date”, “text”, “list”.

The “skip” type excludes a column from the import entirely, useful for ignoring unwanted columns.

## Handling Ranges and Headers

Read a specific cell range:

``` r
# Read range B3:D10
data <- read_excel("report.xlsx", range = "B3:D10")

# Include sheet name in range
data <- read_excel("workbook.xlsx", range = "Budget!B2:G14")
```

Control column naming:

``` r
# Use first row as column names (default)
data <- read_excel("file.xlsx", col_names = TRUE)

# No column names, use X1, X2, X3 etc.
data <- read_excel("file.xlsx", col_names = FALSE)

# Provide custom column names
data <- read_excel("file.xlsx", col_names = c("ID", "Name", "Score"))
```

## Skipping Rows and Limiting Data

Skip header rows before actual data:

``` r
# Skip first 5 rows before reading
data <- read_excel("file.xlsx", skip = 5)
```

Limit the number of rows read:

``` r
# Read only first 1000 data rows
data <- read_excel("file.xlsx", n_max = 1000)
```

## Missing Values

Specify how missing values are represented in the file:

``` r
# Treat "NA", "N/A", and empty cells as missing
data <- read_excel("file.xlsx", na = c("", "NA", "N/A"))
```

## Whitespace Handling

Control leading/trailing whitespace:

``` r
# Strip whitespace (default)
data <- read_excel("file.xlsx", trim_ws = TRUE)

# Keep whitespace
data <- read_excel("file.xlsx", trim_ws = FALSE)
```

## Column Name Repair

Handle problematic column names automatically:

``` r
# Default: ensures unique, non-empty names
data <- read_excel("file.xlsx", .name_repair = "unique")

# Alternative strategies
data <- read_excel("file.xlsx", .name_repair = "minimal")
```

## Interactive File Selection

Choose a file via GUI dialog:

``` r
data <- read_excel(file.choose())
```

RStudio will open a file browser for selection.

## Complete Example

A practical workflow combining multiple features:

``` r
library(readxl)

# Check available sheets
sheets <- excel_sheets("quarterly_report.xlsx")
print(sheets)

# Read specific sheet with type control and row limit
sales <- read_excel(
  "quarterly_report.xlsx",
  sheet = "Sales",
  col_types = c("text", "date", "numeric", "numeric", "skip"),
  skip = 2,
  n_max = 500,
  na = c("", "N/A", "-")
)

# View first few rows
head(sales)

# Check structure
str(sales)
```

## Performance Considerations

For large files (100K+ rows), `read_excel()` performs adequately but consider:

- Use `col_types` explicitly to avoid type guessing overhead
- Use `n_max` to read in chunks if processing the entire file isn’t necessary
- Use `range` to import only needed cell ranges
- For repeated large imports, consider exporting data to CSV or Parquet for faster loading

## Alternatives

If you need more advanced Excel manipulation (writing, modifying sheets), use `openxlsx`:

``` r
library(openxlsx)
write.xlsx(data, "output.xlsx")
```

For reading from remote URLs or complex scenarios, `readxlsx` and other packages exist, but `readxl` covers the vast majority of import use cases efficiently.
