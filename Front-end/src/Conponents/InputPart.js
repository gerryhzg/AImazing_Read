import React,{useState} from 'react'
import "./InputPart.css"
import axios from 'axios'
import { AiOutlineLoading } from 'react-icons/ai'


export default function InputPart({Done,DataResult,SetDataResult}) {

  const [FileText,SetFileText] = useState("")

  const [ContentText,SetContentText] = useState("")

  const [Loading,SetLoading] = useState(false)

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = () => {
        SetContentText(reader.result);
        console.log(reader.result)
      };
      reader.readAsText(file);
    }
  };

  function Generate(){
    SetLoading(true)
    axios.post("http://127.0.0.1:5000/generate",{
      Content:FileText!=="" ? (FileText) : (ContentText)
    }).then((respone)=>{
      console.log(respone.data)
      SetDataResult({
        Video:respone.data.Video,
        Images:respone.data.Images,
        Content:respone.data.Content,
        Voices:respone.data.Voices,
        Bgm:respone.data.Bgm
      })
      SetLoading(false)
      Done()
    })
  }

  return (
    <div className='InputPart_Main_Div' >
      <div className='cloumn'>
      <div className='row'>
        <label>Input Your Article</label>
        <input type='file' id='file-upload' onChange={handleFileChange} style={{display:'none'}}/>
        <label className='upload_file' for="file-upload">Upload File</label>
      </div>
        
      <textarea value={ContentText} onChange={ (e)=>{SetContentText(e.target.value)} } />

      <button onClick={()=>{Generate()}}>Generate</button>

      {Loading && <div className='Loading_Div'>
        <AiOutlineLoading className='icon'/>
        <label>Generating...</label>
        </div>}
      </div>
      
    </div>
  )
}
