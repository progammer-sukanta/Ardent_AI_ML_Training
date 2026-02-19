<?xml version="1.0" encoding="UTF-8"?>
<readme>

  <!-- ═══════════════════════════════════════════════════════ -->
  <!--              CALCULUS — Advanced Python Calculator      -->
  <!-- ═══════════════════════════════════════════════════════ -->

  <project>
    <name>CALCULUS — Advanced Python Calculator</name>
    <tagline>A feature-rich, terminal-based calculator built in Python with arithmetic, statistics, and percentage tools — powered by explicit type casting and clean user input handling.</tagline>
    <language>Python 3.10+</language>
    <dependencies>None (Standard Library only)</dependencies>
    <entry_point>calculator.py</entry_point>
  </project>


  <!-- ═══════════════════════════════════════════════════════ -->
  <!--                        BADGES                          -->
  <!-- ═══════════════════════════════════════════════════════ -->

  <badges>
    <badge label="Python"        value="3.10+"         color="blue"  />
    <badge label="License"       value="MIT"           color="green" />
    <badge label="Dependencies"  value="Zero"          color="brightgreen" />
    <badge label="Platform"      value="Cross-Platform" color="lightgrey" />
    <badge label="Type"          value="CLI Tool"      color="orange" />
  </badges>


  <!-- ═══════════════════════════════════════════════════════ -->
  <!--                    FEATURE SUMMARY                     -->
  <!-- ═══════════════════════════════════════════════════════ -->

  <features>
    <feature id="1">
      <module>Basic Calculator</module>
      <description>Arithmetic operations — addition, subtraction, multiplication, division, modulus, power — with zero-division safety.</description>
      <operators>+ - * / % **</operators>
    </feature>

    <feature id="2">
      <module>Statistics Calculator</module>
      <description>Compute mean, median, mode (multi-modal support), standard deviation, variance, sum, min, max, and range from a list of numbers.</description>
      <operators>mean · median · mode · avg · std_dev · variance</operators>
    </feature>

    <feature id="3">
      <module>Percentage Tool</module>
      <description>Five dedicated percentage operations: ratio, percentage change, reverse percentage, markup, and discount.</description>
      <operators>X% of Y · % change · X is % of Y · add % · subtract %</operators>
    </feature>

    <feature id="4">
      <module>Expression Evaluator</module>
      <description>Type raw arithmetic expressions directly into the terminal with sanitized safe evaluation.</description>
      <operators>+ - * / % ** ^ ( )</operators>
    </feature>
  </features>


  <!-- ═══════════════════════════════════════════════════════ -->
  <!--                   TABLE OF CONTENTS                    -->
  <!-- ═══════════════════════════════════════════════════════ -->

  <table_of_contents>
    <section ref="demo"           label="Demo" />
    <section ref="installation"   label="Installation" />
    <section ref="usage"          label="Usage" />
    <section ref="modules"        label="Modules" />
    <section ref="type_casting"   label="Type Casting" />
    <section ref="error_handling" label="Error Handling" />
    <section ref="structure"      label="Project Structure" />
    <section ref="requirements"   label="Requirements" />
    <section ref="contributing"   label="Contributing" />
    <section ref="license"        label="License" />
  </table_of_contents>


  <!-- ═══════════════════════════════════════════════════════ -->
  <!--                         DEMO                          -->
  <!-- ═══════════════════════════════════════════════════════ -->

  <demo id="demo">
    <title>Terminal Demo</title>
    <screenshot><![CDATA[
══════════════════════════════════════════════════════
    CALCULUS — Advanced Python Calculator
══════════════════════════════════════════════════════
  Type casting · Arithmetic · Statistics · Percentages

  ──────────────────────────────────────────────────────
    MAIN MENU
  ──────────────────────────────────────────────────────
    [1]  Basic Calculator     [ +  −  ×  ÷  %  ^ ]
    [2]  Statistics           [ mean · median · mode · avg ]
    [3]  Percentage Tool      [ %  change  ratio ]
    [4]  Expression Evaluator [ type any expression ]
    [0]  Exit

  Select option: _
    ]]></screenshot>

    <stats_demo><![CDATA[
  ALL STATISTICS REPORT
  Numbers  : [1.0, 3.0, 5.0, 7.0, 9.0, 2.0, 2.0]

  Count    : 7
  Sum      : 29
  Mean     : 4.14285714
  Median   : 3
  Mode     : 2  (×2)
  Min      : 1
  Max      : 9
  Range    : 8
  Std Dev  : 2.74791201
  Variance : 7.55102041
    ]]></stats_demo>
  </demo>


  <!-- ═══════════════════════════════════════════════════════ -->
  <!--                     INSTALLATION                       -->
  <!-- ═══════════════════════════════════════════════════════ -->

  <installation id="installation">
    <note>No external packages required. Uses only Python built-in modules.</note>

    <steps>
      <step number="1">
        <action>Clone the repository</action>
        <command>git clone https://github.com/your-username/calculus-python.git</command>
      </step>

      <step number="2">
        <action>Navigate into the project folder</action>
        <command>cd calculus-python</command>
      </step>

      <step number="3">
        <action>Run the calculator</action>
        <command>python3 calculator.py</command>
      </step>
    </steps>

    <requirement>Python 3.10 or higher</requirement>
  </installation>


  <!-- ═══════════════════════════════════════════════════════ -->
  <!--                        USAGE                          -->
  <!-- ═══════════════════════════════════════════════════════ -->

  <usage id="usage">
    <run_command>python3 calculator.py</run_command>

    <controls>
      <control key="0"        action="Exit the program" />
      <control key="Ctrl + C" action="Return to main menu from any sub-section" />
      <control key="back / q" action="Exit the Expression Evaluator loop" />
    </controls>

    <input_format>
      <description>Numbers can be entered as integers or decimals. Lists use comma or space separation.</description>
      <example label="Single number">42</example>
      <example label="Decimal">3.14</example>
      <example label="Number list">4, 7, 2, 9, 1, 5, 7, 3</example>
      <example label="Number list (spaces)">4 7 2 9 1 5 7 3</example>
    </input_format>
  </usage>


  <!-- ═══════════════════════════════════════════════════════ -->
  <!--                       MODULES                         -->
  <!-- ═══════════════════════════════════════════════════════ -->

  <modules id="modules">

    <!-- MODULE 1: BASIC CALCULATOR -->
    <module id="basic_calculator" menu_option="1">
      <title>Basic Calculator</title>
      <description>Enter two numbers and select an arithmetic operation.</description>

      <operations>
        <operation option="1" symbol="+"  name="Addition"       example="5 + 3 = 8" />
        <operation option="2" symbol="-"  name="Subtraction"    example="5 - 3 = 2" />
        <operation option="3" symbol="*"  name="Multiplication" example="5 * 3 = 15" />
        <operation option="4" symbol="/"  name="Division"       example="9 / 3 = 3" />
        <operation option="5" symbol="%"  name="Modulus"        example="10 % 3 = 1" />
        <operation option="6" symbol="**" name="Power"          example="2 ** 8 = 256" />
      </operations>

      <safety_note>Division and modulus by zero return a descriptive error — the program never crashes.</safety_note>
    </module>


    <!-- MODULE 2: STATISTICS CALCULATOR -->
    <module id="statistics_calculator" menu_option="2">
      <title>Statistics Calculator</title>
      <description>Enter a list of numbers, then select a statistical function.</description>

      <input_example>1, 3, 5, 7, 9, 2, 2</input_example>

      <functions>
        <function option="1" name="Mean (Average)">
          <formula>Sum of all values ÷ count</formula>
          <shows>numbers, sum, count, result</shows>
        </function>

        <function option="2" name="Median">
          <formula>Middle value of the sorted dataset</formula>
          <shows>sorted list, count, result</shows>
        </function>

        <function option="3" name="Mode">
          <formula>Most frequently occurring value(s)</formula>
          <shows>numbers, mode value(s), frequency, multi-modal flag</shows>
          <note>Supports multi-modal datasets using Python's multimode()</note>
        </function>

        <function option="4" name="All Statistics">
          <shows>
            <field>Count</field>
            <field>Sum</field>
            <field>Mean</field>
            <field>Median</field>
            <field>Mode (with frequency)</field>
            <field>Min</field>
            <field>Max</field>
            <field>Range</field>
            <field>Standard Deviation (population)</field>
            <field>Variance</field>
          </shows>
        </function>
      </functions>
    </module>


    <!-- MODULE 3: PERCENTAGE TOOL -->
    <module id="percentage_tool" menu_option="3">
      <title>Percentage Tool</title>
      <description>Five dedicated percentage calculation modes.</description>

      <operations>
        <operation option="1" name="X% of Y">
          <formula>(X / 100) * Y</formula>
          <example>15% of 200 = 30</example>
        </operation>

        <operation option="2" name="Percentage Change">
          <formula>((B - A) / |A|) * 100</formula>
          <example>80 to 100 = +25% increase ▲</example>
          <example>100 to 80 = -20% decrease ▼</example>
        </operation>

        <operation option="3" name="X is what % of Y">
          <formula>(X / Y) * 100</formula>
          <example>45 out of 300 = 15%</example>
        </operation>

        <operation option="4" name="Add X% to Y">
          <formula>Y + (X / 100) * Y</formula>
          <example>200 + 10% = 220</example>
        </operation>

        <operation option="5" name="Subtract X% from Y">
          <formula>Y - (X / 100) * Y</formula>
          <example>200 - 10% = 180</example>
        </operation>
      </operations>
    </module>


    <!-- MODULE 4: EXPRESSION EVALUATOR -->
    <module id="expression_evaluator" menu_option="4">
      <title>Expression Evaluator</title>
      <description>Type raw arithmetic expressions directly. Input is sanitized before evaluation — no unsafe code can be executed.</description>

      <examples>
        <example input="3 + 4 * 2"     output="11"  />
        <example input="2 ** 8"         output="256" />
        <example input="100 / 5 - 3"   output="17"  />
        <example input="15 % 4"         output="3"   />
        <example input="(10 + 5) * 2"  output="30"  />
      </examples>

      <supported_operators>+ - * / % ** ^ ( )</supported_operators>
      <exit_commands>back · b · exit · q</exit_commands>

      <security>
        <measure>Allowed character whitelist enforced before eval()</measure>
        <measure>eval() called with empty __builtins__ — no access to Python internals</measure>
        <measure>ZeroDivisionError caught and reported gracefully</measure>
      </security>
    </module>

  </modules>


  <!-- ═══════════════════════════════════════════════════════ -->
  <!--                    TYPE CASTING                        -->
  <!-- ═══════════════════════════════════════════════════════ -->

  <type_casting id="type_casting">
    <title>Type Casting — Core Design Principle</title>
    <description>All user input is received as str and explicitly cast to numeric types before any computation. Invalid input triggers re-prompting — no silent failures, no crashes.</description>

    <cast id="1">
      <from>str</from>
      <to>float</to>
      <usage>Single number input</usage>
      <code><![CDATA[
raw = input("Enter number: ").strip()
value = float(raw)   # str → float
      ]]></code>
    </cast>

    <cast id="2">
      <from>str</from>
      <to>list[float]</to>
      <usage>Number list input (statistics)</usage>
      <code><![CDATA[
numbers = [float(x) for x in raw.replace(",", " ").split()]
# str → list[float]
      ]]></code>
    </cast>

    <cast id="3">
      <from>float</from>
      <to>str</to>
      <usage>Output formatting</usage>
      <code><![CDATA[
def fmt(n: float) -> str:
    return str(int(n)) if n == int(n) else f"{n:.8f}".rstrip("0")
# float → int (if whole) → str  OR  float → str
      ]]></code>
    </cast>

    <cast id="4">
      <from>str</from>
      <to>float (via eval)</to>
      <usage>Expression evaluator result</usage>
      <code><![CDATA[
result = eval(sanitized, {"__builtins__": {}})
fmt(float(result))   # numeric → float → formatted str
      ]]></code>
    </cast>

    <validation>
      <method>try/except ValueError wraps every float() cast</method>
      <behaviour>User is shown an error and re-prompted — program never exits unexpectedly</behaviour>
    </validation>
  </type_casting>


  <!-- ═══════════════════════════════════════════════════════ -->
  <!--                   ERROR HANDLING                       -->
  <!-- ═══════════════════════════════════════════════════════ -->

  <error_handling id="error_handling">
    <title>Error Handling</title>

    <errors>
      <error>
        <scenario>Non-numeric user input</scenario>
        <behaviour>Caught by ValueError — re-prompts with message</behaviour>
        <crashes>No</crashes>
      </error>

      <error>
        <scenario>Division by zero</scenario>
        <behaviour>Returns None from lambda, displays descriptive error</behaviour>
        <crashes>No</crashes>
      </error>

      <error>
        <scenario>Modulus by zero</scenario>
        <behaviour>Same as division by zero — safely handled</behaviour>
        <crashes>No</crashes>
      </error>

      <error>
        <scenario>Empty number list in statistics</scenario>
        <behaviour>ValueError raised internally — user re-prompted</behaviour>
        <crashes>No</crashes>
      </error>

      <error>
        <scenario>Percentage with zero denominator</scenario>
        <behaviour>Explicit check with descriptive error message</behaviour>
        <crashes>No</crashes>
      </error>

      <error>
        <scenario>Invalid menu choice</scenario>
        <behaviour>Prints error, loops back to menu</behaviour>
        <crashes>No</crashes>
      </error>

      <error>
        <scenario>Ctrl+C keyboard interrupt</scenario>
        <behaviour>Caught at menu level — returns to main menu gracefully</behaviour>
        <crashes>No</crashes>
      </error>

      <error>
        <scenario>Unsafe expression in evaluator</scenario>
        <behaviour>Character whitelist blocks it before eval() is called</behaviour>
        <crashes>No</crashes>
      </error>

      <error>
        <scenario>StatisticsError (no unique mode)</scenario>
        <behaviour>Caught explicitly — displays friendly message</behaviour>
        <crashes>No</crashes>
      </error>
    </errors>
  </error_handling>


  <!-- ═══════════════════════════════════════════════════════ -->
  <!--                   PROJECT STRUCTURE                    -->
  <!-- ═══════════════════════════════════════════════════════ -->

  <structure id="structure">
    <title>Project Structure</title>
    <tree><![CDATA[
calculus-python/
│
├── calculator.py       ← Main application (single-file, zero dependencies)
├── README.xml          ← Project documentation (XML format)
└── LICENSE             ← MIT License
    ]]></tree>

    <code_sections>
      <section name="HELPERS"                lines="17–50"  description="separator(), header(), section(), get_number(), get_number_list(), fmt()" />
      <section name="BASIC ARITHMETIC"       lines="53–97"  description="basic_calculator() — 6 arithmetic operations" />
      <section name="STATISTICS CALCULATOR"  lines="100–162" description="statistics_calculator(), _show_all_stats()" />
      <section name="PERCENTAGE CALCULATOR"  lines="165–226" description="percentage_calculator() — 5 percentage modes" />
      <section name="EXPRESSION EVALUATOR"   lines="229–258" description="expression_evaluator() — safe eval with whitelist" />
      <section name="MAIN MENU"              lines="261–300" description="main() — menu loop with KeyboardInterrupt handling" />
    </code_sections>
  </structure>


  <!-- ═══════════════════════════════════════════════════════ -->
  <!--                     REQUIREMENTS                       -->
  <!-- ═══════════════════════════════════════════════════════ -->

  <requirements id="requirements">
    <python_version minimum="3.10" />

    <stdlib_imports>
      <import module="statistics" items="mean, median, mode, multimode, StatisticsError" />
    </stdlib_imports>

    <third_party_packages>None</third_party_packages>

    <platform_support>
      <platform>Windows</platform>
      <platform>macOS</platform>
      <platform>Linux</platform>
    </platform_support>
  </requirements>


  <!-- ═══════════════════════════════════════════════════════ -->
  <!--                     CONTRIBUTING                       -->
  <!-- ═══════════════════════════════════════════════════════ -->

  <contributing id="contributing">
    <title>Contributing</title>
    <welcome>Contributions, issues, and feature requests are welcome!</welcome>

    <steps>
      <step number="1">Fork the repository</step>
      <step number="2">Create a feature branch:  git checkout -b feature/new-feature</step>
      <step number="3">Commit your changes:       git commit -m "Add new feature"</step>
      <step number="4">Push to the branch:        git push origin feature/new-feature</step>
      <step number="5">Open a Pull Request</step>
    </steps>

    <ideas>
      <idea>GUI version using tkinter or PyQt</idea>
      <idea>History log — save previous calculations to a file</idea>
      <idea>Unit converter module (km/miles, kg/lbs, etc.)</idea>
      <idea>Scientific calculator mode (sin, cos, log, sqrt)</idea>
      <idea>Export statistics report to CSV or JSON</idea>
    </ideas>
  </contributing>


  <!-- ═══════════════════════════════════════════════════════ -->
  <!--                       LICENSE                         -->
  <!-- ═══════════════════════════════════════════════════════ -->

  <license id="license">
    <type>MIT</type>
    <description>This project is open source and available under the MIT License. You are free to use, modify, and distribute this software with attribution.</description>
  </license>


  <!-- ═══════════════════════════════════════════════════════ -->
  <!--                       FOOTER                          -->
  <!-- ═══════════════════════════════════════════════════════ -->

  <footer>
    <tagline>Made with Python 🐍 — No dependencies. Just math.</tagline>
    <author>your-username</author>
    <repo>https://github.com/your-username/calculus-python</repo>
  </footer>

</readme>
