unit RandomSortTests;

interface

uses
  SysUtils;

type
  TIntArray = array of Integer;

procedure GenerateRandomNumbers(var numbers: TIntArray; fromVal, toVal, count: Integer);
procedure BubbleSort(var numbers: TIntArray);
procedure RunAllTests;

implementation

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
end;

procedure BubbleSort(var numbers: TIntArray);
var
  i, j, temp: Integer;
  swapped: Boolean;
begin
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
end;

function IsSorted(numbers: TIntArray): Boolean;
var
  i: Integer;
begin
  for i := 0 to Length(numbers) - 2 do
  begin
    if numbers[i] > numbers[i + 1] then
    begin
      IsSorted := False;
      Exit;
    end;
  end;
  IsSorted := True;
end;

procedure TestGenerateRandomNumbers;
var
  numbers: TIntArray;
  i, fromVal, toVal, count: Integer;
begin
  fromVal := 10;
  toVal := 20;
  count := 5;
  WriteLn('TEST 1: Test Generate Random Numbers');
  GenerateRandomNumbers(numbers, fromVal, toVal, count);
  for i := 0 to count - 1 do
    Assert((numbers[i] >= fromVal) and (numbers[i] <= toVal), 'Number out of range');
end;

procedure TestBubbleSort;
var
  numbers: TIntArray;
begin
  numbers := [5, 3, 8, 1, 2];
  WriteLn('TEST 2: Test Bubble Sort');
  BubbleSort(numbers);
  Assert(IsSorted(numbers), 'BubbleSort failed');
end;

procedure TestBubbleSortEmpty;
var
  numbers: TIntArray;
begin
  SetLength(numbers, 0);
  WriteLn('TEST 3: Test Bubble Sort Empty');
  BubbleSort(numbers);
  Assert(IsSorted(numbers), 'BubbleSort failed on empty array');
end;

procedure TestBubbleSortSingle;
var
  numbers: TIntArray;
begin
  numbers := [7];
  WriteLn('TEST 4: Test Bubble Sort Single');
  BubbleSort(numbers);
  Assert(IsSorted(numbers), 'BubbleSort failed on single element array');
end;

procedure TestBubbleSortSorted;
var
  numbers: TIntArray;
begin
  numbers := [1, 2, 3, 4, 5];
  WriteLn('TEST 5: Test Bubble Sort Sorted');
  BubbleSort(numbers);
  Assert(IsSorted(numbers), 'BubbleSort failed on already sorted array');
end;

procedure RunAllTests;
begin
  TestGenerateRandomNumbers;
  TestBubbleSort;
  TestBubbleSortEmpty;
  TestBubbleSortSingle;
  TestBubbleSortSorted;
  WriteLn('All tests passed!');
end;

end.
