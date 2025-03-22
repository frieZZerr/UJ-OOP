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


procedure BubbleSort(var numbers: TIntArray);
var
  i, j, temp: Integer;
  swapped: Boolean;
begin
  WriteLn('Sorting numbers using bubble sort...');
  
  for i := Length(numbers) - 1 downto 0 do
  begin
    swapped := False;
    for j := 0 to i - 1 do
    begin
      if numbers[j] > numbers[j + 1] then
      begin
        temp := numbers[j];
        numbers[j] := numbers[j + 1];
        numbers[j + 1] := temp;
        swapped := True;
      end;
    end;
    if not swapped then
      Break;
  end;
  
  WriteLn('Sorted numbers:');
  for i := 0 to Length(numbers) - 1 do
    Write(numbers[i], ' ');
  WriteLn;
end;


var
  numbers: TIntArray;
begin
  WriteLn('Random Number Generation Program');
  WriteLn('------------------------------');
  
  Generate50RandomNumbers(numbers);

  BubbleSort(numbers);
end.
