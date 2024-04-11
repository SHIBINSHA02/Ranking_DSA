import './App.css';

function App() {
  return (
    <div class="form-container">
    <h2>Enter Google Form Link</h2>
    <form id="googleForm">
        <div class="form-group">
            <label for="formLink">Google Form Link:</label>
            <input type="text" id="formLink" name="formLink" placeholder="Enter Google Form Link" required/>
        </div>
        <div class="form-group">
            <input type="submit" value="Submit"/>
        </div>
    </form>
</div>

  );
}

export default App;
