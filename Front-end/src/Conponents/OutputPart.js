import React,{useState} from 'react'
import Book from './Book'
import Animate from './Animate'
import "./OutputPart.css"

export default function OutputPart({DataResult}) {
  const [OutputType,SetOutputType] = useState("Book")
  return (
    <div className='Output_Main_Div'>

      <div className='Btn_Div'>
        <button onClick={()=>{SetOutputType("Book")}} style={{backgroundColor:(OutputType==="Book"&&"rgb(241, 100, 34)"),color:(OutputType==="Book"&&"white")}}>Book</button>
        <button onClick={()=>{SetOutputType("Animate")}} style={{backgroundColor:(OutputType!=="Book"&&"rgb(241, 100, 34)"),color:(OutputType!=="Book"&&"white")}}>Animate</button>
      </div>

      <div className='Display_Div'>
        {
          OutputType === "Book" ? (<Book DataResult={DataResult}/>) : (<Animate/>)
        }
      </div>

    </div>
  )
}
