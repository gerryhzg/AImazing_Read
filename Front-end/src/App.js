import './App.css';
import { useState } from 'react';
import Example from './Conponents/Example';
import InputPart from './Conponents/InputPart';
import OutputPart from './Conponents/OutputPart';

function App() {

  const [DisplayState,SetDisplayState] = useState("Input")

  const [DataResult,SetDataResult] = useState(
    {
      Video:"",
      Images:[],
      Content:[],
      Voices:[],
      Bgm:""
    }
  )

  return (
    <div className="App_Main_Div">      

      { DisplayState === "Input" &&<>
          <div className='Logo_Div'>
          <label>Almazing Read</label>
          <p>AI Turn difficult article in to simple Story for kids!</p>
        </div>
        <Example/>
      </> }

      {
        DisplayState === "Input" ?( <InputPart SetDataResult={SetDataResult} DataResult={DataResult} Done={()=>{SetDisplayState("Output")}}/> ):( <OutputPart DataResult={DataResults}/> )
      }

    </div>
  );
}

export default App;
