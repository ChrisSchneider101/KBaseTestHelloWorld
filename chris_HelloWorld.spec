/*
A KBase module: chris_HelloWorld
*/

module chris_HelloWorld {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_chris_HelloWorld(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
