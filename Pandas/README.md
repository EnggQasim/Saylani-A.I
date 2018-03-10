# Preface
## [learn quickly ClickMe!](./allPandasBasics.ipynb)
This book is about learning to use pandas, an open source library for Python, which
was created to enable Python to easily manipulate and perform powerful statistical
and mathematical analyses on tabular and multidimensional datasets. The design of
pandas and its power combined with the familiarity of Python have created explosive
growth in its usage over the last several years, particularly among financial firms as
well as those simply looking for practical tools for statistical and data analysis.
While there exist many excellent examples of using pandas to solve many

domain-specific problems, it can be difficult to find a cohesive set of examples
in a form that allows one to effectively learn and apply the features of pandas.
The information required to learn practical skills in using pandas is distributed
across many websites, slide shares, and videos, and is generally not in a form
that gives an integrated guide to all of the features with practical examples in
an easy-to-understand and applicable fashion.

This book is therefore intended to be a go-to reference for learning pandas. It will
take you all the way from installation, through to creating one- and two-dimensional
indexed data structures, to grouping data and slicing-and-dicing them, with common
analyses used to demonstrate derivation of useful results. This will include the
loading and saving of data from resources that are local and Internet-based and
creating effective data visualizations that provide instant ability to visually realize
insights into the meaning previously hidden within complex data.
<img src="images/panda.jpg">
# What this covers
- `Chapter 1`, A Tour of pandas, is a hands-on introduction to the key features of pandas.
It will give you a broad overview of the types of data tasks that can be performed
with pandas. This chapter will set the groundwork for learning as all concepts
introduced in this chapter will be expanded upon in subsequent chapters.

- `Chapter 2`, Installing pandas, will show you how to install Anaconda Python and pandas
on Windows, OS X, and Linux. This chapter also covers using the conda package
manager to upgrade pandas and its dependent libraries to the most recent version.
- `Chapter 3`, NumPy for pandas, will introduce you to concepts in NumPy,
particularly NumPy arrays, which are core for understanding the pandas
Series and DataFrame objects.
- `Chapter 4`, The pandas Series Object, covers the pandas Series object and how it
expands upon the functionality of the NumPy array to provide richer representation
and manipulation of sequences of data through the use of high-performance indexes.
- `Chapter 5`, The pandas DataFrame Object, introduces the primary data structure of
pandas, the DataFrame object, and how it forms a two-dimensional representation of
tabular data by aligning multiple Series objects along a common index to provide
seamless access and manipulation across elements in multiple series that are related
by a common index label.
- `Chapter 6`, Accessing Data, shows how data can be loaded and saved from external
sources into both Series and DataFrame objects. You will learn how to access
data from multiple sources such as files, HTTP servers, database systems, and
web services, as well as how to process data in CSV, HTML, and JSON formats.
- `Chapter 7`, Tidying Up Your Data, instructs you on how to use the various tools
provided by pandas for managing dirty and missing data.
- `Chapter 8`, Combining and Reshaping Data, covers various techniques for combining,
splitting, joining, and merging data located in multiple pandas objects, and
then demonstrates how to reshape data using concepts such as pivots, stacking,
and melting.
- `Chapter 9`, Grouping and Aggregating Data, focuses on how to use pandas to group data
to enable you to perform aggregate operations on grouped data to assist in deriving
analytic results.

- `Chapter 10`, Time-series Data, will instruct you on how to use pandas to represent
sequences of information that is indexed by the progression of time. This chapter
will first cover how pandas represents dates and time, as well as concepts such as
periods, frequencies, time zones, and calendars. The focus then shifts to time-series
data and various operations such as shifting, lagging, resampling, and moving
window operations.
