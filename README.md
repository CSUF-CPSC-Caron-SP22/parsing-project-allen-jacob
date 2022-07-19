[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7720877&assignment_repo_type=AssignmentRepo)
# CPSC 323 Parsing Project

This is Jacob, Christian, Allen's project.

## Team members and emails

Jacob Ursenbach (jlursenbach@csu.fullerton.edu)

Christian Lara (larachristian@csu.fullerton.edu)

Allen Rivas (allen.rrivas30@csu.fullerton.edu)

## How to compile and execute
 
    /default-grammar-parser$ python3 main.py code.txt

## Inputs and outputs

    Input: a = b + c + d
    
    Output:
    ----------------------------------------------------------------------------------
        ______ _____ _____ _____ _   _  ______  ___  ______  _____ _____
        | ___ \  ___|  __ \_   _| \ | | | ___ \/ _ \ | ___ \/  ___|  ___|
        | |_/ / |__ | |  \/ | | |  \| | | |_/ / /_\ \| |_/ /\ `--.| |__
        | ___ \  __|| | __  | | | . ` | |  __/|  _  ||    /  `--. \  __|
        | |_/ / |___| |_\ \_| |_| |\  | | |   | | | || |\ \ /\__/ / |___
        \____/\____/ \____/\___/\_| \_/ \_|   \_| |_/\_| \_|\____/\____/
    ----------------------------------------------------------------------------------
    STEP  STACK           STREAM      Table Lookup
    1     E0              a=b+c+d$    [a,0]=S3
    2     E0a3            =b+c+d$     [=,3]=R4
    3     E0E2            =b+c+d$     [=,2]=S5
    4     E0E2=5          b+c+d$      [b,5]=S8
    5     E0E2=5b8        +c+d$       [+,8]=R4
    6     E0E2=5E7        +c+d$       [+,7]=S9
    7     E0E2=5E7+9      c+d$        [c,9]=S10
    8     E0E2=5E7+9c10   +d$         [+,10]=R3
    9     E0E2=5E7        +d$         [+,7]=S9
    10    E0E2=5E7+9      d$          [d,9]=S10
    11    E0E2=5E7+9d10   $           [$,10]=R3
    12    E0E2=5E7        $           [$,7]=R1
    13    E0S1            $           [$,1]=ACCT
    ACCT: parsing_complete -> SUCCESS
      ___  _____  _____ _____            _____ _   _ _____  _____  _____ _____ _____
     / _ \/  __ \/  __ \_   _|          /  ___| | | /  __ \/  __ \|  ___/  ___/  ___|
    / /_\ \ /  \/| /  \/ | |    ______  \ `--.| | | | /  \/| /  \/| |__ \ `--.\ `--.
    |  _  | |    | |     | |   |______|  `--. \ | | | |    | |    |  __| `--. \`--. \
    | | | | \__/\| \__/\ | |            /\__/ / |_| | \__/\| \__/\| |___/\__/ /\__/ /
    \_| |_/\____/ \____/ \_/            \____/ \___/ \____/ \____/\____/\____/\____/
    
  
