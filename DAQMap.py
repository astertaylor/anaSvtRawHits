#input: FEB, hybrid; output: layer, module
febToLayer = {
        0.0 : 1.0,
        0.1 : 2.0,
        1.3 : 1.1,
        1.2 : 2.1,
        0.2 : 3.0,
        0.3 : 4.0,
        1.1 : 3.1,
        1.0 : 4.1,
        2.0 : 5.0,
        2.1 : 6.0,
        3.1 : 8.1,
        3.0 : 7.1,
        2.3 : 7.0,
        2.2 : 8.0,
        3.3 : 6.1,
        3.2 : 5.1,
        4.0 : 9.0,
        4.2 : 10.0,
        4.1 : 9.2,
        4.3 : 10.2,
        5.2 : -1,
        5.0 : -1,
        5.3 : -1,
        5.1 : -1,
        6.0 : 11.0,
        6.2 : 12.0,
        6.1 : 11.2,
        6.3 : 12.2,
        7.2 : 12.1,
        7.0 : 11.1,
        7.3 : 12.3,
        7.1 : 11.3,
        8.0 : 13.0,
        8.2 : 14.0,
        8.1 : 13.2,
        8.3 : 14.2,
        9.2 : 14.1,
        9.0 : -1,
        9.3 : -1,
        9.1 : -1
        }

#input: layer, module; input:FEB, hybrid
layerToFeb = {
        1.0 : 0.0,
        2.0 : 0.1,
        1.1 : 1.3,
        2.1 : 1.2,
        3.0 : 0.2,
        4.0 : 0.3,
        3.1 : 1.1,
        4.1 : 1.0,
        5.0 : 2.0,
        6.0 : 2.1,
        8.1 : 3.1,
        7.1 : 3.0,
        7.0 : 2.3,
        8.0 : 2.2,
        6.1 : 3.3,
        5.1 : 3.2,
        9.0 : 4.0,
        10.0 : 4.2,
        9.2 : 4.1,
        10.2 : 4.3,
        11.0 : 6.0,
        12.0 : 6.2,
        11.2 : 6.1,
        12.2 : 6.3,
        12.1 : 7.2,
        11.1 : 7.0,
        12.3 : 7.3,
        11.3 : 7.1,
        13.0 : 8.0,
        14.0 : 8.2,
        13.2 : 8.1,
        14.2 : 8.3,
        14.1 : 9.2
        }
