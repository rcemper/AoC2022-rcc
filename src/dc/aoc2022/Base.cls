Class dc.aoc2022.Base
{

Parameter Folder = "/irisdev/app/data/";

ClassMethod GetInput(fn) As %Stream
{
   
    set fn=..#Folder_fn
    set stream = ##Class(%Stream.FileCharacter).%New()
    set sc=stream.LinkToFile(fn)
    if sc break      ;to avoid smell
    return stream
}

}
