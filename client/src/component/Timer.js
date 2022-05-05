
const GetDisplayTime = (time) => {
    if (time < 0)
      return 0;
    let hours = Math.floor(time/3600);
    let minutes = Math.floor((time % 3600 ) / 60);
    let seconds = Math.floor((time % 3600 ) % 60);
    
    //prepend 0 for single digit values
    hours = hours < 10 ? "0" + hours : hours;
    minutes = minutes < 10 ? "0" + minutes : minutes;
    seconds = seconds < 10 ? "0" + seconds : seconds;
    return hours + ":" + minutes + ":" + seconds;
  };

  export default GetDisplayTime;