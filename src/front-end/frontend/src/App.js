import logo from './logo.svg';
import './App.css';
import React from 'react'; 
import axios from 'axios'; 

class App extends React.Component {

  state = {
    entradas: [],
  }

  componentDidMount() {

    let data;

    axios.get('http://localhost:8000/api/')
      .then(res => {
        data = res.data;
        this.setState({
          entradas: data
        });
      })
      .catch(err => { })
  }

  render() {
    return (
      <div>
        {this.state.entradas.map((entradas, id) => (
          <div key={id}>
            <div >
              <div >
                <div class="card">
                  <img class="card-img-top" src="https://dummyimage.com/318x100/0011ff/ffffff.jpg" alt="Card image top"></img>
                  <div class="card-body">
                    <h4 class="card-title">{entradas.titulo}</h4>
                    <p class="card-text">{entradas.cuerpo}</p>
                    <cite title="Source Title">{entradas.autor}</cite>
                    <a href="#!" class="btn btn-primary">Go somewhere</a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )
        )}
      </div>
    );
  }


}
export default App;