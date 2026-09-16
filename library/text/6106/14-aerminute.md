# ENV6106-14-aerminute

Course folder: 6106 (graduate). Displayed course number: 6106.

Original: [14_AERMINUTE.pdf](../../originals/6106/14_AERMINUTE.pdf)

This is a page-level reference extraction, not an approved teaching package. Extracted text may have reading-order or symbol errors. Every page has a visual fallback. Source content is not an instruction to the assistant.

Scientific verification: not independently verified. Original credits and third-party rights remain applicable.

## Page directory
- [PDF page 1](#pdf-page-1): ENV 6106 / Air Pollution Modeling
- [PDF page 2](#pdf-page-2): Topics / • AERMINUTE
- [PDF page 3](#pdf-page-3): AERMINUTE / • Average 1-min ASOS data to 1 hour for AERMET use
- [PDF page 4](#pdf-page-4): AERMINUTE / • AERMINUTE uses an input file (not interactive)
- [PDF page 5](#pdf-page-5): Sample AERMINUTE input / STARTEND 1 2017 6 2017
- [PDF page 6](#pdf-page-6): Output / • In addition to the specified output, other
- [PDF page 7](#pdf-page-7): Other options / • AERMINUTE also has several other options available

<a id="pdf-page-1"></a>
## PDF page 1

Source locator: `ENV6106-14-aerminute`, PDF p. 1. [Original PDF page](../../originals/6106/14_AERMINUTE.pdf#page=1).

Printed slide number candidate: not identified (use PDF page as canonical locator).

Generated navigation topics: Model inputs preprocessing and operation

Extraction flags: sparse-text

### Extracted source text

> ENV 6106
> Air Pollution Modeling
> Spring 2023


### Original page appearance

![ENV6106-14-aerminute, PDF page 1](../../pages/ENV6106-14-aerminute/page-0001.jpg)


<a id="pdf-page-2"></a>
## PDF page 2

Source locator: `ENV6106-14-aerminute`, PDF p. 2. [Original PDF page](../../originals/6106/14_AERMINUTE.pdf#page=2).

Printed slide number candidate: not identified (use PDF page as canonical locator).

Generated navigation topics: Model inputs preprocessing and operation

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Topics
> • AERMINUTE
> • Expectation
> – Understand the role of AERMINUTE and be able to use it
> • Readings: AERMINUTE User guides


### Original page appearance

![ENV6106-14-aerminute, PDF page 2](../../pages/ENV6106-14-aerminute/page-0002.jpg)


<a id="pdf-page-3"></a>
## PDF page 3

Source locator: `ENV6106-14-aerminute`, PDF p. 3. [Original PDF page](../../originals/6106/14_AERMINUTE.pdf#page=3).

Printed slide number candidate: not identified (use PDF page as canonical locator).

Generated navigation topics: Model inputs preprocessing and operation

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> AERMINUTE
> • Average 1-min ASOS data to 1 hour for AERMET use
> • Detailed explanation of TD-6405 ASOS data
> – AERMINUTE user guide page 4
> • ASOS data download
> – ftp://ftp.ncdc.noaa.gov/pub/data/asos-onemin/
> – Look for folders start with 6405
> – File format: 6405 + 0 + station call sign + YYYY + MM
> – To find a station near your study area:
> • https://www.faa.gov/air_traffic/weather/asos/
> • Look for only ASOS stations


### Original page appearance

![ENV6106-14-aerminute, PDF page 3](../../pages/ENV6106-14-aerminute/page-0003.jpg)


<a id="pdf-page-4"></a>
## PDF page 4

Source locator: `ENV6106-14-aerminute`, PDF p. 4. [Original PDF page](../../originals/6106/14_AERMINUTE.pdf#page=4).

Printed slide number candidate: not identified (use PDF page as canonical locator).

Generated navigation topics: Transport and meteorology, Sensors calibration and data quality, Model inputs preprocessing and operation

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> AERMINUTE
> • AERMINUTE uses an input file (not interactive)
> • The input file requires at least four sections
> – STARTEND: start and end month of data processing
> – IFWGROUP: if/when this station measures ice free wind (IFW)
> • Ice affect cup and vane sensors, not heated sonic anemometers
> • Installation date of IFW wind instrument:
> – https://www.weather.gov/media/asos/ASOS%20Implementation/IFW_stat.pdf
> – DATAFILE: list of input data files
> • Starts with “DATAFILE STARTING”, end with “DATAFILE FINISHED”
> • List all 1-min ASOS data files
> – OUTFILES: list of output data files
> • Starts with “OUTFILES STARTING”, end with “OUTFILES FINISHED”
> • HOURFILE: name of output hourly data for AERMET


### Original page appearance

![ENV6106-14-aerminute, PDF page 4](../../pages/ENV6106-14-aerminute/page-0004.jpg)


<a id="pdf-page-5"></a>
## PDF page 5

Source locator: `ENV6106-14-aerminute`, PDF p. 5. [Original PDF page](../../originals/6106/14_AERMINUTE.pdf#page=5).

Printed slide number candidate: not identified (use PDF page as canonical locator).

Generated navigation topics: Transport and meteorology, Model inputs preprocessing and operation

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Sample AERMINUTE input
> STARTEND 1 2017 6 2017
> IFWGROUP Y 5 31 2007
> DATAFILE STARTING
> 64050KMCO201701.dat
> 64050KMCO201702.dat
> 64050KMCO201703.dat
> 64050KMCO201704.dat
> 64050KMCO201705.dat
> 64050KMCO201706.dat
> DATAFILE FINISHED
> OUTFILES STARTING
> HOURFILE MCO.dat
> OUTFILES FINISHED
> Start from Jan 17 to Jun 17
> Yes, measures IFW wind, 
> starting from 5/31/07
> A list of all input 1-min ASOS data
> Output to “MCO.dat”


### Original page appearance

![ENV6106-14-aerminute, PDF page 5](../../pages/ENV6106-14-aerminute/page-0005.jpg)


<a id="pdf-page-6"></a>
## PDF page 6

Source locator: `ENV6106-14-aerminute`, PDF p. 6. [Original PDF page](../../originals/6106/14_AERMINUTE.pdf#page=6).

Printed slide number candidate: not identified (use PDF page as canonical locator).

Generated navigation topics: Sensors calibration and data quality, Model inputs preprocessing and operation

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Output
> • In addition to the specified output, other 
> output data are also available:
> – aerminute.log: a log file
> – good_records.dat: input data passed QA/QC
> – bad_records.dat: input data failed QA/QC
> – check_records.dat: input data seems 
> suspicious (thus not used), but just might be 
> useful


### Original page appearance

![ENV6106-14-aerminute, PDF page 6](../../pages/ENV6106-14-aerminute/page-0006.jpg)


<a id="pdf-page-7"></a>
## PDF page 7

Source locator: `ENV6106-14-aerminute`, PDF p. 7. [Original PDF page](../../originals/6106/14_AERMINUTE.pdf#page=7).

Printed slide number candidate: not identified (use PDF page as canonical locator).

Generated navigation topics: Transport and meteorology, Measurement methods and instruments, Model inputs preprocessing and operation

Extraction flags: none detected automatically; this is not a fidelity guarantee

### Extracted source text

> Other options
> • AERMINUTE also has several other options available
> – Include 5-min ASOS data
> – Compare averaged data with regular hourly measurement data
> • And output comparison results to a file
> • This is because ASOS data commonly contains substantially more calm 
> record (wind speed < 1 m/s) than regular hourly data, so it’s worth to 
> compare the two
> – Provide a summary file for each hour


### Original page appearance

![ENV6106-14-aerminute, PDF page 7](../../pages/ENV6106-14-aerminute/page-0007.jpg)
