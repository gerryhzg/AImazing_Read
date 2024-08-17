import React,{useEffect, useState} from 'react'
import Book from './Book'
import Animate from './Animate'
import "./OutputPart.css"

export default function OutputPart({DataResult}) {
  const [OutputType,SetOutputType] = useState("Book")

  const PlaySound = (url) => {
    const audio = document.getElementById('my-audio');
    audio.src = url
    audio.currentTime = 0; // Rewind to the start
    audio.play().catch(error => {
        console.error('Error playing sound:', error);
    });
  }

  useEffect(()=>{
    PlaySound('http://127.0.0.1:5000/AI_end/Media/BackgroundMusic/happy.mp3')
  },[])
  return (
    <div className='Output_Main_Div'>

      <audio id="my-audio" style={{display:"none"}} preload="auto"></audio>

      <div className='Btn_Div'>
        <button onClick={()=>{SetOutputType("Book");PlaySound('http://127.0.0.1:5000/AI_end/Media/BackgroundMusic/happy.mp3')}} style={{backgroundColor:(OutputType==="Book"&&"rgb(241, 100, 34)"),color:(OutputType==="Book"&&"white")}}>Book</button>
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
