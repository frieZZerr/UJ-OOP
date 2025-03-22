program RandomSort;

uses
  SysUtils, RandomSortTests;

var
  numbers: TIntArray;
  fromVal, toVal, count: Integer;
  choice: Char;
begin
  WriteLn('Random Number Generation and Bubble Sort Program');
  WriteLn('----------------------------------------------');

  WriteLn('Do you want to run tests? (y/n)');
  ReadLn(choice);
  
  if (choice = 'y') or (choice = 'Y') then
  begin
    RunAllTests;
    Exit;
  end;

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

  WriteLn('Random generated numbers:');
  for fromVal := 0 to High(numbers) do
    Write(numbers[fromVal], ' ');
  WriteLn;
  
  BubbleSort(numbers);

  WriteLn('Sorted numbers:');
  for fromVal := 0 to High(numbers) do
    Write(numbers[fromVal], ' ');
  WriteLn;
end.
