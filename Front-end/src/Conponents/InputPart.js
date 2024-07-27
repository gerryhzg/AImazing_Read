import React,{useState} from 'react'
import "./InputPart.css"
import axios from 'axios'

export default function InputPart({Done,DataResult,SetDataResult}) {

  const [FileText,SetFileText] = useState("")

  const [ContentText,SetContentText] = useState("")

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = () => {
        SetFileText(reader.result);
      };
      reader.readAsText(file);
    }
  };

  function Generate(){
    axios.post("http://localhost:5000/generate",{
      Content:FileText!=="" ? (FileText) : (ContentText)
    }).then((respone)=>{
      SetDataResult({
        Video:respone.data.Video,
        Images:respone.data.Images,
        Content:respone.data.Content,
        Voices:respone.data.Voices,
        Bgm:respone.data.Bgm
      })
      Done()
    })
  }

  return (
    <div className='InputPart_Main_Div'>
      <div className='row'>
        <label>Input Your Article</label>
        <input type='file' id='file-upload' onChange={handleFileChange} style={{display:'none'}}/>
        <label className='upload_file' for="file-upload">Upload File</label>
      </div>
        
      <textarea onChange={ (e)=>{SetContentText(e.target.value)} } />

      <button onClick={()=>{Done()}}>Generate</button>
    </div>
  )
}
