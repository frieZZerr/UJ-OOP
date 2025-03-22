program RandomSort;
uses
  SysUtils;

type
  TIntArray = array of Integer;


procedure GenerateRandomNumbers(var numbers: TIntArray; fromVal, toVal, count: Integer);
var
  i: Integer;
  range: Integer;
begin
  SetLength(numbers, count);
  Randomize;

  range := toVal - fromVal + 1;
  
  for i := 0 to count - 1 do
    numbers[i] := fromVal + Random(range);
    
  WriteLn('Generated ', count, ' random numbers between ', fromVal, ' and ', toVal, ':');
  for i := 0 to count - 1 do
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
  fromVal, toVal, count: Integer;
  choice: Char;
begin
  WriteLn('Random Number Generation and Bubble Sort Program');
  WriteLn('----------------------------------------------');
  
  WriteLn('Do you want to use custom parameters for random number generation? (y/n)');
  ReadLn(choice);
  
  if (choice = 'y') or (choice = 'Y') then
  begin
    Write('Enter minimum value: ');
    ReadLn(fromVal);
    
    Write('Enter maximum value: ');
    ReadLn(toVal);
    
    Write('Enter number of values to generate: ');
    ReadLn(count);
    
    GenerateRandomNumbers(numbers, fromVal, toVal, count);
  end
  else
  begin
    GenerateRandomNumbers(numbers, 0, 100, 50);
  end;
  
  BubbleSort(numbers);
end.
