program RandomNumbers;
uses
  SysUtils;

type
  TIntArray = array of Integer;


procedure Generate50RandomNumbers(var numbers: TIntArray);
var
  i: Integer;
begin
  SetLength(numbers, 50);
  Randomize;
  
  for i := 0 to 49 do
    numbers[i] := Random(101);
    
  WriteLn('Generated 50 random numbers between 0 and 100:');
  for i := 0 to 49 do
    Write(numbers[i], ' ');
  WriteLn;
end;


var
  numbers: TIntArray;
begin
  WriteLn('Random Number Generation Program');
  WriteLn('------------------------------');
  
  Generate50RandomNumbers(numbers);
end.
