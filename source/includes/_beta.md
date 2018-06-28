# Beta Features

This section contains experimental features that are not fully developed yet. Experimental features are not always stable and may undergo spot changes on a regular basis.

## Result Set Exports

Rehive supports a simple mechanism for exporting larger lists of results than the API normally allows. This is done via asynchnous tasks that build JSON files containing the requested data. These result sets are snapshots of the rehive data and show the data as it was at the time of the export. Therefore it is advisable to provide strict date range filters for the exports.

Large result sets are suppport on the following resources:

**transactions**: Check the transaction set documentation for more on this.

### Limitations

1. Storage may be volatile while this is in beta. Do not treat the generated files as permanent resources.
2. There is a max size of 10000 resuts per export file. If more than 10000 results are returned, the results will be split over multiple files.
3. The API may change in future. Additional fields could be added, and some may be removed.

