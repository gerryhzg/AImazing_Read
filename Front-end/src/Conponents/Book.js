import React,{useState} from 'react'
import "./Book.css"
export default function Book({DataResult}) {
    

    let CurrentPage = 0

    const [CurrentImage,SetCurrentImage] = useState(DataResult["Images"][0])

    const [CurrentContent,SetCurrentContent] = useState(DataResult["Content"][0])

    const [CurrentVoice,SetCurrentVoice] = useState(DataResult["Voices"][0])

    function NextPage(){
        if ( CurrentPage < DataResult["Images"].length ){
            CurrentPage += 1
            SetCurrentImage(DataResult["Images"][CurrentPage])
            SetCurrentContent(DataResult["Content"][CurrentPage])
            SetCurrentVoice(DataResult["Voices"][CurrentPage])
        }
    }

    function BackPage(){
        if ( CurrentPage > 0 ){
            CurrentPage -= 1
            SetCurrentImage(DataResult["Images"][CurrentPage])
            SetCurrentContent(DataResult["Content"][CurrentPage])
            SetCurrentVoice(DataResult["Voices"][CurrentPage])
        }
    }


  return (
    <div className='Book_Main_Div'>

        <div className='Content_Div'>
            {
                CurrentImage && 
                <img src={CurrentImage} />
            }
            <div className='Text_Content'>
                <p>
                    {CurrentContent}
                </p>
            </div>
        </div>

        <div className='Control_Div'>
            <button onClick={BackPage}>Back</button>
            <button onClick={NextPage}>Next Page</button>
        </div>

    </div>
  )
}
